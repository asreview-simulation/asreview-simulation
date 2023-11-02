import json
import pytest
from click.testing import CliRunner
from asreview_simulation.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_embedding_lstm
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_min
def test_embedding_lstm_extractor_default_parameterization():
    runner = CliRunner()
    args = [
        "fex-embedding-lstm",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    extractor = json.loads(result.output)["extractor"]
    assert extractor["abbr"] == "embedding-lstm"
    params = extractor["params"].keys()

    expected_pairs = [
        ("embedding_fp", ""),
        ("loop_sequence", 1),
        ("max_sequence_length", 1000),
        ("num_words", 20000),
        ("padding", "post"),
        ("split_ta", 0),
        ("truncating", "post"),
        ("use_keywords", 0),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of 'fex-{extractor.abbr}'."
        assert extractor["params"][param] == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
