"""Functions to generate Collatz sequences"""

from functools import lru_cache
from typing import Dict, Sequence, Tuple


@lru_cache(maxsize=None)
def _collatz_rule(n: int) -> int:
    return n * 3 + 1 if n % 2 == 1 else n // 2


def _generate_sequence(initial_value: int) -> Sequence[int]:
    """Generate a Collatz sequence given the initial value."""
    n = initial_value
    sequence = [n]
    while n != 1:
        n = _collatz_rule(n)
        sequence.append(n)
    return sequence


def generate_sequences(initial_value_range: Tuple[int, int]) -> Dict[int, list]:
    """Generate Collatz sequences given a range of initial values."""
    start, end = initial_value_range
    if not start < end:
        raise ValueError("end must be greater than or equal to start")

    return {n: _generate_sequence(n) for n in range(start, end)}
