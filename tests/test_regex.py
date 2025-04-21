import re
from importlib import import_module

import pytest

from processor import processor
assorting_regexes = processor.assorting_regexes
processing_regexes = processor.processing_regexes

regex_data = import_module(f'..regex_data', package=__name__)

def test_regex_class():
    assert all(
        [isinstance(named_regex.regex, re.Pattern) for named_regex in assorting_regexes + processing_regexes]
    )

@pytest.mark.parametrize(
    'pin, legal, expected_extraction',  
    [
        (item['PIN'], item['LEGAL_DESC'], item['expected_extraction'])  
        for item in regex_data.data
    ]
)  
def test_assorting_regexes(pin, legal, expected_extraction):
    '''At least one regex should match. Is this a good test?'''
    assert next((
        named_regex.name # Should be truthy
        for named_regex
        in assorting_regexes
        if re.match(named_regex.regex, legal)
    ), None) # None is falsy, which will be returned if no regex matches

@pytest.mark.parametrize(
    'pin, legal, expected_extraction, expected_regex_name',  
    [
        (item['PIN'], item['LEGAL_DESC'], item['expected_extraction'], item['expected_regex_name'])  
        for item in regex_data.data
    ]
)
def test_processing_regexes(pin, legal, expected_extraction, expected_regex_name):
    def attempt_match(named_regex, legal):
        matched = re.match(named_regex.regex, legal)
        return (
            named_regex,
            {k: v.strip() for k, v in matched.groupdict().items()}
        ) if matched else (None,None)

    named_regex, extraction = next(
        filter(
            lambda result: result[0] is not None,
            (
                attempt_match(named_regex, legal)
                for named_regex
                in processing_regexes
            )
        ), (None,None)
    )
    assert named_regex.name == expected_regex_name
    assert extraction == expected_extraction
