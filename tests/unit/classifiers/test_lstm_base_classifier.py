import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_lstm_base_classifier_default_parameterization(tmp_path):
    runner = CliRunner()
    args = [
        "cls-lstm-base",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["classifier"]
    assert classifier["abbr"] == "lstm-base"
    params = classifier["params"].keys()
    assert len(params) == 0
