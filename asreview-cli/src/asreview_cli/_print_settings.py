import click
import dataclasses
import json


@click.command("print-settings", help="Print settings")
@click.option("-p", "--pretty", "pretty", is_flag=True, help="Pretty-print the settings")
@click.pass_obj
def print_settings(obj, pretty):
    d = dataclasses.asdict(obj)
    d.pop("provided")
    if pretty:
        click.echo(json.dumps(d, indent=4, sort_keys=True))
        return
    click.echo(json.dumps(d))
