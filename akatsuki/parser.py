#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re

from bibtexparser.bparser import BibTexParser


def load_bibtex_file(filepath):
    """Parse BibTeX file and return entry list"""
    with open(filepath, 'rU') as bibfile:
        bp = BibTexParser(bibfile)
        entries = bp.get_entry_list()

    entries = map(_capitalize_entry_title, entries)
    return entries


def _capitalize_entry_title(entry):
    """Capitalize an entry title"""
    if 'title' in entry:
        entry['title'] = re.sub(r'{(\w+)}', r'\1', entry['title'])
    return entry
