import os
import shutil
from typing import Optional
from asreview.data import ASReviewData
from asreview.project import ASReviewProject
from asreview.review.simulate import ReviewSimulate
from asreviewcontrib.simulation._private.lib.calc_ofn_score import calc_ofn_score
from asreviewcontrib.simulation._private.lib.config import Config
from asreviewcontrib.simulation._private.lib.unwrapping.get_review_simulate_kwargs import get_review_simulate_kwargs


def run(
    config: Config,
    project: ASReviewProject,
    as_data: ASReviewData,
    write_interval: int = None,
    seed: int = None,
    no_zip: bool = False,
) -> Optional[float]:
    """
    Args:
        config:
            The choice of 7 types of model and their parameterization.
        project:
            The `ASReviewProject` object, see https://asreview.readthedocs.io
        as_data:
            The `ASReviewData` object, see https://asreview.readthedocs.io
        write_interval:
            Interval measured in number of queries at which to
            write the state from memory to the state file.
        seed:
            Random seed for the simulation
        no_zip:
            Whether to forgo compressing the project temporary directory into a
            zipped archive once the simulation ends.

    Returns:
        The objective score or `None`.

    Synopsis:

        Runs the ASReview simulation with the provided choice of models and their
        parameterization (i.e., input argument `config`).

    Example usage:

        ```python
        import os
        import tempfile
        from asreviewcontrib.simulation.api import Config
        from asreviewcontrib.simulation.api import OneModelConfig
        from asreviewcontrib.simulation.api import prep_project_directory
        from asreviewcontrib.simulation.api import run

        # make a classifier model config using default parameter values
        # given the model name
        cls = OneModelConfig("cls-svm")

        # make a query model config using positional arguments, and a
        # partial params dict
        qry = OneModelConfig("qry-max-random", {"fraction_max": 0.90})

        # make a stopping model config using keyword arguments
        stp = OneModelConfig(abbr="stp-nq", params={"n_queries": 10})

        # construct an all model config from one model configs -- implicitly
        # use default model choice and parameterization for models not
        # included as argument (i.e. sam, fex, bal, ofn)
        config = Config(cls=cls, qry=qry, stp=stp)

        # arbitrarily pick a benchmark dataset
        benchmark = "benchmark:Cohen_2006_ADHD"

        # create a temporary directory
        tmpdir = tempfile.mkdtemp(prefix="asreview-simulation.", dir=".")
        output_file = f"{tmpdir}{os.sep}project.asreview"

        # prepare the directory that holds the state of the simulation
        project, as_data = prep_project_directory(benchmark=benchmark,
                                                  output_file=output_file)

        # start the simulation
        run(config, project, as_data)
        ```
    """

    # prep
    kwargs = get_review_simulate_kwargs(config, as_data, seed)
    reviewer = ReviewSimulate(as_data, project=project, **kwargs, write_interval=write_interval)

    # run
    project.update_review(status="review")  # (has side effects on disk)
    reviewer.review()
    project.mark_review_finished()  # (has side effects on disk)

    # wrap-up
    p = project.project_path
    if no_zip:
        # rename the .asreview.tmp directory to just .asreview
        os.rename(p, p.with_suffix(""))
    else:
        # zip the results
        project.export(p.with_suffix(""))
        shutil.rmtree(p)

    return calc_ofn_score(config.ofn, p.with_suffix(""))
