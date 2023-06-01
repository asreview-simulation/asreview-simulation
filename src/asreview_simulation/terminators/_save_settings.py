import dataclasses
import json
import click


@click.command("save-settings",
               help="Save settings")
@click.argument("filename", type=click.File("w"))
@click.option("-p", "--pretty", "pretty",
              help="Pretty-print the settings",
              is_flag=True)
@click.pass_obj
def save_settings(obj, filename, pretty):
    d = dataclasses.asdict(obj)
    d.pop("provided")
    if pretty:
        with filename as f:
            s = json.dumps(d, indent=4, sort_keys=True)
            f.write(s)
        return
    with filename as f:
        s = json.dumps(d)
        f.write(s)
