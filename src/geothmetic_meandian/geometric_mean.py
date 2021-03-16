"""A hacky, but working solution for geometric mean without having to require
numpy, scipy, or other libraries. In general we will try to use the one in
statistics first.
"""

from functools import reduce
from numbers import Number
from typing import Iterable


def geometric_mean(nums: Iterable[Number]) -> float:
    """Calculates the geometric mean in a one line lambda/reduce. A hacky slow
    solution for python versions before 3.8 that do not support
    statistics.geometric_mean

    Parameters
    ----------
    nums: Iterable[Number]
        The iterable containing the set of numbers you want to calculate the
        geometric_mean over

    Returns
    -------
    float
        the geometric mean of the numbers in nums
    """
    return reduce((lambda x, y: x * y), nums) ** (1 / len(nums))
