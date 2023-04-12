import click


@click.command("cli", context_settings={"help_option_names": ["-h", "--help"]})
def cli():
    click.echo("Starting Flask app...")
    click.echo("Doing things...")
    click.echo("Done")
