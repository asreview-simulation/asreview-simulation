import json
from click.testing import CliRunner
from asreview_simulation import cli


def test_max_querier_default_parameterization():
    runner = CliRunner()
    args = [
        "qer:max",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    querier = json.loads(result.output)["querier"]
    assert querier["model"] == "max"
    params = querier["params"].keys()
    assert len(params) == 0
