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
        asreview.classifiers.BaseClassifier,
        asreview.classifiers.NaiveBayesClassifier,
        asreview.entrypoints.AlgorithmsEntrypoint,
        asreview.entrypoints.BaseEntrypoint,
        asreview.entrypoints.LabEntrypoint,
        asreview.entrypoints.SimulateEntrypoint,
        asreview.entrypoints.StateInspectEntrypoint,
        asreview.extractors.BaseExtractor,
        asreview.extractors.TfidfExtractor,
        asreview.queriers.BaseQuerier,
        asreview.queriers.MaxQuerier,
        asreview.SomeException,
        asreview.Project
    ]
    for cls in classes:
        assert inspect.isclass(cls)
