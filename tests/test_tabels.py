
from mdparser import parse_markdown
import re

def normalize(html):
    return re.sub(r"\s+", " ", html).strip()

def test_basic_table():
    md = """
:::table
Name | Age
Tarun | 21
Alex | 22
:::
"""
    html = normalize(parse_markdown(md))

    assert "<table>" in html
    assert "<th>Name</th>" in html
    assert "<th>Age</th>" in html
    assert "<td>Tarun</td>" in html
    assert "<td>21</td>" in html
    assert "<td>Alex</td>" in html
