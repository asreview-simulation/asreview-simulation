from asreview.data import ASReviewData
import numpy
from asreview_simulation._private.model_configs import ModelConfigs
from asreview_simulation._private.unwrap_prior_sampling_vars import unwrap_prior_sampling_vars
from asreview_simulation._private.unwrap_stopping_vars import unwrap_stopping_vars
from asreview_simulation._private.unwrap import unwrap


def remove_abstraction(models: ModelConfigs, as_data: ASReviewData, seed: int = None):

    # asreview's query model does not expect n_instances as part
    # of the models.querier.params dict but as a separate variable
    n_instances = models.querier.params.pop("n_instances", 1)

    # if the extractor has a parameter named 'embedding', remove it
    # from models.extractor.params and make it a separate variable
    embedding_fp = models.extractor.params.pop("embedding", None)

    # Initialize the random state
    random_state = numpy.random.RandomState(seed)

    # assign model parameterizations using the configuration from 'models'
    classifier = unwrap(models.classifier, random_state=random_state)
    querier = unwrap(models.querier, random_state=random_state)
    balancer = unwrap(models.balancer, random_state=random_state)
    extractor = unwrap(models.extractor, random_state=random_state)

    if models.classifier.abbr in ["cls-lstm-base", "cls-lstm-pool"]:
        classifier.embedding_matrix = extractor.get_embedding_matrix(as_data.texts, embedding_fp)

    n_papers = None
    stop_if = unwrap_stopping_vars(models, as_data, n_instances)
    prior_indices, n_prior_included, n_prior_excluded, init_seed = unwrap_prior_sampling_vars(models, as_data)

    return {
        "model": classifier,
        "query_model": querier,
        "balance_model": balancer,
        "feature_model": extractor,
        "n_papers": n_papers,
        "n_instances": n_instances,
        "stop_if": stop_if,
        "prior_indices": prior_indices,
        "n_prior_included": n_prior_included,
        "n_prior_excluded": n_prior_excluded,
        "init_seed": init_seed
    }
