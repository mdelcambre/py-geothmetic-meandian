"""Geothmetic meandian for when you don't know which average you want.

Provides the geothmetic meandian as described in XKCD #2435
https://xkcd.com/2435/. 
"""

from numbers import Number
from statistics import mean, median
from typing import Iterable, Tuple

try:
    from statistics import geometric_mean
except ImportError:
    from .geometric_mean import geometric_mean


def _step(nums: Iterable[Number]) -> Tuple[float]:
    """Calculates the mean, geometric mean and median of a given iterable

    Parameters
    ----------
    nums: Iterable[Number]
        The iterable containing the set of numbers you want to calculate the
        many types of averages over

    Returns
    -------
    tuple(float)
        a tuple containing the mean, geometric_mean, and the median of numbers
        in nums
    """
    return (mean(nums), geometric_mean(nums), median(nums))


def geothmetic_meandian(nums: Iterable[Number], error: float = 0.001, drop_zeros:bool= True) -> float:
    """Computes the geothmetic meandian as definied by XKCD #2435 to a given
    allowable error.

    Parameters
    ----------
    nums: Iterable[Number]
        The iterable containing the set of numbers you wish to calculate the
        geothmetic_meandian over
    error: float, default 0.001
        The acceptable error between the minimum and maximum average taken.
    drop_zeros: bool, default True
        If there are any zeros in the set, the geometric mean will always be 
        zero and pull the convergence to zero always. If drop_zeros is true,
        any zeros will be removed before the compute.

    Returns
    -------
    float
        the geothmetic meandian of the numbers in nums
    """
    if 0 in nums:
        if not drop_zeros:
            return 0
        nums = [x for x in nums if x != 0]
    while max(nums) - min(nums) > error:
        nums = _step(nums)
    return median(nums)
