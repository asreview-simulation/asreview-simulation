import json
from click.testing import CliRunner
from asreview_simulation.cli import cli
import pytest


@pytest.mark.sam_random
@pytest.mark.fex_sbert
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_min
def test_sbert_extractor_default_parameterization():
    runner = CliRunner()
    args = [
        "fex-sbert",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    extractor = json.loads(result.output)["extractor"]
    assert extractor["abbr"] == "sbert"
    params = extractor["params"].keys()
    assert "transformer_model" in params
    assert extractor["params"]["transformer_model"] == "all-mpnet-base-v2"
