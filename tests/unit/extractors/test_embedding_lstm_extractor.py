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
    assert len(params) == 7
    assert "embedding_fp" in params
    assert extractor["params"]["embedding_fp"] is None
    assert "loop_sequence" in params
    assert extractor["params"]["loop_sequence"] == 1
    assert "max_sequence_length" in params
    assert extractor["params"]["max_sequence_length"] == 1000
    assert "n_jobs" in params
    assert extractor["params"]["n_jobs"] == 1
    assert "num_words" in params
    assert extractor["params"]["num_words"] == 20000
    assert "padding" in params
    assert extractor["params"]["padding"] == "post"
    assert "truncating" in params
    assert extractor["params"]["truncating"] == "post"
