import click
from asreview.utils import get_entry_points


dataset_names = get_entry_points("asreview.datasets").keys()


@click.command("start",
               help="Start the simulation and exit; terminates parsing")
@click.option("--data", "data",
              default=None,
              help="Name of the file that contains the fully labeled data. Precludes usage of --dataset.",
              type=click.Path(exists=True, readable=True))
@click.option("--dataset", "dataset",
              default=None,
              help="Name of the dataset that contains the fully labeled data. Precludes usage of --data.",
              type=click.Choice(dataset_names))
@click.option("--write-interval", "write_interval",
              help="Write interval.",
              type=click.INT)
@click.pass_obj
def start(obj, data, dataset, write_interval):
    if data is None and dataset is None:
        raise ValueError("Neither '--data' nor '--dataset' was specified.")
    if data is not None and dataset is not None:
        raise ValueError("Expected either '--data' or '--dataset' to be specified, found both.")
    click.echo("simulation starting")
    click.echo("doing things...")
    click.echo("simulation ended")
