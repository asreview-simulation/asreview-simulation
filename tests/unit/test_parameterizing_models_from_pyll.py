import pytest
from asreview.models.base import BaseModel
from asreview_simulation.api import draw_sample
from asreview_simulation.api import get_abbrs
from asreview_simulation.api import get_pyll
from asreview_simulation.api.unwrapping import instantiate_unwrapped_model


@pytest.mark.parametrize("abbr", [model for model in get_abbrs() if model.startswith("bal")])
def test_parameterizing_bal_models_from_pyll(abbr):
    pyll = {"bal": get_pyll(abbr)}
    drawn = draw_sample(pyll)
    bal = drawn["bal"]
    model_unwrapped = instantiate_unwrapped_model(bal, random_state=12345)
    assert isinstance(model_unwrapped, BaseModel)


@pytest.mark.parametrize("abbr", [model for model in get_abbrs() if model.startswith("cls")])
def test_parameterizing_cls_models_from_pyll(abbr):
    pyll = {"cls": get_pyll(abbr)}
    drawn = draw_sample(pyll)
    cls = drawn["cls"]
    model_unwrapped = instantiate_unwrapped_model(cls, random_state=12345)
    assert isinstance(model_unwrapped, BaseModel)


@pytest.mark.parametrize("abbr", [model for model in get_abbrs() if model.startswith("fex")])
def test_parameterizing_fex_models_from_pyll(abbr):
    pyll = {"fex": get_pyll(abbr)}
    drawn = draw_sample(pyll)
    fex = drawn["fex"]
    model_unwrapped = instantiate_unwrapped_model(fex, random_state=12345)
    assert isinstance(model_unwrapped, BaseModel)


@pytest.mark.parametrize("abbr", [model for model in get_abbrs() if model.startswith("qry")])
def test_parameterizing_qry_models_from_pyll(abbr):
    pyll = {"qry": get_pyll(abbr)}
    drawn = draw_sample(pyll)
    qry = drawn["qry"]
    model_unwrapped = instantiate_unwrapped_model(qry, random_state=12345)
    assert isinstance(model_unwrapped, BaseModel)
