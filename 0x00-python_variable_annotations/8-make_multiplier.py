#!/usr/bin/env python3
"""a type-annotated function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    return lambda i: i * multiplier
