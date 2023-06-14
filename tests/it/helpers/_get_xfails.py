def get_xfails(parameterization):
    reasons = {
        "double,logistic,embedding-idf,max": "issue #34",
        "double,lstm-base,doc2vec,max": "incompatible methods",
        "double,lstm-base,embedding-idf,max": "issue #34",
        "double,lstm-base,embedding-lstm,max": "issue #20",
        "double,lstm-base,sbert,max": "incompatible methods",
        "double,lstm-base,tfidf,max": "incompatible methods",
        "double,lstm-pool,doc2vec,max": "incompatible methods",
        "double,lstm-pool,embedding-idf,max": "issue #34",
        "double,lstm-pool,embedding-lstm,max": "issue #20",
        "double,lstm-pool,sbert,max": "incompatible methods",
        "double,lstm-pool,tfidf,max": "incompatible methods",
        "double,nb,doc2vec,max": "incompatible methods",
        "double,nb,embedding-idf,max": "issue #34",
        "double,nb,sbert,max": "incompatible methods",
        "double,nn-2-layer,doc2vec,max": "tbd",
        "double,nn-2-layer,embedding-idf,max": "issue #34",
        "double,nn-2-layer,embedding-lstm,max": "issue #33",
        "double,nn-2-layer,sbert,max": "issue #33",
        "double,nn-2-layer,tfidf,max": "issue #33",
        "double,rf,doc2vec,max": "tbd",
        "double,rf,embedding-idf,max": "issue #34",
        "double,svm,embedding-idf,max": "issue #34",
    }
    present = parameterization in reasons.keys()
    return present, reasons[parameterization] if present else ""
