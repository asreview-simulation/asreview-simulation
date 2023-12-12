from asreviewcontrib.simulation._private.lib.ofn.ofn_none_fun import ofn_none_fun
from asreviewcontrib.simulation._private.lib.ofn.ofn_wss_fun import ofn_wss_fun
from asreviewcontrib.simulation._private.lib.get_quads import get_quads


def calc_ofn_score(ofn, project_path):
    my_ofns = {
        "ofn-none": ofn_none_fun,
        "ofn-wss": ofn_wss_fun,
    }
    other_ofns = [{abbr: q.impl} for abbr, q in get_quads() if abbr.startswith("ofn")]

    ofns = my_ofns
    for other_ofn in other_ofns:
        ofns.update(other_ofn)

    return ofns[ofn.abbr](project_path, **ofn.params)
