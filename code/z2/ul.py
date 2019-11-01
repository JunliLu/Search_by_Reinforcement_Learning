import numpy as np
import math

def ndcg(a, top):
	s = 0.0
	for i in range(top):
		s += (a[i]/math.log(i+2, 2))
	s_ = 0.0
	a_ = np.sort(a)[::-1]
	for i in range(sum(np.isin(a_[:top], 1))):
		s_ += (1.0/math.log(i+2, 2))
	return s/s_ if s > 0.0 else 0.0

def dcg_k(r, k, method=1):
    # """Score is discounted cumulative gain (dcg)
    # Relevance is positive real values.  Can use binary
    # as the previous methods.
    # Example from
    # http://www.stanford.edu/class/cs276/handouts/EvaluationNew-handout-6-per.pdf
    # >>> r = [3, 2, 3, 0, 0, 1, 2, 2, 3, 0]
    # >>> dcg_k(r, 1)
    # 3.0
    # >>> dcg_k(r, 1, method=1)
    # 3.0
    # >>> dcg_k(r, 2)
    # 5.0
    # >>> dcg_k(r, 2, method=1)
    # 4.2618595071429155
    # >>> dcg_k(r, 10)
    # 9.6051177391888114
    # >>> dcg_k(r, 11)
    # 9.6051177391888114
    # Args:
    #     r: Relevance scores (list or numpy) in rank order
    #         (first element is the first item)
    #     k: Number of results to consider
    #     method: If 0 then weights are [1.0, 1.0, 0.6309, 0.5, 0.4307, ...]
    #             If 1 then weights are [1.0, 0.6309, 0.5, 0.4307, ...]
    # Returns:
    #     Discounted cumulative gain
    # """
    r = np.asfarray(r)[:k]
    if r.size:
        if method == 0:
            return r[0] + np.sum(r[1:] / np.log2(np.arange(2, r.size + 1)))
        elif method == 1:
            return np.sum(r / np.log2(np.arange(2, r.size + 2)))
        else:
            raise ValueError('method must be 0 or 1.')
    return 0.


def ndcg_k(r, k, method=1):
    # """Score is normalized discounted cumulative gain (ndcg)
    # Relevance is positive real values.  Can use binary
    # as the previous methods.
    # Example from
    # http://www.stanford.edu/class/cs276/handouts/EvaluationNew-handout-6-per.pdf
    # >>> r = [3, 2, 3, 0, 0, 1, 2, 2, 3, 0]
    # >>> ndcg_k(r, 1)
    # 1.0
    # >>> r = [2, 1, 2, 0]
    # >>> ndcg_k(r, 4)
    # 0.9203032077642922
    # >>> ndcg_k(r, 4, method=1)
    # 0.96519546960144276
    # >>> ndcg_k([0], 1)
    # 0.0
    # >>> ndcg_k([1], 2)
    # 1.0
    # Args:
    #     r: Relevance scores (list or numpy) in rank order
    #         (first element is the first item)
    #     k: Number of results to consider
    #     method: If 0 then weights are [1.0, 1.0, 0.6309, 0.5, 0.4307, ...]
    #             If 1 then weights are [1.0, 0.6309, 0.5, 0.4307, ...]
    # Returns:
    #     Normalized discounted cumulative gain
    # """
    dcg_max = dcg_k(sorted(r, reverse=True), k, method)
    if not dcg_max:
        return 0.
    return dcg_k(r, k, method) / dcg_max