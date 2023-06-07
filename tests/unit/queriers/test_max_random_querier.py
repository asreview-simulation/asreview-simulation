import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_max_random_querier_default_parameterization():
    runner = CliRunner()
    args = [
        "qry:max_random",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    querier = json.loads(result.output)["querier"]
    assert querier["abbr"] == "max_random"
    params = querier["params"].keys()
    assert "mix_ratio" in params
    assert querier["params"]["mix_ratio"] == 0.95
