import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_uncertainty_querier_default_parameterization():
    runner = CliRunner()
    args = [
        "qry:uncertainty",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    querier = json.loads(result.output)["querier"]
    assert querier["abbr"] == "uncertainty"
    params = querier["params"].keys()
    assert len(params) == 0
