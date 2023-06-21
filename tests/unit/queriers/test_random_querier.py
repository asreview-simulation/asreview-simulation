import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_random_querier_default_parameterization():
    runner = CliRunner()
    args = [
        "qry-random",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    querier = json.loads(result.output)["querier"]
    assert querier["abbr"] == "random"
    params = querier["params"].keys()
    assert len(params) == 1
    assert "n_instances" in params
    assert querier["params"]["n_instances"] == 1
