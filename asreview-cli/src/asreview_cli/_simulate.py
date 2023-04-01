import click


@click.command("simulate", help="Run simulation and exit; terminates parsing")
@click.pass_obj
def simulate(obj):
    click.echo("simulation starting")
    click.echo("doing things...")
    click.echo("simulation ended")
