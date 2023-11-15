import os
from tempfile import TemporaryDirectory
import pytest
from asreview_simulation.api import CompleteConfig
from asreview_simulation.api import list_dataset_names
from asreview_simulation.api import PartialConfig
from asreview_simulation.api import prep_project_directory
from asreview_simulation.api import run


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_svm
@pytest.mark.qry_max_random
@pytest.mark.bal_double
@pytest.mark.stp_nq
def test_use_case_1():
    # make partial config using default parameter values given the model name
    cls = PartialConfig("cls-svm")

    # make partial config using positional arguments, partial params dict
    qry = PartialConfig("qry-max-random", {"fraction_max": 0.90})

    # make partial config using keyword arguments
    stp = PartialConfig(abbr="stp-nq", params={"n_queries": 10})

    # construct a complete config from partial configs -- implicitly use default model choice
    # and parameterization for models not included as argument (i.e. bal, stp, sam)
    models = CompleteConfig(cls=cls, qry=qry, stp=stp)

    benchmark = list_dataset_names()[4]
    with TemporaryDirectory(prefix="asreview-simulation.") as tmpdir:
        output_file = f"{tmpdir}{os.sep}simulate.asreview"
        project, as_data = prep_project_directory(benchmark=benchmark, output_file=output_file)
        run(models, project, as_data)
        assert True
