from numbers import Number
from statistics import mean, median

try:
    from statistics import geometric_mean
except ImportError:
    from .geometric_mean import geometric_mean

from typing import Iterable, Tuple


def _step(nums: Iterable[Number]) -> Tuple[float]:
    return (mean(nums), geometric_mean(nums), median(nums))


def geothmetic_meandian(nums: Iterable[Number], error: float = 0.001) -> float:
    while max(nums) - min(nums) > error:
        nums = _step(nums)
    return median(nums)
