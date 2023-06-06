import json
from click.testing import CliRunner
from asreview_simulation import cli


def test_sbert_extractor_default_parameterization():
    runner = CliRunner()
    args = [
        "ext:sbert",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    extractor = json.loads(result.output)["extractor"]
    assert extractor["model"] == "sbert"
    params = extractor["params"].keys()
    assert "transformer_model" in params
    assert extractor["params"]["transformer_model"] == "all-mpnet-base-v2"
