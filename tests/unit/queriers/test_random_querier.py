import json
from click.testing import CliRunner
from asreview_simulation import cli


def test_random_querier_default_parameterization():
    runner = CliRunner()
    args = [
        "qer:random",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    querier = json.loads(result.output)["querier"]
    assert querier["model"] == "random"
