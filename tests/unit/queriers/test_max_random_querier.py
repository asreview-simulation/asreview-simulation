import json
import pytest
from click.testing import CliRunner
from asreview_simulation._private.cli.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max_random
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_max_random_querier_default_parameterization():
    runner = CliRunner()
    args = [
        "qry-max-random",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    querier = json.loads(result.output)["querier"]
    assert querier["abbr"] == "max_random"
    params = querier["params"].keys()
    assert len(params) == 2
    assert "mix_ratio" in params
    assert querier["params"]["mix_ratio"] == 0.95
    assert "n_instances" in params
    assert querier["params"]["n_instances"] == 1
