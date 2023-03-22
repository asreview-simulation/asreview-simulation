import asreview
import inspect


def test_api():

    # modules
    modules = [
        asreview.balancers,
        asreview.classifiers,
        asreview.entrypoints,
        asreview.exceptions,
        asreview.extractors,
        asreview.projects,
        asreview.queriers,
        asreview.readers,
        asreview.writers,
        asreview.config
    ]
    for m in modules:
        assert inspect.ismodule(m)

    # classes
    classes = [
        asreview.balancers.BaseBalancer,
        asreview.balancers.DoubleBalancer,
        asreview.balancers.SimpleBalancer,
        asreview.balancers.TripleBalancer,
        asreview.balancers.UndersampleBalancer,
        asreview.classifiers.BaseClassifier,
        asreview.classifiers.LogisticClassifier,
        asreview.classifiers.LstmBaseClassifier,
        asreview.classifiers.LstmPoolClassifier,
        asreview.classifiers.NaiveBayesClassifier,
        asreview.classifiers.NN2LayerClassifier,
        asreview.classifiers.RandomForestClassifier,
        asreview.classifiers.SVMClassifier,
        asreview.entrypoints.AlgorithmsEntrypoint,
        asreview.entrypoints.BaseEntrypoint,
        asreview.entrypoints.LabEntrypoint,
        asreview.entrypoints.SimulateEntrypoint,
        asreview.entrypoints.StateInspectEntrypoint,
        asreview.exceptions.ASReviewProjectExistsError,
        asreview.exceptions.ASReviewProjectNotFoundError,
        asreview.extractors.BaseExtractor,
        asreview.extractors.Doc2VecExtractor,
        asreview.extractors.EmbeddingIdfExtractor,
        asreview.extractors.EmbeddingLstmExtractor,
        asreview.extractors.SbertExtractor,
        asreview.extractors.TfidfExtractor,
        asreview.projects.Project,
        asreview.readers.CSVReader,
        asreview.readers.RISReader,
        asreview.readers.TSVReader,
        asreview.readers.XLSReader,
        asreview.writers.CSVWriter,
        asreview.writers.RISWriter,
        asreview.writers.TSVWriter,
        asreview.writers.XLSWriter,
        asreview.queriers.BaseQuerier,
        asreview.queriers.ClusterQuerier,
        asreview.queriers.MaxQuerier,
        asreview.queriers.MaxRandomQuerier,
        asreview.queriers.MaxUncertaintyQuerier,
        asreview.queriers.MixedQuerier,
        asreview.queriers.RandomQuerier,
        asreview.queriers.UncertaintyQuerier,
        asreview.BaseModel,
        asreview.Data
    ]
    for cls in classes:
        assert inspect.isclass(cls)

    # functions
    functions = [
        asreview.balancers.list_balancers,
        asreview.classifiers.list_classifiers,
        asreview.entrypoints.list_entrypoints,
        asreview.extractors.list_extractors,
        asreview.projects.list_projects,
        asreview.readers.list_readers,
        asreview.writers.list_writers,
        asreview.queriers.list_queriers
    ]
    for fun in functions:
        assert inspect.isfunction(fun)
