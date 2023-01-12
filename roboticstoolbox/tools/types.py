#!/usr/bin/env python
"""
@author Jesse Haviland
"""

from typing import Tuple, Union, List, Set, Any
from numpy import ndarray, dtype, float64

NDArray = ndarray[Any, dtype[float64]]

PyArrayLike = Union[List[float], Tuple[float], Set[float]]

ArrayLike = Union[NDArray, PyArrayLike]
