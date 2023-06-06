import json
from click.testing import CliRunner
from asreview_simulation import cli


def test_logistic_classifier_default_parameterization():
    runner = CliRunner()
    args = [
        "cls:logistic",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["classifier"]
    assert classifier["model"] == "logistic"
    params = classifier["params"].keys()
    assert "c" in params
    assert classifier["params"]["c"] == 1.0
    assert "class_weight" in params
    assert classifier["params"]["class_weight"] == 1.0
