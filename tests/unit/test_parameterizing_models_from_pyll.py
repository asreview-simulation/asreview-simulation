import pytest
from asreview.models.base import BaseModel as ASReviewBaseModel
from asreview_simulation.api import get_pyll
from asreview_simulation.api import draw_sample
from asreview_simulation.api.unwrapping import instantiate_unwrapped_model


def get_abbrs():
    return [
        "bal-double",
        "bal-simple",
        "bal-undersample",
        "cls-logistic",
        "cls-lstm-base",
        "cls-lstm-pool",
        "cls-nb",
        "cls-nn-2-layer",
        "cls-rf",
        "cls-svm",
        "fex-doc2vec",
        "fex-embedding-idf",
        "fex-embedding-lstm",
        "fex-sbert",
        "fex-tfidf",
        "qry-cluster",
        "qry-max",
        # "qry-max-random",
        # "qry-max-uncertainty",
        "qry-random",
        "qry-uncertainty",
    ]


@pytest.mark.parametrize("abbr", get_abbrs())
def test_parameterizing_models_from_pyll(abbr):
    pyll = get_pyll(abbr)
    model = draw_sample(pyll)
    model_unwrapped = instantiate_unwrapped_model(model, random_state=12345)
    assert isinstance(model_unwrapped, ASReviewBaseModel)
