import asreview
import inspect


def test_api():

    # modules
    modules = [
        asreview.balancers,
        asreview.classifiers,
        asreview.entrypoints,
        asreview.extractors,
        asreview.queriers
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
        asreview.extractors.BaseExtractor,
        asreview.extractors.Doc2VecExtractor,
        asreview.extractors.EmbeddingIdfExtractor,
        asreview.extractors.EmbeddingLstmExtractor,
        asreview.extractors.SbertExtractor,
        asreview.extractors.TfidfExtractor,
        asreview.queriers.BaseQuerier,
        asreview.queriers.ClusterQuerier,
        asreview.queriers.MaxQuerier,
        asreview.queriers.MaxRandomQuerier,
        asreview.queriers.MaxUncertaintyQuerier,
        asreview.queriers.MixedQuerier,
        asreview.queriers.RandomQuerier,
        asreview.queriers.UncertaintyQuerier,
        asreview.SomeException,
        asreview.Project
    ]
    for cls in classes:
        assert inspect.isclass(cls)
