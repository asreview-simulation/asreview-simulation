import click
import dataclasses
import json


@click.command("print-settings")
@click.pass_obj
def print_settings(obj):
    d = dataclasses.asdict(obj)
    click.echo(json.dumps(d))


