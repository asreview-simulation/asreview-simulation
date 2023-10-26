import json
import pytest
from click.testing import CliRunner
from asreview_simulation.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_min
def test_tfidf_extractor_default_parameterization():
    runner = CliRunner()
    args = [
        "fex-tfidf",
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
