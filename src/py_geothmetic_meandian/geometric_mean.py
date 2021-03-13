"""A hacky, but working solution for geometric mean without having to require
numpy, scipy, or other libraries. In general we will try to use the one in
statistics first.
"""

from functools import reduce
from numbers import Number
from typing import Iterable


def geometric_mean(nums: Iterable[Number]) -> float:
    return reduce((lambda x, y: x * y), nums) ** (1 / len(nums))
