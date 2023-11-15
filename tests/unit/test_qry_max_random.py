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
    querier = json.loads(result.output)["qry"]
    assert querier["abbr"] == "qry-max-random"
    params = querier["params"].keys()
    assert len(params) == 2
    assert "fraction_max" in params
    assert querier["params"]["fraction_max"] == 0.95
    assert "n_instances" in params
    assert querier["params"]["n_instances"] == 1