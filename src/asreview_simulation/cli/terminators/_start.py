import os
import shutil
import click
import numpy
from asreview.models.balance import get_balance_model
from asreview.models.classifiers import get_classifier
from asreview.models.feature_extraction import get_feature_model
from asreview.models.query import get_query_model
from asreview.review.simulate import ReviewSimulate
from asreview_simulation.lib.wrangling import assign_vars_for_prior_sampling
from asreview_simulation.lib.wrangling import assign_vars_for_stopping
from asreview_simulation.lib.wrangling import prep_project_directory


@click.command(
    "start",
    help="Start the simulation",
    context_settings=dict(max_content_width=120),
    short_help="Start the simulation",
)
@click.option(
    "--benchmark",
    "benchmark",
    default=None,
    help="Name of the dataset that contains the fully labeled data. Precludes "
    + f"usage of --in. For valid values, refer to the output of running 'asreview-simulation print-benchmark-names'.",
    type=click.STRING,
)
@click.option(
    "--in",
    "input_file",
    default=None,
    help="Name of the file that contains the fully labeled data. Precludes usage of --benchmark. Valid file "
    + "formats are csv, ris, tsv, and xlsx. See the ASReview documentation https://asreview.readthedocs.io "
    + "for details.",
    type=click.Path(exists=True, readable=True),
)
@click.option(
    "--no-zip",
    "no_zip",
    default=False,
    help="Include this flag to avoid zipping the results of the analysis",
    is_flag=True,
)
@click.option(
    "--out",
    "output_file",
    default=None,
    help="Name of the file that will hold the results. Filename must end in '.asreview'.",
    required=True,
    type=click.Path(),
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
def start(obj, benchmark, input_file, no_zip, output_file, seed, write_interval):
    project, as_data = prep_project_directory(benchmark, input_file, output_file)

    random_state = numpy.random.RandomState(seed)

    # these are not valid parameter names, pop them into variables of their own
    n_instances = obj.querier.params.pop("n_instances", 1)

    # assign model parameterizations using the data from obj
    if obj.extractor.abbr == "embedding-lstm":
        assert obj.classifier.abbr.startswith(
            "lstm-"
        ), "fex-embedding-lstm only works with cls-lstm-* classifiers."
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
    stop_if = assign_vars_for_stopping(obj, as_data, n_instances)
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

    p = project.project_path
    if no_zip:
        # rename the .asreview.tmp directory to just .asreview
        os.rename(p, p.with_suffix(""))
    else:
        # zip the results
        project.export(p.with_suffix(""))
        shutil.rmtree(p)
