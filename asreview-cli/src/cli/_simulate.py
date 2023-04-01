import click


@click.command("simulate", help="Run simulation and exit; terminates parsing")
@click.pass_obj
def simulate(obj):
    click.echo("start simulation")
