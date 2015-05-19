# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tests.common import parent_id, parent_name, child_id, child_parent_id, relation, child, parent
from eralchemy.main import _intermediary_to_markdown

import re
import pytest
column_re = re.compile('(?P<key>\*?)(?P<name>[^*].+) \{label:\"(?P<type>.+)\"\}')


def test_all_to_er():
    tables = [child, parent]
    relations = [relation]
    output = _intermediary_to_markdown(tables, relations)
    for element in relations + tables:
        assert element.to_er() in output


def assert_column_well_rendered_to_er(col):
    col_er = col.to_er().strip()
    col_parsed = column_re.match(col_er)
    assert col_parsed.group('key') == ('*' if col.is_key else '')
    assert col_parsed.group('name') == col.name
    assert col_parsed.group('type') == col.type


def test_column_to_er():
    assert_column_well_rendered_to_er(parent_id)
    assert_column_well_rendered_to_er(parent_name)
    assert_column_well_rendered_to_er(child_id)
    assert_column_well_rendered_to_er(child_parent_id)


def test_relation():
    assert relation.to_er() in ['parent *--? child', 'child ?--* parent']


def assert_table_well_rendered_to_er(table):
    assert table.header_er == '[' + table.name + ']'
    table_er = table.to_er()
    for col in table.columns:
        assert col.to_er() in table_er


def test_table():
    assert_table_well_rendered_to_er(child)
    assert_table_well_rendered_to_er(parent)