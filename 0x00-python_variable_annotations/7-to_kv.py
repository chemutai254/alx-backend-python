#!/usr/bin/env python3
"""a type-annotated function to_kv"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """" returns a tuple  should be annotated as a float"""
    return v**2`
