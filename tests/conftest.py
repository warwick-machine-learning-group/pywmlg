"""Fixtures used across all tests"""

import numpy as np
import pytest


@pytest.fixture(scope="function", params=[3, 4, 5])
def toy_dataset(request):
    """Small dataset to use across tests"""
    size = request.param  # get the parameter
    toy_matrix = np.zeros((size, size))
    np.random.seed(size)  # set the seed for reproducible test
    for i in range(size):
        for j in range(size):
            if i == 4 and j == 4:
                toy_matrix[i, j] = np.NaN  # insert a NaN
            else:
                toy_matrix[i, j] = np.random.randint(0, 100)
    return toy_matrix
