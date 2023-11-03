import click
from asreview_simulation.lib.wrangling import list_dataset_names


@click.command(
    "print-benchmark-names",
    help="Print the names of available benchmark datasets.",
    short_help="Print benchmark names",
)
def print_benchmark_names():
    s = "\n".join([name for name in list_dataset_names()])
    click.echo(s)
