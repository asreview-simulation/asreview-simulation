import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_triple_balancer_default_parameterization():
    runner = CliRunner()
    args = [
        "bal:triple",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    balancer = json.loads(result.output)["balancer"]
    assert balancer["abbr"] == "triple"
    params = balancer["params"].keys()
    assert "a" in params
    assert balancer["params"]["a"] == 2.155
    assert "alpha" in params
    assert balancer["params"]["alpha"] == 0.94
    assert "b" in params
    assert balancer["params"]["b"] == 0.789
    assert "beta" in params
    assert balancer["params"]["beta"] == 1.0
    assert "c" in params
    assert balancer["params"]["c"] == 0.835
    assert "gamma" in params
    assert balancer["params"]["gamma"] == 2.0
