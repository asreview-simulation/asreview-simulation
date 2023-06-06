import json
from click.testing import CliRunner
from asreview_simulation import cli


def test_embeddding_idf_extractor_default_parameterization():
    runner = CliRunner()
    args = [
        "ext:embedding-idf",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    extractor = json.loads(result.output)["extractor"]
    assert extractor["model"] == "embedding-idf"
    params = extractor["params"].keys()
    assert len(params) == 0
