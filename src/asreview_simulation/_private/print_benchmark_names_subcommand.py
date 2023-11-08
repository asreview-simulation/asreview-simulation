import click
from asreview_simulation._private.lib.list_dataset_names import list_dataset_names


@click.command(
    "print-benchmark-names",
    help="Print the names of available benchmark datasets.",
    short_help="Print benchmark names",
)
def print_benchmark_names_subcommand():
    s = "\n".join([name for name in list_dataset_names()])
    click.echo(s)
