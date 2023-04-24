from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase
from eralchemy2.sqla import (
    column_to_intermediary,
    database_to_intermediary,
    declarative_to_intermediary,
    table_to_intermediary,
)
from eralchemy2.models import Table, Relation


def test_columns_parent():
    class Base(DeclarativeBase): pass

    class Parent(Base):
        __tablename__ = "parent"
        id = Column(String(), primary_key=True)

    class Child(Base):
        __tablename__ = "child"
        id = Column(String(), primary_key=True)
        parent = Column(String(), ForeignKey(Parent.id), primary_key=True)

    tables, relationships = declarative_to_intermediary(Base)

    assert len(tables) == 2
    assert len(relationships) == 1
    assert all(isinstance(t, Table) for t in tables)
    assert all(isinstance(r, Relation) for r in relationships)
    relation = relationships[0]
    assert relation.right_cardinality == '*'
    assert relation.left_cardinality == '1'
