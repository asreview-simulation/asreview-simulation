import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_nn_2_layer_classifier_default_parameterization():
    runner = CliRunner()
    args = [
        "cls:nn-2-layer",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["classifier"]
    assert classifier["abbr"] == "nn-2-layer"
    params = classifier["params"].keys()
    assert "batch_size" in params
    assert classifier["params"]["batch_size"] == 32
    assert "dense_width" in params
    assert classifier["params"]["dense_width"] == 128
    assert "epochs" in params
    assert classifier["params"]["epochs"] == 35
    assert "learn_rate" in params
    assert classifier["params"]["learn_rate"] == 1.0
    assert "optimizer" in params
    assert classifier["params"]["optimizer"] == "rmsprop"
    assert "regularization" in params
    assert classifier["params"]["regularization"] == 0.01
    assert "shuffle" in params
    assert classifier["params"]["shuffle"] is False
