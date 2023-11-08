import os
import shutil
import click
from asreview_simulation._private.lib.prep_project_directory import prep_project_directory
from asreview_simulation._private.lib.run import run


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
    + "usage of --in. For valid values, refer to the output of running 'asreview-simulation print-benchmark-names'.",
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
def start_subcommand(obj, benchmark, input_file, no_zip, output_file, seed, write_interval):

    # prep
    project, as_data = prep_project_directory(benchmark, input_file, output_file)

    # run
    run(obj.models, project, as_data, write_interval, seed)

    # wrap-up
    p = project.project_path
    if no_zip:
        # rename the .asreview.tmp directory to just .asreview
        os.rename(p, p.with_suffix(""))
    else:
        # zip the results
        project.export(p.with_suffix(""))
        shutil.rmtree(p)
