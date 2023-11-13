from asreview_simulation._private.lib.bal.bal_double_unwrap import instantiate_unwrapped_bal_double
from asreview_simulation._private.lib.bal.bal_simple_unwrap import instantiate_unwrapped_bal_simple
from asreview_simulation._private.lib.bal.bal_undersample_unwrap import instantiate_unwrapped_bal_undersample
from asreview_simulation._private.lib.cls.cls_logistic_unwrap import instantiate_unwrapped_cls_logistic
from asreview_simulation._private.lib.cls.cls_lstm_base_unwrap import instantiate_unwrapped_cls_lstm_base
from asreview_simulation._private.lib.cls.cls_lstm_pool_unwrap import instantiate_unwrapped_cls_lstm_pool
from asreview_simulation._private.lib.cls.cls_nb_unwrap import instantiate_unwrapped_cls_nb
from asreview_simulation._private.lib.cls.cls_nn_2_layer_unwrap import instantiate_unwrapped_cls_nn_2_layer
from asreview_simulation._private.lib.cls.cls_rf_unwrap import instantiate_unwrapped_cls_rf
from asreview_simulation._private.lib.cls.cls_svm_unwrap import instantiate_unwrapped_cls_svm
from asreview_simulation._private.lib.fex.fex_doc2vec_unwrap import instantiate_unwrapped_fex_doc2vec
from asreview_simulation._private.lib.fex.fex_embedding_idf_unwrap import instantiate_unwrapped_fex_embedding_idf
from asreview_simulation._private.lib.fex.fex_embedding_lstm_unwrap import instantiate_unwrapped_fex_embedding_lstm
from asreview_simulation._private.lib.fex.fex_sbert_unwrap import instantiate_unwrapped_fex_sbert
from asreview_simulation._private.lib.fex.fex_tfidf_unwrap import instantiate_unwrapped_fex_tfidf
from asreview_simulation._private.lib.model_config import ModelConfig
from asreview_simulation._private.lib.qry.qry_cluster_unwrap import instantiate_unwrapped_qry_cluster
from asreview_simulation._private.lib.qry.qry_max_random_unwrap import instantiate_unwrapped_qry_max_random
from asreview_simulation._private.lib.qry.qry_max_uncertainty_unwrap import instantiate_unwrapped_qry_max_uncertainty
from asreview_simulation._private.lib.qry.qry_max_unwrap import instantiate_unwrapped_qry_max
from asreview_simulation._private.lib.qry.qry_random_unwrap import instantiate_unwrapped_qry_random
from asreview_simulation._private.lib.qry.qry_uncertainty_unwrap import instantiate_unwrapped_qry_uncertainty


def instantiate_unwrapped_model(model: ModelConfig, random_state):
    assert isinstance(model, ModelConfig), "Input argument 'model' needs to be an instance of ModelConfig"
    mapping = {
        "bal-double": instantiate_unwrapped_bal_double,
        "bal-simple": instantiate_unwrapped_bal_simple,
        "bal-undersample": instantiate_unwrapped_bal_undersample,
        "cls-logistic": instantiate_unwrapped_cls_logistic,
        "cls-lstm-base": instantiate_unwrapped_cls_lstm_base,
        "cls-lstm-pool": instantiate_unwrapped_cls_lstm_pool,
        "cls-nb": instantiate_unwrapped_cls_nb,
        "cls-nn-2-layer": instantiate_unwrapped_cls_nn_2_layer,
        "cls-rf": instantiate_unwrapped_cls_rf,
        "cls-svm": instantiate_unwrapped_cls_svm,
        "fex-doc2vec": instantiate_unwrapped_fex_doc2vec,
        "fex-embedding-idf": instantiate_unwrapped_fex_embedding_idf,
        "fex-embedding-lstm": instantiate_unwrapped_fex_embedding_lstm,
        "fex-sbert": instantiate_unwrapped_fex_sbert,
        "fex-tfidf": instantiate_unwrapped_fex_tfidf,
        "qry-cluster": instantiate_unwrapped_qry_cluster,
        "qry-max": instantiate_unwrapped_qry_max,
        "qry-max-random": instantiate_unwrapped_qry_max_random,
        "qry-max-uncertainty": instantiate_unwrapped_qry_max_uncertainty,
        "qry-random": instantiate_unwrapped_qry_random,
        "qry-uncertainty": instantiate_unwrapped_qry_uncertainty,
    }
    try:
        return mapping[model.abbr](model.params, random_state)
    except KeyError as e:
        abbrs = "\n".join([key for key in mapping.keys()])
        raise f"Undefined behavior for model name f{model.abbr}. Valid model names are: f{abbrs}" from e
