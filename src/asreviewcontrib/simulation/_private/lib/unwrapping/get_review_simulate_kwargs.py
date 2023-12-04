import numpy
from asreview.data import ASReviewData
from asreviewcontrib.simulation._private.lib.all_model_config import AllModelConfig
from asreviewcontrib.simulation._private.lib.unwrapping.instantiate_unwrapped_model import instantiate_unwrapped_model
from asreviewcontrib.simulation._private.lib.unwrapping.unwrap_prior_sampling_vars import unwrap_prior_sampling_vars
from asreviewcontrib.simulation._private.lib.unwrapping.unwrap_stopping_vars import unwrap_stopping_vars


def get_review_simulate_kwargs(models: AllModelConfig, as_data: ASReviewData, seed: int = None) -> dict:
    # asreview's query model does not expect n_instances as part
    # of the models.querier.params dict but as a separate variable
    n_instances = models.qry.params.pop("n_instances", 1)

    # if the extractor has a parameter named 'embedding', remove it
    # from models.extractor.params and make it a separate variable
    embedding_fp = models.fex.params.pop("embedding", None)

    # Initialize the random state
    random_state = numpy.random.RandomState(seed)

    # assign model parameterizations using the configuration from 'models'
    classifier = instantiate_unwrapped_model(models.cls, random_state=random_state)
    querier = instantiate_unwrapped_model(models.qry, random_state=random_state)
    balancer = instantiate_unwrapped_model(models.bal, random_state=random_state)
    extractor = instantiate_unwrapped_model(models.fex, random_state=random_state)

    if models.cls.abbr in ["cls-lstm-base", "cls-lstm-pool"]:
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
        "init_seed": init_seed,
    }
