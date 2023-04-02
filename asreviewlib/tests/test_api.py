import asreviewlib
import inspect
import pytest


def list_members(pkg):
    r = list()
    members = inspect.getmembers(pkg)
    for name, value in members:
        if name.endswith('__'):
            continue
        r.append(f"{pkg.__name__}.{name}")
        if inspect.ismodule(value):
            r += list_members(value)
    return r


actual_members = list_members(asreviewlib)
expected_members = [
    'asreviewlib.balancers.BaseBalancer',
    'asreviewlib.balancers.DoubleBalancer',
    'asreviewlib.balancers.NoBalancer',
    'asreviewlib.balancers.TripleBalancer',
    'asreviewlib.balancers.UndersampleBalancer',
    'asreviewlib.balancers',
    'asreviewlib.BaseModel',
    'asreviewlib.classifiers.BaseClassifier',
    'asreviewlib.classifiers.LogisticClassifier',
    'asreviewlib.classifiers.LstmBaseClassifier',
    'asreviewlib.classifiers.LstmPoolClassifier',
    'asreviewlib.classifiers.NaiveBayesClassifier',
    'asreviewlib.classifiers.NN2LayerClassifier',
    'asreviewlib.classifiers.RandomForestClassifier',
    'asreviewlib.classifiers.SvmClassifier',
    'asreviewlib.classifiers',
    'asreviewlib.Data',
    'asreviewlib.demo_d.fun',
    'asreviewlib.demo_d',
    'asreviewlib.exceptions.ASReviewProjectExistsError',
    'asreviewlib.exceptions.ASReviewProjectNotFoundError',
    'asreviewlib.exceptions',
    'asreviewlib.extractors.BaseExtractor',
    'asreviewlib.extractors.Doc2VecExtractor',
    'asreviewlib.extractors.EmbeddingIdfExtractor',
    'asreviewlib.extractors.EmbeddingLstmExtractor',
    'asreviewlib.extractors.SbertExtractor',
    'asreviewlib.extractors.TfidfExtractor',
    'asreviewlib.extractors',
    'asreviewlib.list_balancers',
    'asreviewlib.list_classifiers',
    'asreviewlib.list_extractors',
    'asreviewlib.list_projects',
    'asreviewlib.list_queriers',
    'asreviewlib.list_readers',
    'asreviewlib.list_writers',
    'asreviewlib.Project',
    'asreviewlib.queriers.BaseQuerier',
    'asreviewlib.queriers.ClusterQuerier',
    'asreviewlib.queriers.MaxQuerier',
    'asreviewlib.queriers.MaxRandomQuerier',
    'asreviewlib.queriers.MaxUncertaintyQuerier',
    'asreviewlib.queriers.MixedQuerier',
    'asreviewlib.queriers.RandomQuerier',
    'asreviewlib.queriers.UncertaintyQuerier',
    'asreviewlib.queriers',
    'asreviewlib.readers.CsvReader',
    'asreviewlib.readers.RisReader',
    'asreviewlib.readers.TsvReader',
    'asreviewlib.readers.XlsReader',
    'asreviewlib.readers',
    'asreviewlib.state.create_database',
    'asreviewlib.state.create_event',
    'asreviewlib.state.create_record',
    'asreviewlib.state.delete_database',
    'asreviewlib.state.delete_event',
    'asreviewlib.state.delete_record',
    'asreviewlib.state.read_database',
    'asreviewlib.state.read_event',
    'asreviewlib.state.read_record',
    'asreviewlib.state.update_database',
    'asreviewlib.state.update_event',
    'asreviewlib.state.update_record',
    'asreviewlib.state',
    'asreviewlib.writers.CsvWriter',
    'asreviewlib.writers.RisWriter',
    'asreviewlib.writers.TsvWriter',
    'asreviewlib.writers.XlsWriter',
    'asreviewlib.writers'
]


@pytest.mark.parametrize("expected_member", expected_members)
def test_api_expected_members_present(expected_member):
    assert expected_member in actual_members, f"Didn't find expected member {expected_member} in the API."


@pytest.mark.parametrize("actual_member", actual_members)
def test_api_no_unintentional_exports(actual_member):
    assert actual_member in expected_members, f"Found unexpected member {actual_member} in the API."
