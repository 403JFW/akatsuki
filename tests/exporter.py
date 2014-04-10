#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from akatsuki import exporter


class TestExporter(unittest.TestCase):
    def test_entry_html(self):
        entry_dict = {
            u'keyword': u'keyword1, keyword2',
            u'title': u'An amazing title',
            u'journal': u'KU Journal',
            u'author': u'John Appleseed',
            u'abstract': u'This is an abstract.',
            u'month': u'jan',
            u'volume': u'12',
            u'number': u'32',
            u'comments': u'A comment',
            u'year': u'2014',
            'id': 'ku2014',
            'type': u'article',
            u'pages': u'121--123'}
        entry_text = "%s<br>\n" % entry_dict['author']
        entry_text += "%s<br>\n" % entry_dict['title']
        entry_text += "%s %s %s;%s(%s):%s.<br>\n" % (
            entry_dict['journal'],
            entry_dict['year'],
            entry_dict['month'],
            entry_dict['volume'],
            entry_dict['number'],
            entry_dict['pages'])
        self.assertEqual(entry_text, exporter._entry_html(entry_dict))
