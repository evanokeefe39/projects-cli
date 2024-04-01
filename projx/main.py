#!/usr/bin/env python
import click

from projx.cli.commands import cli
from projx.api.commands import api
from projx.pipe.commands import pipe
from projx.webapp.commands import webapp
from projx.analysis.commands import analysis


@click.group()
def root():
    pass


root.add_command(cli)
root.add_command(api)
root.add_command(pipe)
root.add_command(webapp)
root.add_command(analysis)


if __name__ == '__main__':
    root()