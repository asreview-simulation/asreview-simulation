from asreview.data import ASReviewData
from numpy.random import RandomState
from asreview_simulation._private.models import Models
from asreview_simulation._private.unwrapping.assign_vars_for_prior_sampling import assign_vars_for_prior_sampling
from asreview_simulation._private.unwrapping.assign_vars_for_stopping import assign_vars_for_stopping
from asreview_simulation._private.unwrapping.map_parameterization import map_parameterization


def remove_abstraction(models: Models, as_data: ASReviewData, random_state: RandomState):
    # asreview's query model does not expect n_instances as part
    # of the models.querier.params dict but as a separate variable
    n_instances = models.querier.params.pop("n_instances", 1)

    # if the extractor has a parameter named 'embedding', remove it
    # from models.extractor.params and make it a separate variable
    embedding_fp = models.extractor.params.pop("embedding", None)

    # assign model parameterizations using the data from obj
    extractor = map_parameterization(models.extractor, random_state=random_state)
    classifier = map_parameterization(models.classifier, random_state=random_state)
    querier = map_parameterization(models.querier, random_state=random_state)
    balancer = map_parameterization(models.balancer, random_state=random_state)

    if models.classifier.abbr in ["lstm-base", "lstm-pool"]:
        classifier.embedding_matrix = extractor.get_embedding_matrix(as_data.texts, embedding_fp)

    n_papers = None
    stop_if = assign_vars_for_stopping(models, as_data, n_instances)
    prior_indices, n_prior_included, n_prior_excluded, init_seed = assign_vars_for_prior_sampling(models, as_data)

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
