#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bibtexparser.bparser import BibTexParser


def load_bibtex_file(filepath):
    u"""Parse BibTeX file and return entry list"""
    with open(filepath, 'rU') as bibfile:
        bp = BibTexParser(bibfile)
        return bp.get_entry_list()
