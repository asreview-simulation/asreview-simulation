import asreview
import inspect
import pytest


def list_members(pkg):
    r = list()
    members = inspect.getmembers(pkg)
    for name, value in members:
        if inspect.isbuiltin(value) or name.endswith('__'):
            continue
        r.append(f"{pkg.__name__}.{name}")
        if inspect.ismodule(value):
            r += list_members(value)
    return r


actual_members = list_members(asreview)
expected_members = [
   'asreview.balancers.BaseBalancer',
   'asreview.balancers.DoubleBalancer',
   'asreview.balancers.list_balancers',
   'asreview.balancers.SimpleBalancer',
   'asreview.balancers.TripleBalancer',
   'asreview.balancers.UndersampleBalancer',
   'asreview.balancers',
   'asreview.BaseModel',
   'asreview.classifiers.BaseClassifier',
   'asreview.classifiers.list_classifiers',
   'asreview.classifiers.LogisticClassifier',
   'asreview.classifiers.LstmBaseClassifier',
   'asreview.classifiers.LstmPoolClassifier',
   'asreview.classifiers.NaiveBayesClassifier',
   'asreview.classifiers.NN2LayerClassifier',
   'asreview.classifiers.RandomForestClassifier',
   'asreview.classifiers.SVMClassifier',
   'asreview.classifiers',
   'asreview.Data',
   'asreview.exceptions.ASReviewProjectExistsError',
   'asreview.exceptions.ASReviewProjectNotFoundError',
   'asreview.exceptions',
   'asreview.extractors.BaseExtractor',
   'asreview.extractors.Doc2VecExtractor',
   'asreview.extractors.EmbeddingIdfExtractor',
   'asreview.extractors.EmbeddingLstmExtractor',
   'asreview.extractors.list_extractors',
   'asreview.extractors.SbertExtractor',
   'asreview.extractors.TfidfExtractor',
   'asreview.extractors',
   'asreview.Project',
   'asreview.projects.list_projects',
   'asreview.projects',
   'asreview.queriers.BaseQuerier',
   'asreview.queriers.ClusterQuerier',
   'asreview.queriers.list_queriers',
   'asreview.queriers.MaxQuerier',
   'asreview.queriers.MaxRandomQuerier',
   'asreview.queriers.MaxUncertaintyQuerier',
   'asreview.queriers.MixedQuerier',
   'asreview.queriers.RandomQuerier',
   'asreview.queriers.UncertaintyQuerier',
   'asreview.queriers',
   'asreview.readers.CSVReader',
   'asreview.readers.list_readers',
   'asreview.readers.RISReader',
   'asreview.readers.TSVReader',
   'asreview.readers.XLSReader',
   'asreview.readers',
   'asreview.writers.CSVWriter',
   'asreview.writers.list_writers',
   'asreview.writers.RISWriter',
   'asreview.writers.TSVWriter',
   'asreview.writers.XLSWriter',
   'asreview.writers'
]


@pytest.mark.parametrize("expected_member", expected_members)
def test_api_expected_members_present(expected_member):
    assert expected_member in actual_members, f"Didn't find expected member {expected_member} in the API."


@pytest.mark.parametrize("actual_member", actual_members)
def test_api_no_unintentional_exports(actual_member):
    assert actual_member in expected_members, f"Found unexpected member {actual_member} in the API."
