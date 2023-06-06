import json
from click.testing import CliRunner
from asreview_simulation import cli


def test_double_balancer_default_parameterization():
    runner = CliRunner()
    args = [
        "bal:double",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    balancer = json.loads(result.output)["balancer"]
    assert balancer["model"] == "double"
    params = balancer["params"].keys()
    assert "a" in params
    assert balancer["params"]["a"] == 2.155
    assert "alpha" in params
    assert balancer["params"]["alpha"] == 0.94
    assert "b" in params
    assert balancer["params"]["b"] == 0.789
    assert "beta" in params
    assert balancer["params"]["beta"] == 1.0
