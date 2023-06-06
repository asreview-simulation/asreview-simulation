import json
from click.testing import CliRunner
from asreview_simulation import cli


def test_lstm_base_classifier_default_parameterization(tmp_path):
    features = tmp_path / "features.npz"
    features.touch()
    runner = CliRunner()
    args = [
        "cls:lstm-base",
        str(features),
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["classifier"]
    assert classifier["model"] == "lstm-base"
    params = classifier["params"].keys()
    assert len(params) == 0
