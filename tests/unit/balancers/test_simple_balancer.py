import json
from click.testing import CliRunner
from asreview_simulation import cli


def test_simple_balancer_default_parameterization():
    runner = CliRunner()
    args = [
        "bal:simple",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    balancer = json.loads(result.output)["balancer"]
    assert balancer["model"] == "simple"
    params = balancer["params"].keys()
    assert len(params) == 0
