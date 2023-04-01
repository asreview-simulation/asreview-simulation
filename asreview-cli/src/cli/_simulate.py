import click


@click.command("simulate")
@click.pass_obj
def simulate(obj):
    click.echo("start simulation")
