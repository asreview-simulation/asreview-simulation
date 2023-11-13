from asreview_simulation._private.lib.model_config import ModelConfig


def get_stp_nq_config():
    abbr = "stp-nq"
    params = {
        "n_queries": None,
    }
    return ModelConfig(abbr=abbr, params=params)
