import os
from pathlib import Path

import click

from . import processor

@click.group()
def cli():
    pass

infile_args = [
    '--infile',
    '-i',
]
infile_kwargs = {
    'nargs': 1,
    'required': True,
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
    required=True,
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
    processor.process(infile, outdir)

@cli.command()
@click.option(
    *infile_args,
    **infile_kwargs,
)
def analyze(infile):
    '''Display an analysis of an input shape file. Prints to STDOUT'''
    processor.analyze(infile)

@cli.command()
@click.option(
    *infile_args,
    **infile_kwargs,
)
def assort(infile):
    '''Assort by matching regexes all legal description strings meeting certian criteria. Usually produces a lot of output, so redirecting STDOUT to a file is probably best'''
    processor.assort(infile)

cli()
