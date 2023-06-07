import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_min_stopping_default_parameterization():
    runner = CliRunner()
    args = [
        "stp:min",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    stopping = json.loads(result.output)["stopping"]
    assert stopping["abbr"] == "min"
    params = stopping["params"].keys()
    assert len(params) == 0
