#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from akatsuki import exporter


class TestExporter(unittest.TestCase):
    def test_entry_html(self):
        entry_dict = {
            'keyword': 'keyword1, keyword2',
            'title': 'An amazing title',
            'journal': 'KU Journal',
            'author': 'John Appleseed',
            'abstract': 'This is an abstract.',
            'month': 'Jan',
            'volume': '12',
            'number': '32',
            'comments': 'A comment',
            'year': '2014',
            'id': 'ku2014',
            'type': 'article',
            'pages': '121--123',
            'URL': 'http://www.google.com/'}
        entry_text = "%s<br>\n" % entry_dict['author']
        entry_text += "%s<br>\n" % entry_dict['title']
        entry_text += "%s %s %s;%s(%s):%s.<br>\n" % (
            entry_dict['journal'],
            entry_dict['year'],
            entry_dict['month'],
            entry_dict['volume'],
            entry_dict['number'],
            entry_dict['pages'])
        if 'URL' in entry_dict:
            link_text = '<a href="{0:s}">{0:s}</a><br>\n'
            entry_text += link_text.format(entry_dict['URL'])
        self.assertEqual(entry_text, exporter._entry_html(entry_dict))
