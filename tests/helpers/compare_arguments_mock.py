from pathlib import Path
from asreview.data import ASReviewData
from asreview.models.base import BaseModel
from asreview.project import ASReviewProject
from pandas.testing import assert_frame_equal


def compare_arguments_mock(args1, kwargs1, args2, kwargs2, tmpdir):
    assert isinstance(
        args1[0], ASReviewData
    ), "Expected SimulateReview's first argument to be of type 'ASReviewData' (asreview simulate cli)."
    assert isinstance(
        args2[0], ASReviewData
    ), "Expected SimulateReview's first argument to be of type 'ASReviewData' (asreview simulation start cli)."
    assert_frame_equal(args1[0].df, args2[0].df), "Expected .df member of ASReviewData instances to be equal."
    assert kwargs1.keys() == kwargs2.keys(), "Expected SimulateReview to be called with the same keyword arguments."
    for (k1, v1), (k2, v2) in zip(kwargs1.items(), kwargs2.items()):
        assert type(v1) == type(v2), f"Expected type of SimulateReview's keyword argument '{k1}' to be equal."
        if isinstance(v1, ASReviewProject):
            assert v1.project_id == "simulate"
            assert v2.project_id == "simulation"
            assert v1.project_path == Path(tmpdir) / "simulate.asreview.tmp"
            assert v2.project_path == Path(tmpdir) / "simulation.asreview.tmp"
            assert v1.config["version"] == v2.config["version"]
            assert v1.config["mode"] == v2.config["mode"]
            assert v1.config["authors"] == v2.config["authors"]
            assert v1.config["reviews"] == v2.config["reviews"]
            assert v1.config["feature_matrices"] == v2.config["feature_matrices"]
            assert v1.config["dataset_path"] == v2.config["dataset_path"]
        elif isinstance(v1, BaseModel):
            assert v1.param == v2.param, "Expected model parameterization to be equal."
        else:
            assert v1 == v2, f"Expected SimulateReview's keyword argument '{k1}' to be equal."
