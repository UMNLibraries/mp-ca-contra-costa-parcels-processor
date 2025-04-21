from collections import namedtuple
from functools import reduce
import numpy as np
from pathlib import Path
from pprint import pprint
import re

import pandas as pd
import geopandas as gpd

def named_capture(name, pattern):
    return r'(?P<{name}>'.format(name=name) + pattern + r')'

def plat(pattern):
    return named_capture('plat', pattern)

def anchored_pattern(pattern):
    return r'^' + pattern + r'$'

def join_ws(*patterns):
    return ws.join(patterns)

# Full regex for Washington Co, MN:
#regex = r'(?P<lot_regex>^LOTS? [\d &\-,]+(?:AND)?(?:THRU)?(?: LOT)?[\d &\-,]+)(?:BLOCK )?(?P<blk_regex>(?<=BLOCK )\d+)?.+(?P<plat_regex>(?<=SubdivisionName )[A-Z \-\.\d\'#]+(?![a-z]))'

ws = r'\s*'

ordinal_indicator = r'(11TH|12TH|13TH|\d*(1ST|2N?D|3RD|[04-9]TH))\s*(,\.)?'
#ordinal_phrase = r'(NUMBER|NO(\s*\.)?|#)?\s*\d+\s*(,|\.)?'
ordinal_phrase = r'(NUMBER|NO(\s*\.)?|#)\s*\d+\s*(,|\.)?'

old_sid_prefix = r'(?:\*?OLD SID \-?\s?[A-Z\d]{1,2}[\s\d\-]+ [A-Z]+(?: CITY)? [\dA-Z]+\-[\dA-Z]+ (?=LOT))?'
ypsi_prefix = r'(?:(?:YP#?(?: CITY)? ?[\dA-Z\-:]+ (?=LOT))|(?:YP (?=LOT)))?'

#r'(?P<lot>^LOTS? [\d &\-,]+(?:AND)?(?:THRU)?(?: LOT)?[\d &\-,])' # Washington Co, MN lot regex
#r'(?P<lot>^LOTS?\s+[\d &\-,]+(?:AND)?(?:THRU)?(?:\s+LOT)?[\d &\-,])' # variation on the above
#lot = r'LOTS?\s*[\d #&,\-]+'
#lot = named_capture('lot', r'LOTS?\s*[\d #&,\-]+((AND|THRU)(\s*LOT)?\s*\d+)?\s*(,|\.)?')
#lot = named_capture('lot', r'LOTS?\s*[\d #&,\-]+((AND|THRU)(\s*LOT)?\s*\d+)?\s*(INCLUSIVE|INCL|INC)?(,|\.)?')
lot = named_capture('lot', r'LOTS?\s*[\-\d]+[\d #&,\-]*((AND|THRU)(\s*LOT)?\s*\d+)?\s*(INCLUSIVE|INCL|INC)?(,|\.)?')

#lot_alpha = r'LOTS?\s+[A-Za-z #&,\-]+((AND|THRU)(\s*LOT)?\s+[A-Za-z])?\s*(,|\.)?'
#lot_alpha = r'LOT\s+[A-Za-z]+(\s*(,|\.))?'
#lot_alpha = r'LOT\s+[A-Z]{1,2}'
#lot_alpha = named_capture('lot', r'LOT\s+[A-Za-z]+?\s*(,|\.)?')
lot_alpha = named_capture('lot', r'LOT\s+[A-Za-z]+\s*(,|\.)?')

lot_ordinal_phrase = named_capture('lot', r'LOT' + ws + ordinal_phrase)

# Variations on the Washington Co, MN block regex
#r'(?:BLK )?(?P<block>(?<=BLK )\d+)?' 
#r'((BLK|BLOCK)?\s+(?(1)(?P<block>\d+)))?\s*,?'
block = named_capture('block', r'BL(OC)?K\s+\d+\s*(,|\.)?')

#addition_num = r"(\d+[A-Za-z]+(,\.)?\s+)?(ADDITION|ADD'?N)" # This doesn't seem to work to match ADDN without an ordinal preceding it...
#addition_num = r"(\d+[A-Za-z]+(,\.)?\s+)?(ADDITION|ADDN)"

#addition = r"(ADDITION|ADD'?N)"
addition = r"(ADDITION|ADD'?N)(,|\.)?"

#addition_num = ordinal_indicator + ws + r"(ADDITION|ADD'?N)"
addition_num = ordinal_indicator + ws + r"(ADDITION|ADD'?N)(,|\.)?"
addition_ordinal_indicator = ordinal_indicator + ws + addition

subdivision = r'(SUBD?|SUBDIVISION)'
subdivision_num = subdivision + ws + r'\d+'
subdivision_ordinal_phrase = subdivision + ws + ordinal_phrase

# Parent parcels may be a sign of duplicate lot, block, & plat data for properties that are actually different. Check for duplicates!
parent_parcels = r'PARENT\s+PARCEL\s+(K\s+\d+-\d+-\d+-\d+,?\s*)+'

corner = r'COR(\s+OF)?'

# Township-Range-Section data, from the Public Land Survery System (PLSS): https://en.wikipedia.org/wiki/Public_Land_Survey_System
part = r'(PART\s+OF\s+THE|PART\s+OF|PART|PT)'
directional_fraction = r'[NESW]{1,2}\s+\d+/\d+(,|\.)?' # This sometimes fails for two-direction abbreviations, e.g., NE, SW
#directional_fraction = r'[NESW]{2}\s+\d+/\d+(,|\.)?'
section = r'(SECTION|SECT|SEC)\.?\s+\d+(,|\.)?'
# T = township, R = range. Example: T1S-R5E Not sure why we sometimes have a B instead of a T... Maybe B = boundary or baseline?
township = r'(B|T)\d+[NESW](,|\.)?' # Mike thinks the Bs may stand for block. Ask Justin for map of Lawrence & Maynards Addition for more context
_range = r'R\d+[NESW](,|\.)?'
township_range = township + r'[, \-]+' + _range

# References to books (liber) of plat information, with page numbers and dates
liber = r'LIBER\s+\d+\s+OF\s+PLATS,?' 
page = r'PAGE\s+\d+,?'
pages = r'PAGES\s+\d+-\d+,?'
mmddyyyy = r'\d{2}/\d{2}/\d{4}'
mmddyy = r'\d{2}/\d{2}/\d{2}'

# Guessing that this is acres. Example: 0.54 AC.
acres = r'\d*\.\d+\s+AC(,|\.)?'

# Split on some date from other PINs:
split_on = r'SPLIT(/COMBINED)?\s+ON'
split_on_date = split_on + ws + r'(' + mmddyyyy + r'|' + mmddyy + r')'

# What are these TH's?
# LOT 36, SCIO HILLS NO. 2 SUB, TH N 07-20-05 E 230.OO FT, TH S 70-17-10 E 225.30 FT, TH S 38-25-00 W 19.50 FT, TH S 07-20-05 W 165.00 FT, TH N 82-39-55 W 209.99 FT TO THE POB. PT SE 1/4 SEC 14, T2S-R5E, 1.00 AC.

NamedPattern = namedtuple('NamedPattern', 'name pattern')
NamedRegex = namedtuple('NamedRegex', 'name regex')

patterns = [
    NamedPattern(
        'non-numeric plat not starting with EXC',
        ypsi_prefix + old_sid_prefix + lot + r'(?!\s*EXC)' + plat(r'\D+')
    ), # 11024 matches
    NamedPattern(
        'lot ordinal phrase & non-numeric plat not starting with EXC',
        ypsi_prefix + old_sid_prefix + lot_ordinal_phrase + r'(?!\s*EXC)' + plat(r'\D+')
    ), # 6
    NamedPattern(
        'alphabetic lot & non-numeric plat not starting with EXC',
        ypsi_prefix + old_sid_prefix + lot_alpha + r'(?!\s*EXC)' + plat(r'\D+')
    ), # 3
    NamedPattern(
        'lot ordinal phrase, block & non-numeric plat not starting with EXC',
        ypsi_prefix + old_sid_prefix + lot_ordinal_phrase + ws + block + r'(?!\s*EXC)' + plat(r'\D+')
    ), # 0
    NamedPattern(
        'non-numeric plat up to subdivision ordinal phrase',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + subdivision_ordinal_phrase)
    ), # 2587
    NamedPattern(
        'non-numeric plat up to subdivision #',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + subdivision_num)
    ), # 14
    NamedPattern(
        'non-numeric plat except for subdivision ordinal phrase in the middle',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + subdivision_ordinal_phrase + r'\D+')
    ), # 18
    NamedPattern(
        'block & non-numeric plat except for subdivision ordinal phrase in the middle',
        ypsi_prefix + old_sid_prefix + lot + ws + block + plat(r'\D+?' + subdivision_ordinal_phrase + r'\D+')
    ), # 0
    NamedPattern(
        'non-numeric plat up to addition ordinal indicator',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + addition_ordinal_indicator)
    ), # 67
    NamedPattern(
        'alphabetic lot & non-numeric plat up to addition ordinal indicator',
        ypsi_prefix + old_sid_prefix + lot_alpha + plat(r'\D+' + addition_ordinal_indicator)
    ), # 6
    NamedPattern(
        'non-numeric plat except for addition ordinal indicator in the middle',
        #lot + plat(r'\D+' + addition_ordinal_indicator + r'\D+')
        #lot + plat(r'\D+?' + addition_ordinal_indicator + r'\D+')
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+?' + r'(?=\d)' + addition_ordinal_indicator + r'\D+')
    ), # 0
    NamedPattern(
        'block & non-numeric plat up to addition ordinal indicator',
        ypsi_prefix + old_sid_prefix + lot + ws + block + plat(r'\D+' + addition_ordinal_indicator)
    ), # 4
    NamedPattern(
        'township range & non-numeric plat up to addition ordinal indicator',
        ypsi_prefix + old_sid_prefix + lot + ws + township_range + ws + plat(r'\D+' + addition_ordinal_indicator)
    ), # 40
    NamedPattern(
        'township & non-numeric plat up to addition ordinal indicator',
        ypsi_prefix + old_sid_prefix + lot + ws + township + ws + plat(r'\D+' + addition_ordinal_indicator)
    ), # 4
    NamedPattern(
        'township range & non-numeric plat up to addition',
        ypsi_prefix + old_sid_prefix + lot + ws + township_range + ws + plat(r'\D+' + addition)
    ), # 103
    NamedPattern(
        'township range & non-numeric plat',
        ypsi_prefix + old_sid_prefix + lot + ws + township_range + ws + plat(r'\D+')
    ), # 29
    NamedPattern(
        'non-numeric plat up to ordinal phrase',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + ordinal_phrase)
    ), # 4288, 4182
    NamedPattern(
        'non-numeric plat up to #',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + r'\d+')
    ), # 106 (4182 + 106 = 4288)
    NamedPattern(
        'non-numeric plat up to ordinal phrase, followed by split on date',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + ordinal_phrase) + ws + split_on_date + (r'.*')
    ), # 17
    NamedPattern(
        'non-numeric plat up to addition ordinal indicator, followed by split on date',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + addition_ordinal_indicator) + ws + split_on_date + (r'.*')
    ), # 2
    NamedPattern(
        'block & non-numeric plat, followed by split on date',
        ypsi_prefix + old_sid_prefix + lot + ws + block + plat(r'\D+?') + ws + split_on_date + (r'.*')
    ), # 5
    NamedPattern(
        'non-numeric plat, followed by split on date',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+?') + ws + split_on_date + (r'.*')
    ), # 73
    NamedPattern(
        'non-numeric plat up to subdivision, followed by parent parcels',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + subdivision_ordinal_phrase) + ws + parent_parcels
    ), # 206
    NamedPattern(
        'non-numeric plat up to digits and non-alpha chars, followed by part of TWS & acres',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+\d+\s*(,|\.)?\s+') + join_ws(part, directional_fraction, section, township_range, acres)
    ), # 114
    NamedPattern(
        'non-numeric plat up to subdivision ordinal phrase, followed by part of TWS',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + subdivision_ordinal_phrase) + ws + join_ws(part, directional_fraction, section, township_range)
    ), # 132
    NamedPattern(
        'non-numeric plat up to subdivision ordinal phrase, followed by part of TWS with multiple directional fractions, liber, pages, and date',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + subdivision_ordinal_phrase) + ws + join_ws(part, directional_fraction + r'\s+AND\s+' + directional_fraction, section, township_range, liber, pages, mmddyy)
    ), # 83
    NamedPattern(
        'non-numeric plat up to subdivision ordinal phrase, followed by TWS, liber, pages, and date',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + subdivision_ordinal_phrase) + ws + join_ws(directional_fraction, section, township_range, liber, pages, mmddyy)
    ), # 74
    NamedPattern(
        'non-numeric plat, followed by as-recorded-in-liber',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+?') + ws + join_ws(r'AS RECORDED IN', liber, page) + r'\D+'
    ), # 20
    NamedPattern(
        'non-numeric plat up to subdivision ordinal phrase, followed by TWS, the rest non-numeric',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + subdivision_ordinal_phrase) + ws + township_range + r'\D+'
    ), # 86
    NamedPattern(
        'non-numeric plat up to digits and non-alpha chars, followed by part of TWS',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+\d+\s*(,|\.)?\s+') + join_ws(part, directional_fraction, section, township_range)
    ), # 156
    NamedPattern(
        'non-numeric plat followed by part of TWS & acres',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+') + join_ws(part, directional_fraction, section, township_range, acres)
    ), # 184
    NamedPattern(
        'block & non-numeric plat followed by part of TWS & acres',
        ypsi_prefix + old_sid_prefix + lot + ws + block + plat(r'\D+') + join_ws(part, directional_fraction, section, township_range, acres)
    ), # 4
    NamedPattern(
        'block & non-numeric plat followed by part of TWS',
        ypsi_prefix + old_sid_prefix + lot + ws + block + plat(r'\D+') + join_ws(part, directional_fraction, section, township_range)
    ), # 4
    NamedPattern(
        'non-numeric plat followed by section, township range, acres',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+') + join_ws(section, township_range, acres)
    ), # 32
    NamedPattern(
        'non-numeric plat followed by directional fraction, section, township range, acres',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+?') + join_ws(directional_fraction, section, township_range, acres)
    ), # 11
    NamedPattern(
        'non-numeric plat followed by part of TWS',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+') + join_ws(part, directional_fraction, section, township_range)
    ), # 313
    NamedPattern(
        'non-numeric plat with addition ordinal indicator in the middle, followed by part of TWS',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + addition_ordinal_indicator + r'\D+') + join_ws(part, directional_fraction, section, township_range)
    ), # 1
    NamedPattern(
        'non-numeric plat followed by part of TWS followed by non-numeric string',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+') + join_ws(part, directional_fraction, section, township_range + r'\D+')
    ), # 35
    NamedPattern(
        'non-numeric plat up to ordinal phrase, followed by part of TWS followed by non-numeric string',
        ypsi_prefix + old_sid_prefix + lot + plat(r'\D+' + ordinal_phrase) + ws + join_ws(part, directional_fraction, corner, section, township_range, r'\D+')
    ), # 79
    NamedPattern(
        'block & non-numeric plat',
        ypsi_prefix + old_sid_prefix + lot + ws + block + plat(r'\D+'),
    ), # 284
    NamedPattern(
        'block & non-numeric plat up to digits, maybe followed by punctuation',
        ypsi_prefix + old_sid_prefix + lot + ws + block + plat(r'\D+\d+\s*\.?$'),
    ), # 44
]
processing_regexes = assorting_regexes = [
    NamedRegex(
        item.name,
        re.compile(anchored_pattern(item.pattern))
    ) for item in patterns
]

def process(infile, outdir):
    parcels = gpd.read_file(infile.name)

    new_columns = ['lot', 'block', 'plat']
    parcels[new_columns] = ''

    for named_regex in processing_regexes:
        parcels.loc[
            parcels['lot'].isin([np.nan, '']), new_columns
        ] = parcels['LEGAL_DESC'].str.extract(named_regex.regex)

    parcels[new_columns].map(lambda x: str(x).strip())

    outdir = Path(outdir)
    outdir.mkdir()
    parcels.to_file(outdir.joinpath(outdir.name + '.shp'))

def analyze(infile):
    parcels = gpd.read_file(infile.name)
    print(parcels.info())

    parcels_legal_notnull = parcels[parcels['LEGAL_DESC'].notnull()]
    print(f'{len(parcels_legal_notnull.index)=}')

    parcels_legal_lot = parcels_legal_notnull[parcels_legal_notnull['LEGAL_DESC'].str.match(r'^LOT')]
    print(f'{len(parcels_legal_lot.index)=}')

    parcels_legal_notlot = parcels_legal_notnull[~parcels_legal_notnull['LEGAL_DESC'].str.match(r'^LOT')]
    print(f'{len(parcels_legal_notlot.index)=}')
    print(parcels_legal_notlot[['PIN','LEGAL_DESC']].head(n=100))

    parcels_lot_notnull = parcels[parcels['lot'].notnull()]
    print(f'{len(parcels_lot_notnull.index)=}')
    print(parcels_lot_notnull[['PIN','lot','block','plat']].head(n=100))

    # 0 matches
    #parcels_legal_ws_lot = parcels_legal_notnull[parcels_legal_notnull['LEGAL_DESC'].str.match(r'^\s+LOT')]
    #print(f'{len(parcels_legal_ws_lot.index)=}')

    # 0 matches
    #parcels_legal_ws = parcels_legal_notnull[parcels_legal_notnull['LEGAL_DESC'].str.match(r'^\s+$')]
    #print(f'{len(parcels_legal_ws.index)=}')

#    if len(parcels_legal_ws.index):
#        parcels_legal_nonws = parcels[~parcels['LEGAL_DESC'].str.match(r'^\s+$')]
#        print('parcels with non-whitespace legal descriptions:')
#        print(parcels_legal_nonws.info())
#    else:
#        print('no parcels with all whitespace legal descriptions')

def assort(infile):
    parcels = gpd.read_file(infile.name)

    assorted = {'unmatched': []} # 2504
    for named_regex in assorting_regexes: 
        assorted[named_regex.name] = []

    pin_legal = parcels[(parcels['LEGAL_DESC'].notnull()) & (parcels['LEGAL_DESC'].str.startswith('LOT'))][['PIN','LEGAL_DESC']].to_dict('records')
    #for d in sorted(pin_legal, key=lambda d: d['LEGAL_DESC']):
    for d in sorted(pin_legal, key=lambda d: d['PIN']):
        matched = False
        for named_regex in assorting_regexes:
            if named_regex.regex.match(d['LEGAL_DESC']):
                assorted[named_regex.name].append(d)
                matched = True
                break
        if not matched:
            assorted['unmatched'].append(d)

    for regex_name, matches in assorted.items():
        print(f"'{regex_name}': {len(matches)} matches")
        for d in matches:
            print('  ', d)

