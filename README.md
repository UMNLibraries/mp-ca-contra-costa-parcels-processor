# mp-mi-washtenaw-parcels-processor

A processor for the Contra Costa County, CA shapefile

## Quick start

To produce a modified shapefile with added `lot`, `block`, and `plat` fields:

* install with [pipenv](https://pipenv.pypa.io/en/latest/)
* display a help message for the `process` subcommand: `python -m processor process --help`
* run the command accordingly

## Overview

This is a Python CLI application that will, for a given Washtenaw County, Michigan input
shapefile, produce a new, modified shapefile with added `lot`, `block`, and `plat` fields.

## Install

For installation and package management, we use [pipenv](https://pipenv.pypa.io/en/latest/).
To install the application, clone this repository. In the repository directory, run:
`pipenv install`

## Help messages

To display an overview help message, including a list of all subcommands:
`python -m processor --help`

To display help for a subcommand:
`python -m processor SUBCOMMAND --help`

## Producing a new shapefile

Producing a new shapefile requires extracting a Washington County parcels archive
to a location readable by this application, and specifying an output directory
writable by this application, to contain the new shapefile and other associated
parcels files. Run the `process` subcommand to produce a new shapefile.

Example:

`python -m processor process -i ./input-parcels-path/input-parcels.shp -o ./output-parcels-path/`

## Development workflow

The `processor/processor.py` file does almost all the work, so that file is where you
will make most of your changes during development. The one exception to that is
`tests/regex_data.py`, which provides input for the automated tests.

More specifically, a list of `NamedRegex` objects in `processor.py` does most of the
work, and `regex_data.py` contains sample legal description strings to test against
each `NamedRegex`.

Also, for each subcommand, there is an identically named function in `processor.py`
that does the work of that subcommand.

Below we describe how to use the subcommands and automated tests to develop this list
of regexes, and ensure that they do what we want.

### Analyze

The `analyze` subcommand is for discovering what is in a shapefile, especially the
legal descriptions strings to be parsed for `lot`, `block`, and `plat` fields. For
example, the regex we used to parse Washington County, MN strings matched only strings
that start with `LOT`. So we put some code in `analyze` that told us there are
123,479 legal description strings in the Washtenaw County, MI shapefile, and that
22,650 of them start with `LOT`. We decided to start with those.

We also use `analyze` against output shapefiles, to help verify that we produced what
we expected.

As long as this function only reads shapefiles, you can put anything you want in there,
and it won't affect anything else that the processor does.

### Assort

The `assort` subcommand assorts all legal description strings that we expect to match
into lists according to which regex in the `assorting_regexes` list actually matches
each string, or into the `unmatched` list if no regex matches. 

This is how we have used it so far: We started by listing all legal description strings
that start with `LOT`, sorted by Property Identification Number (`PIN`). Not having any
regexes yet, we were hoping to find something to start with. We guessed that `PIN`s may
have been assigned in sequence to properties adjacent to each other, and which may 
therefore have similar legal description strings. This turned out to be true. Seeing
consecutive legal description strings in the `unmatched` list of the output, which were all
very similar to each other, allowed us to easily see patterns that we could use to write
regexes to match many properties at once. As we added each regex to `assorting_regexes`,
we ran `assort` again to make sure that the regexes were matching as we expected. Giving
each regex a name in a `NamedRegex` object allowed us to list the regex names in the output,
along with a list of all legal descriptions that match each named regex, so we could easily
evaluate the results. 

Like `analyze`, as long as the `assort` function only reads shapefiles, and uses only the
`assorting_regexes` list, you can put anything you want in those without breaking anything
else. Note, however, that as development progressed on strings starting with `LOT`, we
eventually found it more efficient to make the `assorting_regexes` and
`processing_regexes` lists identical. As we attempt to parse other strings, it may be easier
to add regexes to the `assorting_regexes` list first, and add them to `processing_regexes`,
which `process` uses to produce a new shapefile, later. More on that below.

### Test

To run the automated tests: `pytest tests/test_regex.py`

Once we had a significant number of regexes that were matching as expected, we started
adding them to the `processing_regexes` list and adding named captures for the `lot`,
`block`, and `plat` fields.

That gave us some very specific expected results to test against. In `tests/regex_data.py`,
we have a list of dictionaries with expected outputs for a range of inputs for each regex.
Each dictionary includes a `PIN` and `LEGAL_DESC` string, along with the `expected_regex_name`
that we expect to match that string, and an `expected_extraction` sub-dictionary of excepted
values for the named captures for `lot`, `block`, and `plat` fields.

After adding or modifying regexes, we ran the tests to ensure that not only were our changes
working as expected, but that we had not broken anything that was previously working as 
expected.

### Process

The `process` subcommand, which produces a new shapefile, is documented above in the
[Quick start](#quick-start) and [Producing a new shapefile](#producing-a-new-shapefile)
sections.

## Future improvements?

The [Development workflow](#development-workflow) described above is slow and tedious.
Is there any way we can speed it up?

One of the biggest challenges with Washtenaw County data is parsing out the plat, often
among lots of other data we do not want. While the lot and block values are relatively easy
to parse out, because they are typically preceded by the words `LOT` and `BLOCK`, respectively,
there is no such label in the data for the plat. This is especially challenging when there
are other things in the data that are not part of the plat, like parent parcels or 
township-range-section data. So far, we have matched only legal description strings where we can
identify everything else that is not part of the plat, and can therefore presume that
whatever's left is the plat. This requires lots of regexes, because these other data types
are not always present, and when they are, thay are not always present in the same order with
repsect to the plat or each other.

If we had a tool that could automatically identify and parse out these non-plat data types
we do not want, in whatever combination and order they happen to appear, that would
significantly reduce development time. We have just begun to explore the possibility of
using a machine learning, natural language processing tool, like [spaCy](https://spacy.io/),
to do that. We may be able to use what we have learned about the non-plat data types, and
the regexes we have written to match them, to automatically tag a large number of legal description
strings, which we could use to train a spaCy model.
