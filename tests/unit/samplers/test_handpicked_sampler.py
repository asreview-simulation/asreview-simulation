import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_handpicked_sampler_default_parameterization():
    runner = CliRunner()
    args = [
        "sam:handpicked",
        "1,2,3",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    sampler = json.loads(result.output)["sampler"]
    assert sampler["abbr"] == "handpicked"
    params = sampler["params"].keys()
    assert "ids" in params
    assert sampler["params"]["ids"] == [1, 2, 3]
