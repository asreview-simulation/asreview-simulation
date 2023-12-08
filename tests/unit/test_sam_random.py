import json
import pytest
from click.testing import CliRunner
from asreviewcontrib.simulation._private.cli.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.clr_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_random_sampler_default_parameterization():
    runner = CliRunner()
    args = [
        "sam-random",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    sampler = json.loads(result.output)["sam"]
    assert sampler["abbr"] == "sam-random"
    params = sampler["params"].keys()
    assert "n_included" in params
    assert sampler["params"]["n_included"] == 1
    assert "n_excluded" in params
    assert sampler["params"]["n_excluded"] == 1
