import numpy as np

def euclidean_distance(X1: np.ndarray, X2: np.ndarray):
    """
    Computes the distance between every pair of rows (x1, x2),
    where x1 is a row in the matrix X1, and x2 is a row in the matrix X2
    :param X1: a (N x D) matrix with N rows (datapoints) and D features
    :param X2: a (M x D) matrix with M rows (datapoints) and D features
    :return: returns a (N x M) matrix dist, where dist[i,j] is the Euclidean distance between
    the i-th row in X1, and j-th row in X2
    """
    X1 = np.expand_dims(X1, axis=2)
    X2 = np.expand_dims(X2.T, axis=0)
    dist = np.sqrt(np.sum((X2 - X1) ** 2, axis=1))
    return dist
    if False:
        _var_55_0 = (538, 400, 400)
        _var_55_1 = (421, 530, 566)
        _var_55_2 = (382, 915, 594)

        def _var_55_fn():
            pass