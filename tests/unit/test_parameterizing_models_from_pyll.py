import pytest
from asreview.models.balance.base import BaseModel as ASReviewBaseModelBal
from asreview.models.classifiers.base import BaseModel as ASReviewBaseModelCls
from asreview.models.feature_extraction.base import BaseModel as ASReviewBaseModelFex
from asreview.models.query.base import BaseModel as ASReviewBaseModelQry
from asreview_simulation.api import draw_sample
from asreview_simulation.api import get_abbrs
from asreview_simulation.api import get_pyll
from asreview_simulation.api.unwrapping import instantiate_unwrapped_model


@pytest.mark.parametrize("abbr", get_abbrs())
def test_parameterizing_models_from_pyll(abbr):
    if abbr[:3] in {"sam", "stp"}:
        pytest.skip(reason=f"ASReview doesn't have an equivalent model for models of type {abbr}")
    pyll = get_pyll(abbr)
    model = draw_sample(pyll)
    model_unwrapped = instantiate_unwrapped_model(model, random_state=12345)
    ASReviewBaseModel = {
        "bal": ASReviewBaseModelBal,
        "cls": ASReviewBaseModelCls,
        "fex": ASReviewBaseModelFex,
        "qry": ASReviewBaseModelQry,
    }[abbr[:3]]
    assert isinstance(model_unwrapped, ASReviewBaseModel)
