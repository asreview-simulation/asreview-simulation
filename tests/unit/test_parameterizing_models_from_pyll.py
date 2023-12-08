import pytest
from asreview.models.base import BaseModel
from asreviewcontrib.simulation.api import draw_sample
from asreviewcontrib.simulation.api import get_abbrs
from asreviewcontrib.simulation.api import get_pyll
from asreviewcontrib.simulation.api.unwrapping import instantiate_unwrapped_model


@pytest.mark.parametrize("abbr", [model for model in get_abbrs() if model.startswith("bal")])
def test_parameterizing_bal_models_from_pyll(abbr):
    pyll = {"bal": get_pyll(abbr)}
    drawn = draw_sample(pyll)
    bal = drawn["bal"]
    model_unwrapped = instantiate_unwrapped_model(bal, random_state=12345)
    assert isinstance(model_unwrapped, BaseModel)


@pytest.mark.parametrize("abbr", [model for model in get_abbrs() if model.startswith("clr")])
def test_parameterizing_clr_models_from_pyll(abbr):
    pyll = {"clr": get_pyll(abbr)}
    drawn = draw_sample(pyll)
    clr = drawn["clr"]
    model_unwrapped = instantiate_unwrapped_model(clr, random_state=12345)
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
