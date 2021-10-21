"""Functions for preprocessing datasets"""

import numpy as np
import numpy.typing as npt


def remove_rows_with_nans(data: npt.NDArray) -> npt.ArrayLike:
    """Remove NaNs"""
    return data[~np.isnan(data).any(axis=1)]
