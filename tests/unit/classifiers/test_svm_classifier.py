import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_svm_classifier_default_parameterization():
    runner = CliRunner()
    args = [
        "cls:svm",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["classifier"]
    assert classifier["abbr"] == "svm"
    params = classifier["params"].keys()
    assert "C" in params
    assert classifier["params"]["C"] == 15.4
    assert "class_weight" in params
    assert classifier["params"]["class_weight"] == 0.249
    assert "gamma" in params
    assert classifier["params"]["gamma"] == "auto"
    assert "kernel" in params
    assert classifier["params"]["kernel"] == "linear"
