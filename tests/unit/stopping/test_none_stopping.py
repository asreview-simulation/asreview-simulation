import json
from click.testing import CliRunner
from asreview_simulation import cli


def test_none_stopping_default_parameterization():
    runner = CliRunner()
    args = [
        "stp:none",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    stopping = json.loads(result.output)["stopping"]
    assert stopping["model"] == "none"
    params = stopping["params"].keys()
    assert len(params) == 0
