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
   'asreview.BaseModel',
   'asreview.Data',
   'asreview.balancers',
   'asreview.balancers.BaseBalancer',
   'asreview.balancers.DoubleBalancer',
   'asreview.balancers.SimpleBalancer',
   'asreview.balancers.TripleBalancer',
   'asreview.balancers.UndersampleBalancer',
   'asreview.balancers.list_balancers',
   'asreview.classifiers',
   'asreview.classifiers.BaseClassifier',
   'asreview.classifiers.LogisticClassifier',
   'asreview.classifiers.LstmBaseClassifier',
   'asreview.classifiers.LstmPoolClassifier',
   'asreview.classifiers.NN2LayerClassifier',
   'asreview.classifiers.NaiveBayesClassifier',
   'asreview.classifiers.RandomForestClassifier',
   'asreview.classifiers.SVMClassifier',
   'asreview.classifiers.list_classifiers',
   'asreview.config',
   'asreview.config.ASCII_LOGO',
   'asreview.config.COLUMN_DEFINITIONS',
   'asreview.config.DEFAULT_BALANCER',
   'asreview.config.DEFAULT_CLASSIFIER',
   'asreview.config.DEFAULT_EXTRACTOR',
   'asreview.config.DEFAULT_N_INSTANCES',
   'asreview.config.DEFAULT_QUERIER',
   'asreview.config.EMAIL_ADDRESS',
   'asreview.config.GITHUB_PAGE',
   'asreview.config.KERAS_MODELS',
   'asreview.config.LABEL_NA',
   'asreview.entrypoints',
   'asreview.entrypoints.AlgorithmsEntrypoint',
   'asreview.entrypoints.BaseEntrypoint',
   'asreview.entrypoints.LabEntrypoint',
   'asreview.entrypoints.SimulateEntrypoint',
   'asreview.entrypoints.StateInspectEntrypoint',
   'asreview.entrypoints.list_entrypoints',
   'asreview.exceptions',
   'asreview.exceptions.ASReviewProjectExistsError',
   'asreview.exceptions.ASReviewProjectNotFoundError',
   'asreview.extractors',
   'asreview.extractors.BaseExtractor',
   'asreview.extractors.Doc2VecExtractor',
   'asreview.extractors.EmbeddingIdfExtractor',
   'asreview.extractors.EmbeddingLstmExtractor',
   'asreview.extractors.SbertExtractor',
   'asreview.extractors.TfidfExtractor',
   'asreview.extractors.list_extractors',
   'asreview.projects',
   'asreview.projects.Project',
   'asreview.projects.list_projects',
   'asreview.queriers',
   'asreview.queriers.BaseQuerier',
   'asreview.queriers.ClusterQuerier',
   'asreview.queriers.MaxQuerier',
   'asreview.queriers.MaxRandomQuerier',
   'asreview.queriers.MaxUncertaintyQuerier',
   'asreview.queriers.MixedQuerier',
   'asreview.queriers.RandomQuerier',
   'asreview.queriers.UncertaintyQuerier',
   'asreview.queriers.list_queriers',
   'asreview.readers',
   'asreview.readers.CSVReader',
   'asreview.readers.RISReader',
   'asreview.readers.TSVReader',
   'asreview.readers.XLSReader',
   'asreview.readers.list_readers',
   'asreview.writers',
   'asreview.writers.CSVWriter',
   'asreview.writers.RISWriter',
   'asreview.writers.TSVWriter',
   'asreview.writers.XLSWriter',
   'asreview.writers.list_writers'
]


@pytest.mark.parametrize("expected_member", expected_members)
def test_api_expected_members_present(expected_member):
    assert expected_member in actual_members, f"Didn't find expected member {expected_member} in the API."


@pytest.mark.parametrize("actual_member", actual_members)
def test_api_no_unintentional_exports(actual_member):
    assert actual_member in expected_members, f"Found unexpected member {actual_member} in the API."
