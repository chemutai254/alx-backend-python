#!/usr/bin/env python3
"""Parametize a unittest"""
from nose.tools import assert_equal
from parameterized import parameterized, parameterized_class
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    Parametization tests the function of below inputs
    """
    @parametized.expand([
        nested_map={"a": 1}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a", "b"),
    ])
    def test_access_nested_map(self, a, b, path):
        """
        Method testing to establish whether it returns
        what its suppossed to
        """
        assert_equal(a, b, path)

    @parametized.expand([
        nested_map={"a": 1}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a", "b"),
    ])
    def test_access_nested_map(self, a, b, path):
        assert_equal(a, b, path)
