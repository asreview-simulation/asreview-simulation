from asreviewcontrib.simulation._private.lib.ofn.ofn_none_fun import ofn_none_fun
from asreviewcontrib.simulation._private.lib.ofn.ofn_wss_fun import ofn_wss_fun


def calc_ofn_score(ofn, project_path):
    return {
        "ofn-none": ofn_none_fun,
        "ofn-wss": ofn_wss_fun,
    }[
        ofn.abbr
    ](project_path, **ofn.params)
