#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from future_builtins import zip
import unittest

from akatsuki import utils


class TestUtils(unittest.TestCase):
    def test_sort_by_date(self):
        # Test data
        entry_first = {
            'title': 'First',
            'year': 2012,
            'month': 'Jan'}
        entry_second = {
            'title': 'Second',
            'year': 2012,
            'month': 'Oct'}
        entry_third = {
            'title': 'Third',
            'year': 2013}
        entry_fourth = {
            'title': 'Third',
            'year': 2013,
            'month': 'Feb'}
        entries = [entry_second, entry_first, entry_fourth, entry_third]
        expected_result = [
            entry_first,
            entry_second,
            entry_third,
            entry_fourth]

        # Test sort by date
        result = utils.sort_by_date(entries)
        for es in zip(result, expected_result):
            self.assertEqual(es[0], es[1])

        # Test reverse sort by date
        expected_result = expected_result[::-1]
        result = utils.sort_by_date(entries, reverse=True)
        for es in zip(result, expected_result):
            self.assertEqual(es[0], es[1])
