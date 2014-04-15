Akatsuki
========

[![Build Status](https://travis-ci.org/403JFW/akatsuki.svg?branch=master)](https://travis-ci.org/403JFW/akatsuki)
[![Coverage Status](https://coveralls.io/repos/403JFW/akatsuki/badge.png?branch=master)](https://coveralls.io/r/403JFW/akatsuki?branch=master)

Akatsuki is a BibTeX to HTML converter written in Python.

Requirements
------------
* Python 2.7+, Python 3.2+ or PyPy
* [python-bibtexparser](https://github.com/sciunto/python-bibtexparser)

Installation
------------
```
pip install akatsuki
```

Usage
-----

### bib2html
Convert BibTeX file to HTML5 file.

Input BibTeX file: john.bib
Output HTML file: john.html

```
bib2html john.bib john.html
```