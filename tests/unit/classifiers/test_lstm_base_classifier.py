import json
import pytest
from click.testing import CliRunner
from asreview_simulation.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_lstm_base
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_min
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
    expected_pairs = [
        ("backwards", False),
        ("batch_size", 32),
        ("class_weight", 30.0),
        ("dense_width", 128),
        ("dropout", 0.4),
        ("epochs", 35),
        ("optimizer", "rmsprop"),
        ("learn_rate", 1.0),
        ("lstm_out_width", 20),
        ("shuffle", False),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of classifier."
        assert classifier["params"][param] == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
