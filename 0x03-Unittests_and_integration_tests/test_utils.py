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
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, message):
        """
        Method testing to establish whether it returns
        what its suppossed to
        """
    @parametized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b') 
    ])
    message = "Successfully returns the expected output"
    self.assert_equal(nested_map, message)

    def test_access_nested_map_exception():
        """Uses assertRaises to raise an alert"""

