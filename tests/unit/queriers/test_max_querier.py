import json
import pytest
from click.testing import CliRunner
from asreview_simulation.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max_querier
@pytest.mark.bal_double
@pytest.mark.stp_min
def test_max_querier_default_parameterization():
    runner = CliRunner()
    args = [
        "qry-max",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    querier = json.loads(result.output)["querier"]
    assert querier["abbr"] == "max"
    params = querier["params"].keys()
    assert len(params) == 1
    assert "n_instances" in params
    assert querier["params"]["n_instances"] == 1
