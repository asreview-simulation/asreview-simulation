import click


@click.command("start", help="Start the simulation and exit; terminates parsing\n\n    DATA_FILE: " +
               "path to the fully labeled data")
@click.argument("data_file", type=click.Path(exists=True, readable=True))
@click.option("--write-interval", "write_interval", type=click.INT, help="Write interval.")
@click.pass_obj
def start(obj, data_file, write_interval):
    click.echo("simulation starting")
    click.echo("doing things...")
    click.echo("simulation ended")
