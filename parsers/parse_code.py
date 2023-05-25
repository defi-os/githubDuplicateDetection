from collections import OrderedDict


def vectorSpaceModel(query, doc_dict, tfidf_scr):
    query_vocab = []
    for word in query.split():
        if word not in query_vocab:
            query_vocab.append(word)

    query_wc = {}
    for word in query_vocab:
        query_wc[word] = query.lower().split().count(word)

    relevance_scores = {}
    for doc_id in doc_dict.keys():
        score = 0
        for word in query_vocab:
            score += query_wc[word] * tfidf_scr[doc_id][word]
        relevance_scores[doc_id] = score
    sorted_value = OrderedDict(
        sorted(relevance_scores.items(), key=lambda x: x[1], reverse=True)
    )
    top_5 = {k: sorted_value[k] for k in list(sorted_value)[:5]}
    return top_5
