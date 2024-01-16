def cluster(cells):
    """Given an array of cell of 9 x 6 colours, cluster them into 6 groups of colours, and indicate the 6 central colours.

    The `cells` is a numpy array of dimension 54 x 3,
    where each block of 3 represents an RGB colour of a cell on the Rubik's cube.

    The returned value is a tuple of 2 value of `(cluster_ids, cluster_centroids)`.
    The `cluster_ids` is a numpy array of dimension 54,
    each value is an integer between 0 and 5 (inclusive),
    indicating which cluster of colours the corresponding cell belongs to.
    The `cluster_centroids` is a numpy array of dimension 6 x 3,
    where each block of 3 is the RGB colour of the centroid of each cluster.
    """
    pass
