import os
from pathlib import Path

import click

from . import processor
from dotenv import load_dotenv

load_dotenv()

INFILE_ENV = os.getenv('INFILE')
OUTDIR_ENV = os.getenv('OUTDIR')
PIN_FIELD = os.getenv('PIN_FIELD')
LEGAL_DESC_FIELD = os.getenv('LEGAL_DESC_FIELD')

@click.group()
def cli():
    pass

infile_args = [
    '--infile',
    '-i',
]
infile_kwargs = {
    'nargs': 1,
    'required': False,
    'type': click.File('r'),
    'help': 'Name of, and path to, an input shape file',
}

@cli.command()
@click.option(
    *infile_args,
    **infile_kwargs,
)
@click.option(
    '--outdir',
    '-o',
    nargs=1,
    required=False,
    type=click.Path(
        #exists=True,
        exists=False,
        file_okay=False,
        readable=True,
        writable=True,
        path_type=Path,
    ),
    help='Destination directory for the output shape file',
)
def process(infile, outdir):
    '''Create a new shape file with lot, block, plat fields.

    Example:

    python -m processor process -i ./input-parcels-path/input-parcels.shp -o ./output-parcels-path/
    '''
    if not infile:
        if INFILE_ENV:
            infile = INFILE_ENV
    if not infile:
        raise "Must specify infile with --infile or .env"

    if not outdir:
        if OUTDIR_ENV:
            outdir = OUTDIR_ENV
    if not outdir:
        raise "Must specify infile with --outfile or .env"

    # try:
    #     pin_field = PIN_FIELD
    # except:
    #     pin_field = 'PIN'

    try:
        legal_desc_field = LEGAL_DESC_FIELD
    except:
        legal_desc_field = 'LEGAL_DESC'

    processor.process(infile, outdir, legal_desc_field)

@cli.command()
@click.option(
    *infile_args,
    **infile_kwargs,
)
def analyze(infile):
    '''Display an analysis of an input shape file. Prints to STDOUT'''

    if not infile:
        if INFILE_ENV:
            infile = Path(INFILE_ENV)
    if not infile:
        raise "Must specify infile with --infile or .env"

    # if not outdir:
    #     if OUTDIR_ENV:
    #         outdir = OUTDIR_ENV
    # if not outdir:
    #     raise "Must specify infile with --outfile or .env"

    try:
        pin_field = PIN_FIELD
    except:
        pin_field = 'PIN'

    try:
        legal_desc_field = LEGAL_DESC_FIELD
    except:
        legal_desc_field = 'LEGAL_DESC'
    processor.analyze(infile, pin_field, legal_desc_field)

@cli.command()
@click.option(
    *infile_args,
    **infile_kwargs,
)
def assort(infile):
    '''Assort by matching regexes all legal description strings meeting certian criteria. Usually produces a lot of output, so redirecting STDOUT to a file is probably best'''

    if not infile:
        if INFILE_ENV:
            infile = INFILE_ENV
    if not infile:
        raise "Must specify infile with --infile or .env"

    # if not outdir:
    #     if OUTDIR_ENV:
    #         outdir = OUTDIR_ENV

    if not PIN_FIELD:
        PIN_FIELD = 'PIN'

    if not LEGAL_DESC:
        LEGAL_DESC = 'LEGAL_DESC'

    processor.assort(infile, PIN_FIELD, LEGAL_DESC)

cli()
