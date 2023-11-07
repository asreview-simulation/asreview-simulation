import json
import pytest
from click.testing import CliRunner
from asreview_simulation._private.cli.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nn_2_layer
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_nn_2_layer_classifier_default_parameterization():
    runner = CliRunner()
    args = [
        "cls-nn-2-layer",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["classifier"]
    assert classifier["abbr"] == "cls-nn-2-layer"
    params = classifier["params"].keys()
    expected_pairs = [
        ("batch_size", 32),
        ("class_weight", 30.0),
        ("dense_width", 128),
        ("epochs", 35),
        ("learn_rate", 1.0),
        ("optimizer", "rmsprop"),
        ("regularization", 0.01),
        ("shuffle", False),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of classifier."
        actual_value = classifier["params"][param]
        assert type(actual_value) == type(expected_value), f"Unexpected type for key '{param}'"
        assert actual_value == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
