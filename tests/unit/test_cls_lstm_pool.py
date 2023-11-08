import json
import pytest
from click.testing import CliRunner
from asreview_simulation._private.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_lstm_pool
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_lstm_pool_classifier_default_parameterization(tmp_path):
    runner = CliRunner()
    args = [
        "cls-lstm-pool",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["cls"]
    assert classifier["abbr"] == "cls-lstm-pool"
    params = classifier["params"].keys()
    expected_pairs = [
        ("batch_size", 32),
        ("class_weight", 30.0),
        ("dropout", 0.4),
        ("epochs", 35),
        ("forward", False),
        ("learn_rate", 1.0),
        ("lstm_out_width", 20),
        ("lstm_pool_size", 128),
        ("optimizer", "rmsprop"),
        ("shuffle", False),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of classifier."
        actual_value = classifier["params"][param]
        assert type(actual_value) == type(expected_value), f"Unexpected type for key '{param}'"
        assert actual_value == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
