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

# old_sid_prefix = r'(?:\*?OLD SID \-?\s?[A-Z\d]{1,2}[\s\d\-]+ [A-Z]+(?: CITY)? [\dA-Z]+\-[\dA-Z]+ (?=LOT))?'
# ypsi_prefix = r'(?:(?:YP#?(?: CITY)? ?[\dA-Z\-:]+ (?=LOT))|(?:YP (?=LOT)))?'

x_feet_of_lot = r'([NSEW] \d+ FT )?'

#r'(?P<lot>^LOTS? [\d &\-,]+(?:AND)?(?:THRU)?(?: LOT)?[\d &\-,])' # Washington Co, MN lot regex
#r'(?P<lot>^LOTS?\s+[\d &\-,]+(?:AND)?(?:THRU)?(?:\s+LOT)?[\d &\-,])' # variation on the above
#lot = r'LOTS?\s*[\d #&,\-]+'
#lot = named_capture('lot', r'LOTS?\s*[\d #&,\-]+((AND|THRU)(\s*LOT)?\s*\d+)?\s*(,|\.)?')
#lot = named_capture('lot', r'LOTS?\s*[\d #&,\-]+((AND|THRU)(\s*LOT)?\s*\d+)?\s*(INCLUSIVE|INCL|INC)?(,|\.)?')
lot = named_capture('lot', fr'(?<! POR ){x_feet_of_lot}LO?TS?\s*[\-\d]+[\d #&,\-]*((AND|THRU|&|TO)?{x_feet_of_lot}(\s*LO?T)?\s*\d+)?\s*(INCLUSIVE|INCL|INC)?(,|\.)?')

#lot_alpha = r'LOTS?\s+[A-Za-z #&,\-]+((AND|THRU)(\s*LOT)?\s+[A-Za-z])?\s*(,|\.)?'
#lot_alpha = r'LOT\s+[A-Za-z]+(\s*(,|\.))?'
#lot_alpha = r'LOT\s+[A-Z]{1,2}'
#lot_alpha = named_capture('lot', r'LOT\s+[A-Za-z]+?\s*(,|\.)?')
lot_alpha = named_capture('lot', r'LO?T\s+[A-Za-z]+\s*(,|\.)?')

lot_plus_por = named_capture('lot', r'LO?TS?\s+\d+[A-Z]*(?: & \d+)?(?: &)? POR \d+[\d& ]*')

# lot_por_only = named_capture('lot', r'(?:POR )?LO?TS?\s+\d+[A-Z]*(?: & \d+[A-Z]*)?\s*(,|\.)?')
lot_por_only = named_capture('lot', r'(?:POR )?LO?TS?\s+[,&\d ]+[A-Z]?(?: & )?[,&\d]+[A-Z]*')
lot_por_only_simple = named_capture('lot', r'POR(?: LO?TS?)?\s+[\dA-Z,]+')

# RICH PULLMAN PUEBLO LT 29 & POR 30 BLK 21

lot_ordinal_phrase = named_capture('lot', r'LOT' + ws + ordinal_phrase)

# Variations on the Washington Co, MN block regex
#r'(?:BLK )?(?P<block>(?<=BLK )\d+)?' 
#r'((BLK|BLOCK)?\s+(?(1)(?P<block>\d+)))?\s*,?'
block = named_capture('block', r'BL(OC)?K\s+[\dA-Z]+\s*(,|\.)?')

#addition_num = r"(\d+[A-Za-z]+(,\.)?\s+)?(ADDITION|ADD'?N)" # This doesn't seem to work to match ADDN without an ordinal preceding it...
#addition_num = r"(\d+[A-Za-z]+(,\.)?\s+)?(ADDITION|ADDN)"

#addition = r"(ADDITION|ADD'?N)"
# addition = r"(ADDITION|ADD'?N)(,|\.)?"

#addition_num = ordinal_indicator + ws + r"(ADDITION|ADD'?N)"
# addition_num = ordinal_indicator + ws + r"(ADDITION|ADD'?N)(,|\.)?"
# addition_ordinal_indicator = ordinal_indicator + ws + addition

# subdivision = r'(SUBD?|SUBDIVISION)'
# subdivision_num = subdivision + ws + r'\d+'
# subdivision_ordinal_phrase = subdivision + ws + ordinal_phrase

addition_before_lot = fr'^[A-Z &]+(?:#\d+)?(?=(?: LO?TS? \d)| {x_feet_of_lot})'
addition_before_por_lot = r'^[A-Z &]+(?:#\d+)?(?= POR (?:LO?TS? )?\d)'
addition_before_por_no_labels = r'(?:[A-Z &]+(?:#\d+)?(?= POR))|(?:[A-Z ]+(?:#\d+)?(?= \d+ (?:\d+|[A-Z])))'

numeric_tract = r'^T(?:RACT )?\d+(?= (?:POR )?L(?:O?TS? )?\d)'
numeric_tract_lot = named_capture('lot', r'L\d+[A-Z]?(?: [A-Z])?(?=(?: BL)|(?: EX)|(?: LESS)|$)')
numeric_tract_lot_long = named_capture('lot', r'(?:POR )?LO?TS? \d+[A-Z]?(?: [A-Z])?(?=(?: BL)|(?: EX)|(?: LESS)|$)')

# Parent parcels may be a sign of duplicate lot, block, & plat data for properties that are actually different. Check for duplicates!
# parent_parcels = r'PARENT\s+PARCEL\s+(K\s+\d+-\d+-\d+-\d+,?\s*)+'

# corner = r'COR(\s+OF)?'

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
acres = r'(?: \d*\.\d+\s+AC(,|\.)?)?'

# Not relevant to identifying lot so can be basically ignored
mineral_rights = r'(?: (?:EX|LESS)(?: POR)?(?: \d+\/\d+)? MR)?'

# Split on some date from other PINs:
split_on = r'SPLIT(/COMBINED)?\s+ON'
split_on_date = split_on + ws + r'(' + mmddyyyy + r'|' + mmddyy + r')'

# What are these TH's?
# LOT 36, SCIO HILLS NO. 2 SUB, TH N 07-20-05 E 230.OO FT, TH S 70-17-10 E 225.30 FT, TH S 38-25-00 W 19.50 FT, TH S 07-20-05 W 165.00 FT, TH N 82-39-55 W 209.99 FT TO THE POB. PT SE 1/4 SEC 14, T2S-R5E, 1.00 AC.

NamedPattern = namedtuple('NamedPattern', 'name pattern')
NamedRegex = namedtuple('NamedRegex', 'name regex')

print(plat(addition_before_por_no_labels) + ' ' + r'(?P<lot>(?:POR )?[\d&]+)' + ' ' + r'(?P<block>(?:\d+|[A-Z]))')

patterns = [
    NamedPattern(
        'addition + lot + block no labels',
        plat(addition_before_por_no_labels) + ' ' + r'(?P<lot>(?:POR )?[\d&]+)' + ' ' + r'(?P<block>(?:\d+|[A-Z]$))'
    ),
    NamedPattern(
        'addition + lot + block',
        plat(addition_before_lot) + ' ' + lot + ' ' + block + acres + mineral_rights
    ),
    NamedPattern(
        'addition + lot (no block)',
        plat(addition_before_lot) + ' ' + lot + acres + mineral_rights
    ),
    NamedPattern(
        'addition + lot + por + block',
        plat(addition_before_lot) + ' ' + lot_plus_por + ' ' + block + acres + mineral_rights
    ),
    NamedPattern(
        'addition + por_lot simple (no block)',  # This one should go before 'addition + lot + por (no block)
        plat(addition_before_por_lot) + ' ' + lot_por_only_simple + acres + mineral_rights
    ),
    NamedPattern(
        'addition + por_lot simple + block',  # This one should go before 'addition + lot + por (no block)
        plat(addition_before_por_lot) + ' ' + lot_por_only_simple + ' ' + block + acres + mineral_rights
    ),
    NamedPattern(
        'addition + por_lot (no block)',  # This one should go before 'addition + lot + por (no block)
        plat(addition_before_por_lot) + ' ' + lot_por_only + acres + mineral_rights
    ),
    NamedPattern(
        'addition + por_lot + block',  # This one should go before 'addition + lot + por (no block)
        plat(addition_before_por_lot) + ' ' + lot_por_only + ' ' + block + acres + mineral_rights
    ),
    NamedPattern(
        'addition + lot + por (no block)',
        plat(addition_before_lot) + ' ' + lot_plus_por + acres + mineral_rights
    ),
    NamedPattern(
        'numeric tract + lot',
        plat(numeric_tract) + ' ' + numeric_tract_lot + acres + mineral_rights
    ),
    NamedPattern(
        'numeric tract + lot long',
        plat(numeric_tract) + ' ' + numeric_tract_lot_long + acres + mineral_rights
    ),
    NamedPattern(
        'numeric tract + lot long + block',
        plat(numeric_tract) + ' ' + numeric_tract_lot_long + ' ' + block + acres + mineral_rights
    ),
    NamedPattern(
        'addition + lot (no labels)',   # This one should stay at or toward the end
        plat(r'(?:(?<!POR|LOT)[A-Z #\d])+? ') + named_capture('lot', r'(?:LOT )*\d+$')
    ),
]
processing_regexes = assorting_regexes = [
    NamedRegex(
        item.name,
        re.compile(anchored_pattern(item.pattern))
    ) for item in patterns
]

def process(infile, outdir, legal_desc_field):
    parcels = gpd.read_file(infile)

    new_columns = ['lot', 'block', 'plat']
    parcels[new_columns] = ''

    for named_regex in processing_regexes:
        parcels.loc[
            parcels['lot'].isin([np.nan, '']), new_columns
        ] = parcels[legal_desc_field].str.extract(named_regex.regex)

    parcels[new_columns].map(lambda x: str(x).strip())

    outdir = Path(outdir)
    outdir.mkdir()
    parcels.to_file(outdir.joinpath(outdir.name + '.shp'))

def analyze(infile, pin_field, legal_desc_field):
    parcels = gpd.read_file(infile.name)
    print(parcels.info())

    parcels_legal_notnull = parcels[parcels[legal_desc_field].notnull()]
    print(f'{len(parcels_legal_notnull.index)=}')

    parcels_legal_lot = parcels_legal_notnull[parcels_legal_notnull[legal_desc_field].str.match(r'^LOT')]
    print(f'{len(parcels_legal_lot.index)=}')

    parcels_legal_notlot = parcels_legal_notnull[~parcels_legal_notnull[legal_desc_field].str.match(r'^LOT')]
    print(f'{len(parcels_legal_notlot.index)=}')
    print(parcels_legal_notlot[[pin_field,legal_desc_field]].head(n=100))

    parcels_lot_notnull = parcels[parcels['lot'].notnull()]
    print(f'{len(parcels_lot_notnull.index)=}')
    print(parcels_lot_notnull[[pin_field,'lot','block','plat']].head(n=100))

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

def assort(infile, pin_field, legal_desc_field):
    parcels = gpd.read_file(infile.name)

    assorted = {'unmatched': []} # 2504
    for named_regex in assorting_regexes: 
        assorted[named_regex.name] = []

    pin_legal = parcels[(parcels[legal_desc_field].notnull()) & (parcels[legal_desc_field].str.startswith('LOT'))][[pin_field,legal_desc_field]].to_dict('records')
    #for d in sorted(pin_legal, key=lambda d: d['LEGAL_DESC']):
    for d in sorted(pin_legal, key=lambda d: d[pin_field]):
        matched = False
        for named_regex in assorting_regexes:
            if named_regex.regex.match(d[legal_desc_field]):
                assorted[named_regex.name].append(d)
                matched = True
                break
        if not matched:
            assorted['unmatched'].append(d)

    for regex_name, matches in assorted.items():
        print(f"'{regex_name}': {len(matches)} matches")
        for d in matches:
            print('  ', d)

