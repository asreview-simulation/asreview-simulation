import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_undersample_balancer_default_parameterization():
    runner = CliRunner()
    args = [
        "bal:undersample",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    balancer = json.loads(result.output)["balancer"]
    assert balancer["abbr"] == "undersample"
    params = balancer["params"].keys()
    assert "ratio" in params
    assert balancer["params"]["ratio"] == 1.0
