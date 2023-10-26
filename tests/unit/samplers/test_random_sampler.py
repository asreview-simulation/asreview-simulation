import json
from click.testing import CliRunner
from asreview_simulation.cli import cli
import pytest


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_min
def test_random_sampler_default_parameterization():
    runner = CliRunner()
    args = [
        "sam-random",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    sampler = json.loads(result.output)["sampler"]
    assert sampler["abbr"] == "random"
    params = sampler["params"].keys()
    assert "n_included" in params
    assert sampler["params"]["n_included"] == 1
    assert "n_excluded" in params
    assert sampler["params"]["n_excluded"] == 1
