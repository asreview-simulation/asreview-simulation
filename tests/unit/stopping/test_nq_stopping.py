import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_nq_stopping_default_parameterization():
    runner = CliRunner()
    args = [
        "stp-nq",
        "--n_queries",
        "25",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    stopping = json.loads(result.output)["stopping"]
    assert stopping["abbr"] == "nq"
    params = stopping["params"].keys()
    assert "n_queries" in params
    assert stopping["params"]["n_queries"] == 25
