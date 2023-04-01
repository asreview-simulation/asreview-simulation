import click
import dataclasses
import json


@click.command("print-settings", help="Print settings")
@click.pass_obj
def print_settings(obj):
    d = dataclasses.asdict(obj)
    d.pop("provided")
    click.echo(json.dumps(d))
