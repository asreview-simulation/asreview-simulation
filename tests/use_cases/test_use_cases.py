import os
from random import random
from tempfile import TemporaryDirectory
import pytest
from matplotlib import pyplot as plt
from asreviewcontrib.simulation.api import Config
from asreviewcontrib.simulation.api import draw_sample
from asreviewcontrib.simulation.api import get_pyll
from asreviewcontrib.simulation.api import OneModelConfig
from asreviewcontrib.simulation.api import prep_project_directory
from asreviewcontrib.simulation.api import run
from asreviewcontrib.simulation.api.plotting import plot_trellis


# arbitrary choice of benchmark
benchmark = "benchmark:Cohen_2006_ADHD"


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
@pytest.mark.ofn_none
def test_use_case_all_models_default():
    # construct an all-model config using the default model choise for each flavor of
    # model, and the default parameterization for each flavor
    config = Config()

    # create a temporary directory and start the simulation
    with TemporaryDirectory(prefix="asreview-simulation.") as tmpdir:
        output_file = f"{tmpdir}{os.sep}project.asreview"
        project, as_data = prep_project_directory(benchmark=benchmark, output_file=output_file)
        run(config, project, as_data)


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_svm
@pytest.mark.qry_max_random
@pytest.mark.bal_double
@pytest.mark.stp_nq
@pytest.mark.ofn_none
def test_use_case_some_models_nondefault():
    # make classifier model config using default parameter values given the model name
    cls = OneModelConfig("cls-svm")

    # make query model config using positional arguments, partial params dict
    qry = OneModelConfig("qry-max-random", {"fraction_max": 0.90})

    # make stopping model config using keyword arguments
    stp = OneModelConfig(abbr="stp-nq", params={"n_queries": 10})

    # construct an all-model config from one-model configs -- implicitly use default model choice
    # and parameterization for models not included as argument (i.e. sam, fex, bal, ofn)
    config = Config(cls=cls, qry=qry, stp=stp)

    # create a temporary directory and start the simulation
    with TemporaryDirectory(prefix="asreview-simulation.") as tmpdir:
        output_file = f"{tmpdir}{os.sep}project.asreview"
        project, as_data = prep_project_directory(benchmark=benchmark, output_file=output_file)
        run(config, project, as_data)


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_svm
@pytest.mark.qry_max_random
@pytest.mark.bal_double
@pytest.mark.stp_rel
@pytest.mark.ofn_wss
def test_use_case_some_models_nondefault_some_models_drawn():
    # make classifier model config using default parameter values given the model name
    cls = OneModelConfig("cls-svm")

    # make query model config using positional arguments
    qry = OneModelConfig(
        "qry-max-random",
        {
            "n_instances": 10,
            "fraction_max": 0.90,
        },
    )

    # make stopping model config using keyword arguments
    stp = OneModelConfig(abbr="stp-rel")

    # use wss @ 90% recall as objective function
    ofn = OneModelConfig(abbr="ofn-wss", params={"at_pct": 90})

    # use pyll programs to draw a parameterization for 'bal' and 'fex'
    pyll = {
        "bal": get_pyll("bal-double"),
        "fex": get_pyll("fex-tfidf"),
    }
    drawn = draw_sample(pyll)

    # construct an all-model config from one-model configs -- implicitly use default model choice
    # and parameterization for models not included as argument (i.e. sam)
    config = Config(cls=cls, qry=qry, stp=stp, ofn=ofn, **drawn)

    # create a temporary directory and start the simulation
    with TemporaryDirectory(prefix="asreview-simulation.") as tmpdir:
        output_file = f"{tmpdir}{os.sep}project.asreview"
        project, as_data = prep_project_directory(benchmark=benchmark, output_file=output_file)
        wss = run(config, project, as_data)
        assert wss is not None


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
@pytest.mark.ofn_wss
def test_use_case_some_models_drawn_100_samples():
    # use wss @ 90% recall as objective function
    fixed = {
        "ofn": OneModelConfig(abbr="ofn-wss", params={"at_pct": 90}),
        "qry": OneModelConfig(abbr="qry-max", params={"n_instances": 10}),
    }

    pyll = {
        "bal": get_pyll("bal-double"),
        "fex": get_pyll("fex-tfidf"),
    }

    n_samples = 100
    results = []

    for _ in range(n_samples):
        # use pyll programs to draw a parameterization for 'bal' and 'fex'
        drawn = draw_sample(pyll)

        # construct an all-model config from one-model configs -- implicitly use default model choice
        # and parameterization for models not included as argument
        config = Config(**fixed, **drawn)

        # create a temporary directory and start the simulation
        with TemporaryDirectory(prefix="asreview-simulation.") as tmpdir:
            output_file = f"{tmpdir}{os.sep}project.asreview"
            project, as_data = prep_project_directory(benchmark=benchmark, output_file=output_file)
            wss = run(config, project, as_data)
            assert wss is not None

        results.append((config, wss))

    if "PYTEST_CURRENT_TEST" not in os.environ:
        plt.figure()
        plot_trellis(
            results,
            [
                "bal-double/a",
                "bal-double/alpha",
                "bal-double/b",
                "bal-double/beta",
                "fex-tfidf/ngram_max",
                "fex-tfidf/split_ta",
                "fex-tfidf/stop_words",
                "fex-tfidf/use_keywords",
            ],
        )
        plt.show()


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
@pytest.mark.ofn_wss
def test_trellis():
    # use wss @ 90% recall as objective function
    fixed = {
        "ofn": OneModelConfig(abbr="ofn-wss", params={"at_pct": 90}),
    }

    pyll = {
        "bal": get_pyll("bal-double"),
        "fex": get_pyll("fex-tfidf"),
    }

    n_samples = 100
    results = []

    for _ in range(n_samples):
        # use pyll programs to draw a parameterization for 'bal' and 'fex'
        drawn = draw_sample(pyll)

        # construct an all-model config from one-model configs -- implicitly use default model choice
        # and parameterization for models not included as argument
        config = Config(**fixed, **drawn)
        results.append((config, random()))

    if "PYTEST_CURRENT_TEST" not in os.environ:
        plt.figure()
        plot_trellis(
            results,
            [
                "bal-double/a",
                "bal-double/alpha",
                "bal-double/b",
                "bal-double/beta",
                "fex-tfidf/ngram_max",
                "fex-tfidf/split_ta",
                "fex-tfidf/stop_words",
                "fex-tfidf/use_keywords",
            ],
        )
        plt.show()
