import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_n_stopping_default_parameterization():
    runner = CliRunner()
    args = [
        "stp:n",
        "25",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    stopping = json.loads(result.output)["stopping"]
    assert stopping["abbr"] == "n"
    params = stopping["params"].keys()
    assert "n" in params
    assert stopping["params"]["n"] == 25
