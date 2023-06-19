from warnings import warn
import click
import numpy
from asreview.models.balance import get_balance_model
from asreview.models.classifiers import get_classifier
from asreview.models.feature_extraction import get_feature_model
from asreview.models.query import get_query_model
from asreview.review.simulate import ReviewSimulate
from asreview_simulation.lib import assign_vars_for_prior_sampling
from asreview_simulation.lib import assign_vars_for_stopping
from asreview_simulation.lib import list_dataset_names
from asreview_simulation.lib import prep_project_directory


@click.command(
    "start",
    help="Start the simulation and write the results to a new file DOT_ASREVIEW_FILE.\n\n"
    + "This command terminates parsing of further input supplied via the command line.",
    context_settings=dict(max_content_width=120),
)
@click.argument("dot_asreview_file", type=click.STRING)
@click.option(
    "--data",
    "data",
    default=None,
    help="Name of the file that contains the fully labeled data. Precludes usage of --dataset.",
    type=click.Path(exists=True, readable=True),
)
@click.option(
    "--dataset",
    "dataset",
    default=None,
    help="Name of the dataset that contains the fully labeled data. Precludes "
    + "usage of --data. Valid options are: "
    + ", ".join([f"'{d}'" for d in list_dataset_names()]),
    type=click.STRING,
)
@click.option(
    "--seed",
    "seed",
    default=None,
    help="Random seed for the classifier, balancer, extractor and querier",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--write-interval",
    "write_interval",
    help="Write interval. The simulation data will be written to file after each set of this many labeled records. "
    + "By default only writes data at the end of the simulation to make it as fast as possible.",
    type=click.INT,
)
@click.pass_obj
def start(obj, dot_asreview_file, data, dataset, seed, write_interval):
    """
    DOT_ASREVIEW_FILE: the file that will hold the results
    """
    if data is None and dataset is None:
        raise ValueError("Neither '--data' nor '--dataset' was specified.")
    if data is not None and dataset is not None:
        raise ValueError(
            "Expected either '--data' or '--dataset' to be specified, found both."
        )
    if dataset not in list_dataset_names():
        warn("Unrecognized dataset name, not sure this is going to work.")

    project, as_data = prep_project_directory(dot_asreview_file, dataset)

    random_state = numpy.random.RandomState(seed)

    # these are not valid parameter names, pop them into variables of their own
    n_instances = obj.querier.params.pop("n_instances", 1)

    # assign model parameterizations using the data from obj
    if obj.extractor.abbr == "embedding-lstm":
        assert obj.classifier.abbr.startswith("lstm-"), "fex:embedding-lstm only works with cls:lstm-* classifiers."
        classifier = get_classifier(
            obj.classifier.abbr, random_state=random_state, **obj.classifier.params
        )
        embedding_fp = obj.extractor.params.pop("embedding_fp", None)
        extractor = get_feature_model(
            obj.extractor.abbr, random_state=random_state, **obj.extractor.params
        )
        classifier.embedding_matrix = extractor.get_embedding_matrix(
            as_data.texts, embedding_fp
        )
    else:
        classifier = get_classifier(
            obj.classifier.abbr, random_state=random_state, **obj.classifier.params
        )
        extractor = get_feature_model(
            obj.extractor.abbr, random_state=random_state, **obj.extractor.params
        )
    querier = get_query_model(
        obj.querier.abbr, random_state=random_state, **obj.querier.params
    )
    balancer = get_balance_model(
        obj.balancer.abbr, random_state=random_state, **obj.balancer.params
    )

    n_papers = None
    stop_if = assign_vars_for_stopping(obj)
    (
        prior_indices,
        n_prior_included,
        n_prior_excluded,
        init_seed,
    ) = assign_vars_for_prior_sampling(obj, as_data)

    reviewer = ReviewSimulate(
        as_data,
        project=project,
        model=classifier,
        query_model=querier,
        balance_model=balancer,
        feature_model=extractor,
        n_papers=n_papers,
        n_instances=n_instances,
        stop_if=stop_if,
        prior_indices=prior_indices,
        n_prior_included=n_prior_included,
        n_prior_excluded=n_prior_excluded,
        init_seed=init_seed,
        write_interval=write_interval,
    )

    project.update_review(status="review")  # (has side effects on disk)
    click.echo("Simulation started")
    reviewer.review()
    click.echo("Simulation finished")
    project.mark_review_finished()  # (has side effects on disk)
