#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from akatsuki import parser


class TestParser(unittest.TestCase):
    def test_capitalize_entry_title(self):
        entry = {'title': '{C}apitalized {T}itle'}
        capitalized_title = 'Capitalized Title'
        entry = parser._capitalize_entry_title(entry)

        self.assertEqual(entry['title'], capitalized_title)

    def test_format_entry_authors(self):
        entry = {'author': 'Tanaka, A. and Suzuki, K. and Fujiwara, S'}
        formatted_author = 'Tanaka, A, Suzuki, K and Fujiwara, S'
        entry = parser._format_entry_authors(entry)
        self.assertEqual(entry['author'], formatted_author)
