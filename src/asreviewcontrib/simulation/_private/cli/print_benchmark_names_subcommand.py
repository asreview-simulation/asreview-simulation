import click
from asreviewcontrib.simulation._private.lib.get_dataset_names import get_dataset_names


@click.command(
    "print-benchmark-names",
    help="Print the names of available benchmark datasets.",
    short_help="Print benchmark names",
)
def print_benchmark_names_subcommand():
    s = "\n".join([name for name in get_dataset_names()])
    click.echo(s)
