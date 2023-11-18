import os
from tempfile import TemporaryDirectory
import pytest
from asreview_simulation.api import AllModelConfig
from asreview_simulation.api import draw_sample
from asreview_simulation.api import get_dataset_names
from asreview_simulation.api import get_pyll
from asreview_simulation.api import OneModelConfig
from asreview_simulation.api import prep_project_directory
from asreview_simulation.api import run


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_svm
@pytest.mark.qry_max_random
@pytest.mark.bal_double
@pytest.mark.stp_nq
def test_use_case():
    # make classifier model config using default parameter values given the model name
    cls = OneModelConfig("cls-svm")

    # make query model config using positional arguments, partial params dict
    qry = OneModelConfig("qry-max-random", {"fraction_max": 0.90})

    # make stopping model config using keyword arguments
    stp = OneModelConfig(abbr="stp-nq", params={"n_queries": 10})

    # use pyll programs to draw a parameterization for 'bal' and 'fex'
    pyll = {
        "bal": get_pyll("bal-double"),
        "fex": get_pyll("fex-tfidf"),
    }
    drawn = draw_sample(pyll)

    # construct an all model config from one model configs -- implicitly use default model choice
    # and parameterization for models not included as argument (i.e. sam)
    models = AllModelConfig(cls=cls, qry=qry, stp=stp, **drawn)

    # arbitrarily pick a benchmark dataset
    benchmark = get_dataset_names()[4]

    # create a temporary directory and start the simulation
    with TemporaryDirectory(prefix="asreview-simulation.") as tmpdir:
        output_file = f"{tmpdir}{os.sep}simulate.asreview"
        project, as_data = prep_project_directory(benchmark=benchmark, output_file=output_file)
        obj_score = run(models, project, as_data)
        assert obj_score is None
