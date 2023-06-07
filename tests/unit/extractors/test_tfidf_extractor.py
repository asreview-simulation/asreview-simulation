import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_tfidf_extractor_default_parameterization():
    runner = CliRunner()
    args = [
        "fex:tfidf",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    extractor = json.loads(result.output)["extractor"]
    assert extractor["abbr"] == "tfidf"
    params = extractor["params"].keys()
    assert "ngram_max" in params
    assert extractor["params"]["ngram_max"] == 1
    assert "stop_words" in params
    assert extractor["params"]["stop_words"] == "english"
