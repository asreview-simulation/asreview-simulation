from pathlib import Path
from warnings import warn
import click
from asreview.data import load_data
from asreview.datasets import DatasetManager
from asreview.models.balance import get_balance_class
from asreview.models.classifiers import get_classifier_class
from asreview.models.feature_extraction import get_feature_class
from asreview.models.query import get_query_class
from asreview.project import ASReviewProject
from asreview.review.simulate import ReviewSimulate


def list_dataset_names():
    dataset_names = list()
    for group in DatasetManager().list():
        for dataset in group["datasets"]:
            dataset_names.append(f"{group['group_id']}:{dataset['dataset_id']}")
    return dataset_names


def prep_project_directory(asreview_file, dataset):
    # Prepare an *.asreview.tmp directory which will contain the log / state / configuration
    # of the ASReview analysis. The directory will be zipped later and renamed to *.asreview
    name = Path(asreview_file).stem
    project_path = Path(asreview_file).with_suffix(".asreview.tmp")
    project = ASReviewProject.create(project_path,
                                     project_id=name,
                                     project_name=name,
                                     project_mode="simulate",
                                     project_description="Simulation created via ASReview command line interface")

    # Add the dataset to the project directory.
    as_data = load_data(dataset)
    if len(as_data) == 0:
        raise ValueError("Supply at least one dataset with at least one record.")
    dataset_path = f"{dataset[10:]}.csv" if dataset.startswith("benchmark:") else f"{dataset}.csv"
    as_data.to_file(project_path / "data" / dataset_path)

    # Write settings to settings.json
    project.update_config(dataset_path=dataset_path)
    return project, as_data


def assign_vars_prior_sampling(obj):
    prior_idx = None
    n_prior_included = None
    n_prior_excluded = None
    if obj.sampler == "handpicked":
        prior_idx = obj.sampler.params
    if obj.sampler == "random":
        n_prior_included = obj.sampler.n_included
        n_prior_excluded = obj.sampler.n_excluded
    return prior_idx, n_prior_included, n_prior_excluded


@click.command("start",
               help="Start the simulation and write the results to a new file DOT_ASREVIEW_FILE.\n\n" +
                    "This command terminates parsing of further input supplied via the command line.",
               context_settings=dict(max_content_width=120))
@click.argument("dot_asreview_file", type=click.STRING)
@click.option("--data", "data",
              default=None,
              help="Name of the file that contains the fully labeled data. Precludes usage of --dataset.",
              type=click.Path(exists=True, readable=True))
@click.option("--dataset", "dataset",
              default=None,
              help="Name of the dataset that contains the fully labeled data. Precludes " +
                   "usage of --data. Valid options are: " + ", ".join([f"'{d}'" for d in list_dataset_names()]),
              type=click.STRING)
@click.option("--write-interval", "write_interval",
              help="Write interval.",
              type=click.INT)
@click.pass_obj
def start(obj, dot_asreview_file, data, dataset, write_interval):
    """
    DOT_ASREVIEW_FILE: the file that will hold the results
    """
    if data is None and dataset is None:
        raise ValueError("Neither '--data' nor '--dataset' was specified.")
    if data is not None and dataset is not None:
        raise ValueError("Expected either '--data' or '--dataset' to be specified, found both.")
    if dataset not in list_dataset_names():
        warn("Unrecognized dataset name, not sure this is going to work.")

    project, as_data = prep_project_directory(dot_asreview_file, dataset)

    classifier = get_classifier_class(obj.classifier.model)(**obj.classifier.params)
    querier = get_query_class(obj.querier.model)(**obj.querier.params)
    balancer = get_balance_class(obj.balancer.model)(**obj.balancer.params)
    extractor = get_feature_class(obj.extractor.model)(**obj.extractor.params)

    n_papers = None
    n_instances = 1
    stop_if = "min"
    prior_idx, n_prior_included, n_prior_excluded = assign_vars_prior_sampling(obj)

    reviewer = ReviewSimulate(as_data,
                              project=project,
                              model=classifier,
                              query_model=querier,
                              balance_model=balancer,
                              feature_model=extractor,
                              n_papers=n_papers,
                              n_instances=n_instances,
                              stop_if=stop_if,
                              prior_indices=prior_idx,
                              n_prior_included=n_prior_included,
                              n_prior_excluded=n_prior_excluded,
                              write_interval=write_interval)

    project.update_review(status="review")  # (has side effects on disk)
    click.echo("Simulation started")
    reviewer.review()
    click.echo("Simulation finished")
    project.mark_review_finished()          # (has side effects on disk)
