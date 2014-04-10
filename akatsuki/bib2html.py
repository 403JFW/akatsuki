# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from akatsuki.exporter import export_html
from akatsuki.parser import load_bibtex_file


def main(bibtex_file, html_file):
    """Load BibTeX file and export to HTML file"""
    entries = load_bibtex_file(bibtex_file)
    export_html(html_file, entries)
