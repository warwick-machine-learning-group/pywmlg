"""Tests for preprocessing"""

import numpy as np

from pywmlg.preprocessing import remove_rows_with_nans


def test_remove_rows_with_nans(toy_dataset):
    """Test remove NaNs"""
    assert np.count_nonzero(np.isnan(remove_rows_with_nans(toy_dataset))) == 0
