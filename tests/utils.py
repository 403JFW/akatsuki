#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
try:
    from future_builtins import zip
except ImportError:
    pass

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

    def test_pmid_to_url(self):
        # Test data
        entry_first = {
            'title': 'First',
            'id': 'aaa'}
        entry_second = {
            'title': 'Second',
            'id': 'pmid24685317'}
        entry_third = {
            'title': 'Third',
            'id': 'pmid24685317',
            'URL': 'http://www.google.com/'}
        entries = [entry_first, entry_second, entry_third]

        result = utils.pmid_to_url(entries)

        self.assertFalse('URL' in result[0])
        self.assertEqual(result[1]['URL'],
                        'http://www.ncbi.nlm.nih.gov/pubmed/24685317')
        self.assertEqual(result[2]['URL'], entry_third['URL'])
