import click
from asreviewlib import list_datasets


dataset_names = list_datasets().keys()


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
        raise Exception("Neither '--data' nor '--dataset' was set.")
    if data is not None and dataset is not None:
        raise Exception("Expected '--data' or '--dataset' to be set, found both.")
    click.echo("simulation starting")
    click.echo("doing things...")
    click.echo("simulation ended")
