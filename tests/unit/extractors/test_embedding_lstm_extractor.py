import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_embeddding_lstm_extractor_default_parameterization():
    runner = CliRunner()
    args = [
        "fex:embedding-lstm",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    extractor = json.loads(result.output)["extractor"]
    assert extractor["abbr"] == "embedding-lstm"
    params = extractor["params"].keys()
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
