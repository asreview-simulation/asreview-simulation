import json
import pytest
from click.testing import CliRunner
from asreview_simulation._private.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_embedding_lstm
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_embedding_lstm_extractor_default_parameterization():
    runner = CliRunner()
    args = [
        "fex-embedding-lstm",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    extractor = json.loads(result.output)["fex"]
    assert extractor["abbr"] == "fex-embedding-lstm"
    params = extractor["params"].keys()

    expected_pairs = [
        ("embedding", None),
        ("loop_sequence", 1),
        ("max_sequence_length", 1000),
        ("num_words", 20000),
        ("padding", "post"),
        ("split_ta", False),
        ("truncating", "post"),
        ("use_keywords", False),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of feature extractor."
        actual_value = extractor["params"][param]
        assert type(actual_value) == type(expected_value), f"Unexpected type for key '{param}'"
        assert actual_value == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
