data = [
    # 'non-numeric plat not starting with EXC'
    {
        'PIN': '08-03-32-360-004',
        'LEGAL_DESC': 'LOT 11 MARY J. RAYWALTS ADDITION.',
        'expected_extraction': {'lot': 'LOT 11', 'plat': 'MARY J. RAYWALTS ADDITION.'},
        'expected_regex_name': 'non-numeric plat not starting with EXC',
    },
    {
        'PIN': '09-09-28-413-033',
        'LEGAL_DESC': 'LOTS 40 41 42 43 44 MAP OF A TENBROOKS ADDN',
        'expected_extraction': {'lot': 'LOTS 40 41 42 43 44', 'plat': 'MAP OF A TENBROOKS ADDN'},
        'expected_regex_name': 'non-numeric plat not starting with EXC',
    },
    {
        'PIN': '08-08-05-265-001',
        'LEGAL_DESC': "LOT 3 MEYERS' SUBDIVISION.",
        'expected_extraction': {'lot': 'LOT 3', 'plat': "MEYERS' SUBDIVISION."},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': '09-08-25-214-011',
        'LEGAL_DESC': 'LOTS 166, 167, LAKEWOOD SUB',
        'expected_extraction': {'lot': 'LOTS 166, 167,', 'plat': 'LAKEWOOD SUB'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': '09-08-25-402-018',
        'LEGAL_DESC': 'LOTS 17-33 W LIBERTY HEIGHTS',
        'expected_extraction': {'lot': 'LOTS 17-33', 'plat': 'W LIBERTY HEIGHTS'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': '09-12-04-201-038',
        'LEGAL_DESC': 'LOT 17 AND LOT 16 FRISINGER INDUSTRIAL SUBDIVISION',
        'expected_extraction': {'lot': 'LOT 17 AND LOT 16', 'plat': 'FRISINGER INDUSTRIAL SUBDIVISION'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': 'H -08-22-140-002',
        'LEGAL_DESC': 'LOT-25 SCIOMEADOW COMMONS',
        'expected_extraction': {'lot': 'LOT-25', 'plat': 'SCIOMEADOW COMMONS'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': 'H -08-22-462-008',
        'LEGAL_DESC': 'LOTS 90&91 BUENA VISTA',
        'expected_extraction': {'lot': 'LOTS 90&91', 'plat': 'BUENA VISTA'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': 'H -08-25-245-002',
        'LEGAL_DESC': 'LOTS 115-136,200-226 INCL WESTOVER HILLS',
        'expected_extraction': {'lot': 'LOTS 115-136,200-226 INCL', 'plat': 'WESTOVER HILLS'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': 'K -11-02-327-044',
        'LEGAL_DESC': 'LOT 73 &74 EAST PARK SUBDIVISION.',
        'expected_extraction': {'lot': 'LOT 73 &74', 'plat': 'EAST PARK SUBDIVISION.'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': 'H -08-22-140-002',
        'LEGAL_DESC': 'LOT-25 SCIOMEADOW COMMONS',
        'expected_extraction': {'lot': 'LOT-25', 'plat': 'SCIOMEADOW COMMONS'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': '09-09-32-228-001',
        'LEGAL_DESC': 'LOTS 147 THRU 154 INCL OAK CREST SUB',
        'expected_extraction': {'lot': 'LOTS 147 THRU 154 INCL', 'plat': 'OAK CREST SUB'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': '11-11-39-130-029',
        'LEGAL_DESC': '*OLD SID - 11 11-100-035-00 YP CITY 11W-35 LOT 35 AINSWORTH PARK.',
        'expected_extraction': {'lot': 'LOT 35', 'plat': 'AINSWORTH PARK.'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': 'N -14-21-285-001',
        'LEGAL_DESC': '*OLD SID - N 14-070-011-00 FR 40-11 LOT 11 SUNRISE BEACH SUBDIVISION.',
        'expected_extraction': {'lot': 'LOT 11', 'plat': 'SUNRISE BEACH SUBDIVISION.'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': 'M -13-05-325-009',
        'LEGAL_DESC': '*OLD SID - M 13-085-017-00 LO 42-17 LOT 17 LONE OAK SUBDIVISION',
        'expected_extraction': {'lot': 'LOT 17', 'plat': 'LONE OAK SUBDIVISION'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': 'K -11-07-163-001',
        'LEGAL_DESC': 'YP 102-198 LOTS 299-300 INCL. WASHTENAW CLUBVIEW SUB.',
        'expected_extraction': {'lot': 'LOTS 299-300 INCL.', 'plat': 'WASHTENAW CLUBVIEW SUB.'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': 'K -11-07-161-010',
        'LEGAL_DESC': 'YP 102-275 LOTS 275 & 276 WASHTENAW CLUBVIEW SUB.',
        'expected_extraction': {'lot': 'LOTS 275 & 276', 'plat': 'WASHTENAW CLUBVIEW SUB.'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': 'K -11-26-475-004',
        'LEGAL_DESC': 'YP# 109-28 LOT 28 FRANK H. CLARK SUBDIVISION.',
        'expected_extraction': {'lot': 'LOT 28', 'plat': 'FRANK H. CLARK SUBDIVISION.'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },
    {
        'PIN': 'K -11-14-486-015',
        'LEGAL_DESC': 'YP#104-1064 LOT 1384 WATSONIA PARK SUBDIVISION.',
        'expected_extraction': {'lot': 'LOT 1384', 'plat': 'WATSONIA PARK SUBDIVISION.'},
        'expected_regex_name': 'non-numeric plat not starting with EXC'
    },

    # 'lot ordinal phrase & non-numeric plat not starting with EXC'
    {
        'PIN': 'K -11-29-300-031',
        'LEGAL_DESC': 'LOT #1 OAK KNOLL CONDOS',
        'expected_extraction': {'lot': 'LOT #1', 'plat': 'OAK KNOLL CONDOS'},
        'expected_regex_name': 'lot ordinal phrase & non-numeric plat not starting with EXC'
    },

    # 'alphabetic lot & non-numeric plat not starting with EXC'
    {
        'PIN': '09-09-32-105-013',
        'LEGAL_DESC': 'LOT A SCHAIRER & KEMPFS ADDN',
        'expected_extraction': {'lot': 'LOT A', 'plat': 'SCHAIRER & KEMPFS ADDN'},
        'expected_regex_name': 'alphabetic lot & non-numeric plat not starting with EXC'
    },

    # 'non-numeric plat except for subdivision ordinal phrase in the middle'
    {
        'PIN': '09-09-20-302-023',
        'LEGAL_DESC': 'LOT 53 TWIN OAKS SUBD NO 1 OF SUNSET HGTS',
        'expected_extraction': {'lot': 'LOT 53', 'plat': 'TWIN OAKS SUBD NO 1 OF SUNSET HGTS'},
        'expected_regex_name': 'non-numeric plat except for subdivision ordinal phrase in the middle',
    },

    # 'non-numeric plat up to subdivision ordinal phrase'
    {
        'PIN': 'D -04-29-232-047',
        'LEGAL_DESC': 'LOT 47, WANDERING HILLS SUB #3.',
        'expected_extraction': {'lot': 'LOT 47,', 'plat': 'WANDERING HILLS SUB #3.'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase',
    },
    {
        'PIN': 'K -11-10-386-038',
        'LEGAL_DESC': 'LOTS 206 AND 207 STURTEVANT MANOR SUBDIVISION NO. 1.',
        'expected_extraction': {'lot': 'LOTS 206 AND 207', 'plat': 'STURTEVANT MANOR SUBDIVISION NO. 1.'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase',
    },
    {
        'PIN': 'K -11-11-202-044',
        'LEGAL_DESC': 'LOT 620 & 621 DEVONSHIRE SUBDIVISION NO. 4.',
        'expected_extraction': {'lot': 'LOT 620 & 621', 'plat': 'DEVONSHIRE SUBDIVISION NO. 4.'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase',
    },
    {
        'PIN': 'K -11-11-204-018',
        'LEGAL_DESC': 'LOT 322, 323 & 324 DEVONSHIRE SUBDIVISION NO. 2.',
        'expected_extraction': {'lot': 'LOT 322, 323 & 324', 'plat': 'DEVONSHIRE SUBDIVISION NO. 2.'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase',
    },
    {
        'PIN': 'K -11-27-120-001',
        'LEGAL_DESC': 'LOT 1 WHISPERING MEADOWS SUBDIVISION  NO. 1,',
        'expected_extraction': {'lot': 'LOT 1', 'plat': 'WHISPERING MEADOWS SUBDIVISION  NO. 1,'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase',
    },
    {
        'PIN': 'K -11-27-124-148',
        'LEGAL_DESC': 'LOT 148 WHISPERING MEADOWS SUBDIVISION NO. 2,',
        'expected_extraction': {'lot': 'LOT 148', 'plat': 'WHISPERING MEADOWS SUBDIVISION NO. 2,'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase',
    },
    {
        'PIN': 'K -11-40-350-042',
        'LEGAL_DESC': 'LOT 485 AND 490 WASHTENAW CLUB VIEW SUBDIVISION NO 1.',
        'expected_extraction': {'lot': 'LOT 485 AND 490', 'plat': 'WASHTENAW CLUB VIEW SUBDIVISION NO 1.'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase',
    },
    {
        'PIN': '09-08-24-400-013',
        'LEGAL_DESC': 'LOT 301 SCIOTO HILLS SUB NO. 1',
        'expected_extraction': {'lot': 'LOT 301', 'plat': 'SCIOTO HILLS SUB NO. 1'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase'
    },
    {
        'PIN': '09-09-14-202-008',
        'LEGAL_DESC': 'LOT 131 FOREST HILLS SUBDIVISION NO 2',
        'expected_extraction': {'lot': 'LOT 131', 'plat': 'FOREST HILLS SUBDIVISION NO 2'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase'
    },
    {
        'PIN': '09-09-27-301-071',
        'LEGAL_DESC': 'LOT 77 HILLWOOD SUB #5',
        'expected_extraction': {'lot': 'LOT 77', 'plat': 'HILLWOOD SUB #5'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase'
    },
    {
        'PIN': '09-12-10-106-019',
        'LEGAL_DESC': 'LOT 151 152 & 153 SPRINGWATER SUB NO 2',
        'expected_extraction': {'lot': 'LOT 151 152 & 153', 'plat': 'SPRINGWATER SUB NO 2'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase'
    },
    {
        'PIN': 'K -11-11-281-050',
        'LEGAL_DESC': 'LOT 525 - 527 DEVONSHIRE SUB #4',
        'expected_extraction': {'lot': 'LOT 525 - 527', 'plat': 'DEVONSHIRE SUB #4'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase'
    },
    {
        'PIN': 'K -11-11-282-050',
        'LEGAL_DESC': 'LOTS 668 & 669 DEVONSHIRE SUBDIVISION #4',
        'expected_extraction': {'lot': 'LOTS 668 & 669', 'plat': 'DEVONSHIRE SUBDIVISION #4'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase'
    },
    {
        'PIN': 'K -11-11-461-034',
        'LEGAL_DESC': 'LOTS 374 - 375 SOUTH DEVONSHIRE SUBDIVISION NO. 2',
        'expected_extraction': {'lot': 'LOTS 374 - 375', 'plat': 'SOUTH DEVONSHIRE SUBDIVISION NO. 2'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase'
    },
    {
        'PIN': 'K -11-33-215-049',
        'LEGAL_DESC': 'LOT 49 STREAMWOOD SUB #1',
        'expected_extraction': {'lot': 'LOT 49', 'plat': 'STREAMWOOD SUB #1'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase'
    },
    {
        'PIN': 'K -11-33-245-102',
        'LEGAL_DESC': 'LOT 102 STREAMWOOD SUBDIVISIONNO. 2',
        'expected_extraction': {'lot': 'LOT 102', 'plat': 'STREAMWOOD SUBDIVISIONNO. 2'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase'
    },
    {
        'PIN': 'K -11-33-286-556',
        'LEGAL_DESC': 'LOT 556 STREAMWOOD SUB # 8',
        'expected_extraction': {'lot': 'LOT 556', 'plat': 'STREAMWOOD SUB # 8'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase'
    },
    {
        'PIN': 'K -11-33-321-770',
        'LEGAL_DESC': 'LOT  770 GREENE FARMS SUB # 7',
        'expected_extraction': {'lot': 'LOT  770', 'plat': 'GREENE FARMS SUB # 7'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase'
    },
    {
        'PIN': 'K -11-33-411-509',
        'LEGAL_DESC': 'LOT 509  GREENE FARMS SUB #6',
        'expected_extraction': {'lot': 'LOT 509', 'plat': 'GREENE FARMS SUB #6'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase'
    },
    {
        'PIN': 'K -11-33-415-633',
        'LEGAL_DESC': 'LOTS 633, 634 AND 635 GREENE FARMS SUB #6',
        'expected_extraction': {'lot': 'LOTS 633, 634 AND 635', 'plat': 'GREENE FARMS SUB #6'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase'
    },

    # 'non-numeric plat up to subdivision #'
    {
        'PIN': 'K -11-33-274-393',
        'LEGAL_DESC': 'LOT 393 STREAMWOOD SUB 7',
        'expected_extraction': {'lot': 'LOT 393', 'plat': 'STREAMWOOD SUB 7'},
        'expected_regex_name': 'non-numeric plat up to subdivision #'
    },

    # 'non-numeric plat except for subdivision ordinal phrase in the middle'
    {
        'PIN': '09-09-20-302-023',
        'LEGAL_DESC': 'LOT 53 TWIN OAKS SUBD NO 1 OF SUNSET HGTS',
        'expected_extraction': {'lot': 'LOT 53', 'plat': 'TWIN OAKS SUBD NO 1 OF SUNSET HGTS'},
        'expected_regex_name': 'non-numeric plat except for subdivision ordinal phrase in the middle'
    },

    # 'non-numeric plat up to addition ordinal indicator'
    {
        'PIN': '08-03-31-475-003',
        'LEGAL_DESC': "LOTS 32 & 33 MARY J. RAYWALT'S 2D ADDITION.",
        'expected_extraction': {'lot': 'LOTS 32 & 33', 'plat': "MARY J. RAYWALT'S 2D ADDITION."},
        'expected_regex_name': 'non-numeric plat up to addition ordinal indicator',
    },
    {
        'PIN': '08-03-31-475-004',
        'LEGAL_DESC': "LOT 34 MARY J. RAYWALT'S 2D ADDITION.",
        'expected_extraction': {'lot': 'LOT 34', 'plat': "MARY J. RAYWALT'S 2D ADDITION."},
        'expected_regex_name': 'non-numeric plat up to addition ordinal indicator',
    },

    # 'alphabetic lot & non-numeric plat up to addition ordinal indicator'
    {
        'PIN': '09-09-29-310-022',
        'LEGAL_DESC': 'LOT AA WILLIAM S MAYNRDS 3RD ADDITION',
        'expected_extraction': {'lot': 'LOT AA', 'plat': 'WILLIAM S MAYNRDS 3RD ADDITION'},
        'expected_regex_name': 'alphabetic lot & non-numeric plat up to addition ordinal indicator',
    },
    {
        'PIN': '09-09-29-310-029',
        'LEGAL_DESC': 'LOT U WILLIAM S MAYNARDS 3RD ADDN',
        'expected_extraction': {'lot': 'LOT U', 'plat': 'WILLIAM S MAYNARDS 3RD ADDN'},
        'expected_regex_name': 'alphabetic lot & non-numeric plat up to addition ordinal indicator',
    },

    # 'block & non-numeric plat up to addition ordinal indicator'
    {
        'PIN': '09-09-20-406-001',
        'LEGAL_DESC': 'LOT 1 BLK 3 MAP OF DANIEL HISCOCKS 2ND ADDN',
        'expected_extraction': {'lot': 'LOT 1', 'block': 'BLK 3', 'plat': 'MAP OF DANIEL HISCOCKS 2ND ADDN'},
        'expected_regex_name': 'block & non-numeric plat up to addition ordinal indicator',
    },

    # 'non-numeric plat up to ordinal phrase'
    {
        'PIN': '09-08-24-100-008',
        'LEGAL_DESC': 'LOT 102 HOLLYWOOD PARK NO 2',
        'expected_extraction': {'lot': 'LOT 102', 'plat': 'HOLLYWOOD PARK NO 2'},
        'expected_regex_name': 'non-numeric plat up to ordinal phrase',
    },
    {
        'PIN': '09-08-24-104-036',
        'LEGAL_DESC': 'LOT 88 HOLLYWOOD PARK NO. 2',
        'expected_extraction': {'lot': 'LOT 88', 'plat': 'HOLLYWOOD PARK NO. 2'},
        'expected_regex_name': 'non-numeric plat up to ordinal phrase',
    },
    {
        'PIN': '09-08-24-400-001',
        'LEGAL_DESC': 'LOTS 269,270,298,&299 SCIOTO HILLS NO 1',
        'expected_extraction': {'lot': 'LOTS 269,270,298,&299', 'plat': 'SCIOTO HILLS NO 1'},
        'expected_regex_name': 'non-numeric plat up to ordinal phrase',
    },
    {
        'PIN': '09-08-24-401-013',
        'LEGAL_DESC': 'LOTS 217 & 218 SCIOTO HILLS NO. 1',
        'expected_extraction': {'lot': 'LOTS 217 & 218', 'plat': 'SCIOTO HILLS NO. 1'},
        'expected_regex_name': 'non-numeric plat up to ordinal phrase',
    },
    {
        'PIN': '09-08-24-401-014',
        'LEGAL_DESC': 'LOT 230 & 231 SCIOTO HILLS NO. 1',
        'expected_extraction': {'lot': 'LOT 230 & 231', 'plat': 'SCIOTO HILLS NO. 1'},
        'expected_regex_name': 'non-numeric plat up to ordinal phrase',
    },
    {
        'PIN': 'K -11-14-333-022',
        'LEGAL_DESC': 'YP# 122-95 LOT 344 NANCY PARK NUMBER 6.',
        'expected_extraction': {'lot': 'LOT 344', 'plat': 'NANCY PARK NUMBER 6.'},
        'expected_regex_name': 'non-numeric plat up to ordinal phrase'
    },

    # non-numeric plat up to ordinal phrase, followed by split on date
    {
        'PIN': '09-09-15-406-034',
        'LEGAL_DESC': 'LOTS 185 & 186 NORTH CAMPUS HEIGHTS NO 4 SPLIT ON 05/10/2001 FROM 09-09-15-406-031 AND 09-09-15-406-030;',
        'expected_extraction': {'lot': 'LOTS 185 & 186', 'plat': 'NORTH CAMPUS HEIGHTS NO 4'},
        'expected_regex_name': 'non-numeric plat up to ordinal phrase, followed by split on date',
    },
    {
        'PIN': '09-09-19-212-040',
        'LEGAL_DESC': 'LOT 128 GARDEN HOMES PARK SUBDIVISION ALSO PARK NO. 2 SPLIT/COMBINED ON 05/17/2018 FROM 09-09-19-212-022, 09-09-19-212-021;',
        'expected_extraction': {'lot': 'LOT 128', 'plat': 'GARDEN HOMES PARK SUBDIVISION ALSO PARK NO. 2'},
        'expected_regex_name': 'non-numeric plat up to ordinal phrase, followed by split on date',
    },

    {
        'PIN': 'K -11-27-120-002',
        'LEGAL_DESC': 'LOT 2 WHISPERING MEADOWS SUBDIVISION NO. 1,  PARENT PARCEL K 11-27-100-021, K 11-27-100-003, K 11-27-100-007',
        'expected_extraction': {'lot': 'LOT 2', 'plat': 'WHISPERING MEADOWS SUBDIVISION NO. 1,'},
        'expected_regex_name': 'non-numeric plat up to subdivision, followed by parent parcels'
    },
    {
        'PIN': 'K -11-27-120-008',
        'LEGAL_DESC': 'LOT 8 WHISPERING MEADOWS SUBDIVISION NO. 1,  PARENT PARCEL K 11-27-100-021',
        'expected_extraction': {'lot': 'LOT 8', 'plat': 'WHISPERING MEADOWS SUBDIVISION NO. 1,'},
        'expected_regex_name': 'non-numeric plat up to subdivision, followed by parent parcels'
    },
    {
        'PIN': 'K -11-27-121-017',
        'LEGAL_DESC': 'LOT 17 WHISPERING MEADOWS SUBDIVISION NO . 1,  PARENT PARCEL K 11-27-100-021, K 11-27-100-003, K 11-27-100-007',
        'expected_extraction': {'lot': 'LOT 17', 'plat': 'WHISPERING MEADOWS SUBDIVISION NO . 1,'},
        'expected_regex_name': 'non-numeric plat up to subdivision, followed by parent parcels'
    },
    {
        'PIN': 'K -11-27-121-020',
        'LEGAL_DESC': 'LOT20 WHISPERING MEADOWS SUBDIVISION NO. 1,  PARENT PARCEL K 11-27-100-021, K 11-27-100-003, K 11-27-100-007',
        'expected_extraction': {'lot': 'LOT20', 'plat': 'WHISPERING MEADOWS SUBDIVISION NO. 1,'},
        'expected_regex_name': 'non-numeric plat up to subdivision, followed by parent parcels'
    },
    {
        'PIN': 'K -11-27-122-042',
        'LEGAL_DESC': 'LOT42 WHISPERING MEADOWS SUBDIVISION NO.1, PARENT PARCEL K 11-27-100-021, K 11-27-100-003, K 11-27-100-007',
        'expected_extraction': {'lot': 'LOT42', 'plat': 'WHISPERING MEADOWS SUBDIVISION NO.1,'},
        'expected_regex_name': 'non-numeric plat up to subdivision, followed by parent parcels'
    },
    {
        'PIN': 'K -11-27-125-100',
        'LEGAL_DESC': 'LOT 100 WHISPERING MEADOWS SUBDIVISION NO. 1 , PARENT PARCEL K 11-27-100-021, K 11-27-100-003, K 11-27-100-007',
        'expected_extraction': {'lot': 'LOT 100', 'plat': 'WHISPERING MEADOWS SUBDIVISION NO. 1 ,'},
        'expected_regex_name': 'non-numeric plat up to subdivision, followed by parent parcels'
    },

    {
        'PIN': '08-08-07-125-030',
        'LEGAL_DESC': 'LOT 30, DEXTER BUS & RES PARK NO. 2. PT NE 1/4 SEC 7, T2S-R5E, 2.20 AC.',
        'expected_extraction': {'lot': 'LOT 30,', 'plat': 'DEXTER BUS & RES PARK NO. 2.'},
        'expected_regex_name': 'non-numeric plat up to digits and non-alpha chars, followed by part of TWS & acres'
    },
    {
        # Probably lot should = 'LOT 40 OF', but not sure it's worth the effort to parse it that way...
        'PIN': '08-08-07-125-040',
        'LEGAL_DESC': 'LOT 40 OF DEXTER BUSINESS & RESEARCH PARK #2. PT NE 1/4 SEC 7, T2S-R5E, 1.60 AC.',
        'expected_extraction': {'lot': 'LOT 40', 'plat': 'OF DEXTER BUSINESS & RESEARCH PARK #2.'},
        'expected_regex_name': 'non-numeric plat up to digits and non-alpha chars, followed by part of TWS & acres'
    },

    # 'non-numeric plat up to subdivision ordinal phrase, followed by part of TWS'
    {
        'PIN': 'K -11-33-304-412',
        'LEGAL_DESC': 'LOT 412 GREENE FARMS SUB NO 5 PART OF THE SW 1/4 SECTION 33 T3S R7E',
        'expected_extraction': {'lot': 'LOT 412', 'plat': 'GREENE FARMS SUB NO 5'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase, followed by part of TWS'
    },
    {
        'PIN': 'K -11-33-305-399',
        'LEGAL_DESC': 'LOT 399 GREENE FARMS SUB NO.5 PART OF THE SW 1/4 SECTION 33 T3S R7E',
        'expected_extraction': {'lot': 'LOT 399', 'plat': 'GREENE FARMS SUB NO.5'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase, followed by part of TWS'
    },
    {
        'PIN': 'K -11-33-306-379',
        'LEGAL_DESC': 'LOT 379 GREENE FARMS SUB NO. 5 PART OF THE SW 1/4 SECT 33 T3S R7E',
        'expected_extraction': {'lot': 'LOT 379', 'plat': 'GREENE FARMS SUB NO. 5'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase, followed by part of TWS'
    },
    {
        'PIN': 'K -11-33-312-466',
        'LEGAL_DESC': 'LOT 466  GREENE FARMS SUB NO 5 PART OF THE SW 1/4 SECTION 33 T3S R7E',
        'expected_extraction': {'lot': 'LOT 466', 'plat': 'GREENE FARMS SUB NO 5'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase, followed by part of TWS'
    },
    {
        'PIN': 'K -11-33-313-481',
        'LEGAL_DESC': 'LOT481 GREENE FARMS SUB NO.5 PART OF THE SW 1/4 SECTION 33 T3S R7E',
        'expected_extraction': {'lot': 'LOT481', 'plat': 'GREENE FARMS SUB NO.5'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase, followed by part of TWS'
    },
    {
        'PIN': 'K -11-33-315-490',
        'LEGAL_DESC': 'LOT 490 GREENE FARMS SUB NO. 5 PART OF THE SW 1/4 SECTION 33  T3S R7E',
        'expected_extraction': {'lot': 'LOT 490', 'plat': 'GREENE FARMS SUB NO. 5'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase, followed by part of TWS'
    },

    # 'non-numeric plat up to subdivision ordinal phrase, followed by part of TWS with multiple directional fractions, liber, pages, and date' 
    {
        'PIN': 'K -11-33-407-076',
        'LEGAL_DESC': 'LOT 76 GREENE FARMS SUB NO. 2 PART OF SW 1/4 AND SE 1/4 SEC 33, T3S-R7E LIBER 00 OF PLATS, PAGES 00-00 00/00/99',
        'expected_extraction': {'lot': 'LOT 76', 'plat': 'GREENE FARMS SUB NO. 2'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase, followed by part of TWS with multiple directional fractions, liber, pages, and date'
    },

    # 'non-numeric plat up to subdivision ordinal phrase, followed by TWS, liber, pages, and date'
    {
        'PIN': 'K -11-33-401-001',
        'LEGAL_DESC': 'LOT 1 GREENE FARMS SUB NO. 1 SE 1/4 SEC 33, T3S-R7E LIBER 31 OF PLATS, PAGES 71-76 03/10/99',
        'expected_extraction': {'lot': 'LOT 1', 'plat': 'GREENE FARMS SUB NO. 1'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase, followed by TWS, liber, pages, and date'
    },

    # non-numeric plat, followed by as-recorded-in-liber
    {
        'PIN': '09-08-24-301-036',
        'LEGAL_DESC': 'LOT 12, DEXTER AVENUE HILLS SUBDIVISION, AS RECORDED IN LIBER 6 OF PLATS, PAGE 49, WASHTENAW COUNTY RECORDS, MICHIGAN',
        'expected_extraction': {'lot': 'LOT 12,', 'plat': 'DEXTER AVENUE HILLS SUBDIVISION,'},
        'expected_regex_name': 'non-numeric plat, followed by as-recorded-in-liber'
    },
    {
        'PIN': '09-08-24-421-029',
        'LEGAL_DESC': 'LOT 242 SCIOTO HILLS NUMBER ONE AS RECORDED IN LIBER 8 OF PLATS, PAGE 30, WASHTENAW COUNTY RECORDS',
        'expected_extraction': {'lot': 'LOT 242', 'plat': 'SCIOTO HILLS NUMBER ONE'},
        'expected_regex_name': 'non-numeric plat, followed by as-recorded-in-liber'
    },

    # 'non-numeric plat up to digits and non-alpha chars, followed by part of TWS'
    {
        'PIN': 'H -08-15-452-006',
        'LEGAL_DESC': 'LOT 35 FARMCREST NO 2. PT SE 1/4 SEC 15, T2S-R5E.',
        'expected_extraction': {'lot': 'LOT 35', 'plat': 'FARMCREST NO 2.'},
        'expected_regex_name': 'non-numeric plat up to digits and non-alpha chars, followed by part of TWS'
    },
    {
        'PIN': 'H -08-15-452-009',
        'LEGAL_DESC': 'LOT 32 FARMCREST NUMBER 2. PART OF SE 1/4 SEC 15, T2S-R5E.',
        'expected_extraction': {'lot': 'LOT 32', 'plat': 'FARMCREST NUMBER 2.'},
        'expected_regex_name': 'non-numeric plat up to digits and non-alpha chars, followed by part of TWS'
    },
    {
        'PIN': 'H -08-23-115-005',
        'LEGAL_DESC': "LOT 31 SUPERVISOR'S PLAT NO. 2. PART OF NE 1/4 SEC 23, T2S-R5E.",
        'expected_extraction': {'lot': 'LOT 31', 'plat': "SUPERVISOR'S PLAT NO. 2."},
        'expected_regex_name': 'non-numeric plat up to digits and non-alpha chars, followed by part of TWS'
    },
    {
        'PIN': 'H -08-36-435-001',
        'LEGAL_DESC': 'LOT 1, THE RAVINES NO 1,  PT SE 1/4 SEC 36, T2S-R5E.',
        'expected_extraction': {'lot': 'LOT 1,', 'plat': 'THE RAVINES NO 1,'},
        'expected_regex_name': 'non-numeric plat up to digits and non-alpha chars, followed by part of TWS'
    }, 
    {
        'PIN': 'H -08-36-435-040',
        'LEGAL_DESC': 'LOT 40,THE RAVINES NO 1,  PT SE 1/4 SEC 36, T2S-R5E.',
        'expected_extraction': {'lot': 'LOT 40,', 'plat': 'THE RAVINES NO 1,'},
        'expected_regex_name': 'non-numeric plat up to digits and non-alpha chars, followed by part of TWS'
    },
    {
        'PIN': 'M -13-24-340-021',
        'LEGAL_DESC': '*OLD SID - M 13-080-016-00 LO 41-16 LOT 68 LODI COUNTRY ESTATES NO. 3 PART OF SW 1/4, SEC. 24 T3S-R5E',
        'expected_extraction': {'lot': 'LOT 68', 'plat': 'LODI COUNTRY ESTATES NO. 3'},
        'expected_regex_name': 'non-numeric plat up to digits and non-alpha chars, followed by part of TWS'
    },


    {
        'PIN': '08-08-07-125-001',
        'LEGAL_DESC': 'LOTS 1, 2, 3, & 16 DEXTER BUSINESS AND RESEARCH PARK. PT NW 1/4 SEC 8, T2S-R5E, 9.80 AC.',
        'expected_extraction': {'lot': 'LOTS 1, 2, 3, & 16', 'plat': 'DEXTER BUSINESS AND RESEARCH PARK.'},
        'expected_regex_name': 'non-numeric plat followed by part of TWS & acres',
    },
    {
        'PIN': 'H -08-35-215-002',
        'LEGAL_DESC': 'LOT 2 SAGINAW HILLS SUB PT NW 1/4 SEC 35 T2S R5E 3.41 AC',
        'expected_extraction': {'lot': 'LOT 2', 'plat': 'SAGINAW HILLS SUB'},
        'expected_regex_name': 'non-numeric plat followed by part of TWS & acres',
    },

    # 'block & non-numeric plat followed by part of TWS & acres' 
    {
        'PIN': '08-08-05-235-002',
        'LEGAL_DESC': 'LOTS 3 & 4 BLK 30 ORIGINAL PLAT, VILLAGE OF DEXTER. PT NW 1/4, SEC 5, T2S-R5E, 0.90 AC.',
        'expected_extraction': {'lot': 'LOTS 3 & 4', 'block': 'BLK 30', 'plat': 'ORIGINAL PLAT, VILLAGE OF DEXTER.'},
        'expected_regex_name': 'block & non-numeric plat followed by part of TWS & acres',
    },
    {
        'PIN': '08-08-06-110-014',
        'LEGAL_DESC': 'LOT 2, BLK 10 ORIGINAL PLAT, VILLAGE OF DEXTER. PT NE 1/4 SEC 6, T2S-R5E, 0.045 AC.',
        'expected_extraction': {'lot': 'LOT 2,', 'block': 'BLK 10', 'plat': 'ORIGINAL PLAT, VILLAGE OF DEXTER.'},
        'expected_regex_name': 'block & non-numeric plat followed by part of TWS & acres',
    },
    {
        'PIN': '08-08-06-153-026',
        'LEGAL_DESC': 'LOT 14, BLK 20, ORIGINAL PLAT, VILLAGE OF DEXTER. PT NE 1/4 SEC 6, T2S-R5E, 0.45 AC.',
        'expected_extraction': {'lot': 'LOT 14,', 'block': 'BLK 20,', 'plat': 'ORIGINAL PLAT, VILLAGE OF DEXTER.'},
        'expected_regex_name': 'block & non-numeric plat followed by part of TWS & acres',
    },
    {
        'PIN': '08-08-06-408-013',
        'LEGAL_DESC': 'LOTS 6 & 7, BLK 37, PLAT OF ADDN TO VILLAGE OF DEXTER BY DEXTER ESTATE. PT SE 1/4 SEC 6, T2S-R5E, 0.65 AC.',
        'expected_extraction': {'lot': 'LOTS 6 & 7,', 'block': 'BLK 37,', 'plat': 'PLAT OF ADDN TO VILLAGE OF DEXTER BY DEXTER ESTATE.'},
        'expected_regex_name': 'block & non-numeric plat followed by part of TWS & acres',
    },

    # 'block & non-numeric plat followed by part of TWS'
    {
        'PIN': '08-08-05-230-007',
        'LEGAL_DESC': 'LOTS 5-8, INC, BLK 12, ORIGINAL PLAT, VILLAGE OF DEXTER. PT NW 1/4 SEC 5, T2S-R5E.',
        'expected_extraction': {'lot': 'LOTS 5-8, INC,', 'block': 'BLK 12,', 'plat': 'ORIGINAL PLAT, VILLAGE OF DEXTER.'},
        'expected_regex_name': 'block & non-numeric plat followed by part of TWS',
    },

    {
        'PIN': '08-03-32-365-007',
        'LEGAL_DESC': "LOT 6, MARY J. RAYWALT'S ADDN TO DEXTER VILLAGE. PT SE 1/4 SEC 31, T1S-R5E.",
        'expected_extraction': {'lot': 'LOT 6,', 'plat': "MARY J. RAYWALT'S ADDN TO DEXTER VILLAGE."},
        'expected_regex_name': 'non-numeric plat followed by part of TWS',
    },
    {
        'PIN': 'H -08-03-479-005',
        'LEGAL_DESC': 'LOT 13, LOCH ALPINE. PART OF SE 1/4 SEC 3, T2S-R5E.',
        'expected_extraction': {'lot': 'LOT 13,', 'plat': 'LOCH ALPINE.'},
        'expected_regex_name': 'non-numeric plat followed by part of TWS',
    },

    # 'non-numeric plat with addition ordinal indicator in the middle, followed by part of TWS' 
    {
        'PIN': '08-03-31-475-005',
        'LEGAL_DESC': "LOT 35 MARY J RAYWALT'S 2ND ADDN, VILLAGE OF DEXTER, PT SE 1/4 SEC 31, T1S-R5E.",
        'expected_extraction': {'lot': 'LOT 35', 'plat': "MARY J RAYWALT'S 2ND ADDN, VILLAGE OF DEXTER,"},
        'expected_regex_name': 'non-numeric plat with addition ordinal indicator in the middle, followed by part of TWS',
    },
    
    # 'non-numeric plat followed by part of TWS followed by non-numeric string' 
    {
        'PIN': '08-03-32-360-003',
        'LEGAL_DESC': "LOT 10 MARY J RAYWALT'S ADD'N TO THE VILLAGE OF DEXTER. PT SW 1/4 SEC 32, T1S-R5E (SCIO TWP).",
        'expected_extraction': {'lot': 'LOT 10', 'plat': "MARY J RAYWALT'S ADD'N TO THE VILLAGE OF DEXTER."},
        'expected_regex_name': 'non-numeric plat followed by part of TWS followed by non-numeric string',
    },
    {
        'PIN': '08-08-08-260-001',
        'LEGAL_DESC': 'LOT 1, DEXTER CROSSING PLAT ONE SUBD. PT NW 1/4 SEC 8, T2S-R5E, DEXTER VILLAGE.',
        'expected_extraction': {'lot': 'LOT 1,', 'plat': 'DEXTER CROSSING PLAT ONE SUBD.'},
        'expected_regex_name': 'non-numeric plat followed by part of TWS followed by non-numeric string',
    },

    # non-numeric plat up to ordinal phrase, followed by part of TWS followed by non-numeric string'
    {
        'PIN': '08-08-08-260-104',
        'LEGAL_DESC': 'LOT 104, DEXTER CROSSING, WASHTENAW CO CONDO SUBDV PLAN NO. 293.  PT N 1/4 COR OF SEC 8, T2S-R5E. VILLAGE OF DEXTER.  AC.',
        'expected_extraction': {'lot': 'LOT 104,', 'plat': 'DEXTER CROSSING, WASHTENAW CO CONDO SUBDV PLAN NO. 293.'},
        'expected_regex_name': 'non-numeric plat up to ordinal phrase, followed by part of TWS followed by non-numeric string',
    },

    # block & non-numeric plat
    {
        'PIN': '08-03-31-476-001',
        'LEGAL_DESC': 'LOT 1 BLK 2 ORIGINAL PLAT',
        'expected_extraction': {'lot': 'LOT 1', 'block': 'BLK 2', 'plat': "ORIGINAL PLAT"},
        'expected_regex_name': 'block & non-numeric plat'
    },
    {
        'PIN': '08-08-05-250-001',
        'LEGAL_DESC': 'LOTS 11 & 12, BLK 31 PLAT OF THE ADDITION TO THE VILLAGE OF DEXTER BY THE DEXTER ESTATES.',
        'expected_extraction': {'lot': 'LOTS 11 & 12,', 'block': 'BLK 31', 'plat': 'PLAT OF THE ADDITION TO THE VILLAGE OF DEXTER BY THE DEXTER ESTATES.'},
        'expected_regex_name': 'block & non-numeric plat'
    },
    {
        'PIN': '08-08-05-250-002',
        'LEGAL_DESC': 'LOT 10, BLK 31 PLAT OF THE ADDITION TO THE VILLAGE OF DEXTER BY THE DEXTER ESTATES.',
        'expected_extraction': {'lot': 'LOT 10,', 'block': 'BLK 31', 'plat': 'PLAT OF THE ADDITION TO THE VILLAGE OF DEXTER BY THE DEXTER ESTATES.'},
        'expected_regex_name': 'block & non-numeric plat'
    },
    {
        'PIN': '08-03-31-476-002',
        'LEGAL_DESC': 'LOT 2 BLK 2 ORIGINAL PLAT.',
        'expected_extraction': {'lot': 'LOT 2', 'block': 'BLK 2', 'plat': "ORIGINAL PLAT."},
        'expected_regex_name': 'block & non-numeric plat'
    },
    {
        'PIN': '08-08-05-235-001',
        'LEGAL_DESC': 'LOTS 1 & 2 BLK 30 ORIGINAL PLAT.',
        'expected_extraction': {'lot': 'LOTS 1 & 2', 'block': 'BLK 30', 'plat': 'ORIGINAL PLAT.'},
        'expected_regex_name': 'block & non-numeric plat'
    },
    {
        'PIN': '08-08-06-109-001',
        'LEGAL_DESC': 'LOTS 1, 2, 3 & 4 BLK 14 ORIGINAL PLAT.',
        'expected_extraction': {'lot': 'LOTS 1, 2, 3 & 4', 'block': 'BLK 14', 'plat': 'ORIGINAL PLAT.'},
        'expected_regex_name': 'block & non-numeric plat'
    },
    {
        'PIN': '08-08-06-111-004',
        'LEGAL_DESC': 'LOT 4, BLK 13, ORIGINAL PLAT, VILLAGE OF DEXTER.',
        'expected_extraction': {'lot': 'LOT 4,', 'block': 'BLK 13,', 'plat': "ORIGINAL PLAT, VILLAGE OF DEXTER."},
        'expected_regex_name': 'block & non-numeric plat'
    },
    {
        'PIN': '09-09-21-209-017',
        'LEGAL_DESC': 'LOT 16 BLOCK 4 PATRIDGE ADDITION',
        'expected_extraction': {'lot': 'LOT 16', 'block': 'BLOCK 4', 'plat': 'PATRIDGE ADDITION'},
        'expected_regex_name': 'block & non-numeric plat'
    },
    {
        'PIN': '09-09-21-209-006',
        'LEGAL_DESC': 'LOTS 10 THRU 15 INCL BLK 4 PATRIDGE ADDITION',
        'expected_extraction': {'lot': 'LOTS 10 THRU 15 INCL', 'block': 'BLK 4', 'plat': 'PATRIDGE ADDITION'},
        'expected_regex_name': 'block & non-numeric plat'
    },

    # 'block & non-numeric plat up to digits, maybe followed by punctuation'
    {
        'PIN': '09-09-29-208-010',
        'LEGAL_DESC': 'LOT 11 BLOCK 4 ASSESSORS PLAT NO 3',
        'expected_extraction': {'lot': 'LOT 11', 'block': 'BLOCK 4', 'plat': 'ASSESSORS PLAT NO 3'},
        'expected_regex_name': 'block & non-numeric plat up to digits, maybe followed by punctuation'
    },
    {
        'PIN': '09-09-29-208-011',
        'LEGAL_DESC': 'LOT 12 BLK 4 ASSESSORS PLAT NO 3',
        'expected_extraction': {'lot': 'LOT 12', 'block': 'BLK 4', 'plat': 'ASSESSORS PLAT NO 3'},
        'expected_regex_name': 'block & non-numeric plat up to digits, maybe followed by punctuation'
    },
    {
        'PIN': '09-09-29-211-002',
        'LEGAL_DESC': 'LOTS 3 AND 4 BLK 2 ASSESSORS PLAT NO 3',
        'expected_extraction': {'lot': 'LOTS 3 AND 4', 'block': 'BLK 2', 'plat': 'ASSESSORS PLAT NO 3'},
        'expected_regex_name': 'block & non-numeric plat up to digits, maybe followed by punctuation'
    },
    {
        'PIN': '09-09-29-213-012',
        'LEGAL_DESC': 'LOTS 3 4 AND 5 BLK 1 ASSESSORS PLAT NO 3',
        'expected_extraction': {'lot': 'LOTS 3 4 AND 5', 'block': 'BLK 1', 'plat': 'ASSESSORS PLAT NO 3'},
        'expected_regex_name': 'block & non-numeric plat up to digits, maybe followed by punctuation'
    },

#    { # We need a block_alpha pattern for this one.
#        'PIN': '09-09-28-200-054', 'LEGAL_DESC': 'LOT 1 BLOCK B EASTERN ADDITION', 'expected_regex_name': 6,
#        'expected_extraction': {'lot': 'LOT 1', 'block': 'B', 'plat': 'EASTERN ADDITION'},
#    },
#    { # This one should probably not match! Probably impossible to know what the EXC... means.
#        'PIN': '09-09-28-410-009', 'LEGAL_DESC': 'LOTS 15 & 20 EXC PORTION TAKEN FOR OBSERVATORY C T WILMOTS ADDN', 'expected_regex_name': 6,
#        'expected_extraction': {'lot': 'LOTS 15 & 20', 'plat': 'EXC PORTION TAKEN FOR OBSERVATORY C T WILMOTS ADDN'},
#    },

    # township range & non-numeric plat up to addition ordinal indicator
    {
        'PIN': '09-09-29-329-004',
        'LEGAL_DESC': "LOT 3, B6S, R1W, WILLIAM S. MAYNARD'S 2ND ADDITION",
        'expected_extraction': {'lot': 'LOT 3,', 'plat': "WILLIAM S. MAYNARD'S 2ND ADDITION"},
        'expected_regex_name': 'township range & non-numeric plat up to addition ordinal indicator',
    },

    # township & non-numeric plat up to addition ordinal indicator
    {
        'PIN': '09-09-29-332-001',
        'LEGAL_DESC': 'LOT 5 B7S WILLIAM S MAYNARDS 2ND ADDITION',
        'expected_extraction': {'lot': 'LOT 5', 'plat': 'WILLIAM S MAYNARDS 2ND ADDITION'},
        'expected_regex_name': 'township & non-numeric plat up to addition ordinal indicator',
    },

    # township range & non-numeric plat up to addition
    {
        'PIN': '09-09-28-200-002',
        'LEGAL_DESC': 'LOT 6 B5N R10E LAWRENCE & MAYNARDS ADDITION',
        'expected_extraction': {'lot': 'LOT 6', 'plat': 'LAWRENCE & MAYNARDS ADDITION'},
        'expected_regex_name': 'township range & non-numeric plat up to addition',
    },
    {
        'PIN': '09-09-29-319-018',
        'LEGAL_DESC': 'LOT 5 B5S, R2W WILLIAM S MAYNARDS ADDITION',
        'expected_extraction': {'lot': 'LOT 5', 'plat': 'WILLIAM S MAYNARDS ADDITION'},
        'expected_regex_name': 'township range & non-numeric plat up to addition',
    },
    {
        'PIN': '09-09-29-424-001',
        'LEGAL_DESC': 'LOTS 3 THRU 11 B4S R8E ANN ARBOR LAND COMPANYS ADDITION',
        'expected_extraction': {'lot': 'LOTS 3 THRU 11', 'plat': 'ANN ARBOR LAND COMPANYS ADDITION'},
        'expected_regex_name': 'township range & non-numeric plat up to addition',
    },

    # township range & non-numeric plat
    {
        'PIN': '09-09-29-112-006',
        'LEGAL_DESC': 'LOT 6 B2S R6E ORIGINAL PLAT OF ANN ARBOR',
        'expected_extraction': {'lot': 'LOT 6', 'plat': 'ORIGINAL PLAT OF ANN ARBOR'},
        'expected_regex_name': 'township range & non-numeric plat',
    },
    {
        'PIN': '09-09-29-132-026',
        'LEGAL_DESC': 'LOTS 7 & 8, B1S, R4E, ORIGINAL PLAT OF ANN ARBOR',
        'expected_extraction': {'lot': 'LOTS 7 & 8,', 'plat': 'ORIGINAL PLAT OF ANN ARBOR'},
        'expected_regex_name': 'township range & non-numeric plat',
    },
    {
        'PIN': '09-09-29-405-001',
        'LEGAL_DESC': 'LOTS 9 THRU 13 INCL B3S R4E ORIGINAL PLAT OF ANN ARBOR',
        'expected_extraction': {'lot': 'LOTS 9 THRU 13 INCL', 'plat': 'ORIGINAL PLAT OF ANN ARBOR'},
        'expected_regex_name': 'township range & non-numeric plat',
    },

    # non-numeric plat up to subdivision ordinal phrase, followed by TWS, the rest non-numeric
    {
        'PIN': 'K -11-26-305-205',
        'LEGAL_DESC': 'LOT 205 GREENFIELDS SUBDIVISION NO. 3 T3S R7E WASHTENAW COUNTY',
        'expected_extraction': {'lot': 'LOT 205', 'plat': 'GREENFIELDS SUBDIVISION NO. 3'},
        'expected_regex_name': 'non-numeric plat up to subdivision ordinal phrase, followed by TWS, the rest non-numeric',
    },


    # What to do with this one? Probably lot should = 'LOTS 139 & 140 ALSO VACATED WALK BETWN AD LOTS'
    #{'PIN': '09-09-34-411-014', 'LEGAL_DESC': 'LOTS 139 & 140 ALSO VACATED WALK BETWN AD LOTS ANN ARBOR HILLS'} 'expected_regex_name': 'non-numeric plat not starting with EXC'

    # What to do with this one?
    #{'PIN': '09-12-03-208-004', 'LEGAL_DESC': 'LOT 27 ALSO NLY HALF VACATED CAMELOT RD ORCHARD CREST SUBDIVISION'} 'expected_regex_name': 'non-numeric plat not starting with EXC'

    # lot ending with INCL. (with a period)
    #{'PIN': 'K -11-10-482-035', 'LEGAL_DESC': 'LOTS 104 - 110 INCL. LAPHAM & HOWES YPSI MANOR SUBDIVISION.'} 'expected_regex_name': 'non-numeric plat not starting with EXC'


    # non-numeric plat followed by section, township range, acres
    {
        'PIN': 'H -08-35-165-001',
        'LEGAL_DESC': 'LOT 1 SAGINAW HILLS SOUTH SEC 35 T2S-R5E 1.26 AC',
        'expected_extraction': {'lot': 'LOT 1', 'plat': 'SAGINAW HILLS SOUTH'},
        'expected_regex_name': 'non-numeric plat followed by section, township range, acres',
    },

    # non-numeric plat followed by directional fraction, section, township range, acres
    {
        'PIN': 'H -08-11-405-001',
        'LEGAL_DESC': 'LOT 1 RIVER PINES ESTATES. SE 1/4 SEC 11, T2S-R5E, 1.40 AC.',
        'expected_extraction': {'lot': 'LOT 1', 'plat': 'RIVER PINES ESTATES.'},
        'expected_regex_name': 'non-numeric plat followed by directional fraction, section, township range, acres',
    },
    {
        'PIN': 'H -08-35-215-001',
        'LEGAL_DESC': 'LOT 1 SAGINAW HILLS SUB NW 1/4 SEC 35 T2S-R5E 3.09 AC',
        'expected_extraction': {'lot': 'LOT 1', 'plat': 'SAGINAW HILLS SUB'},
        'expected_regex_name': 'non-numeric plat followed by directional fraction, section, township range, acres',
    },
]
