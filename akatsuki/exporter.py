#!/usr/bin/env python
# -*- coding: utf-8 -*-


HTML_HEADER = u"""\
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Bibliography</title>
</head>
<body>
<h1>Bibliography</h1>"""
HTML_FOOTER = """\
</body>
</html>"""


def export_html(filepath, entries):
    # Open HTML file
    html = open(filepath, 'w')
    # Write HTML header lines
    html.write(HTML_HEADER)

    for entry in entries:
        html.write('<p>\n')
        html.write(entry['title'])
        html.write('</p>\n')

    # Write HTML footer lines
    html.write(HTML_FOOTER)
