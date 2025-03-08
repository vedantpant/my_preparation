import pytest
from pytest_practice import add_number

def test_add():
    assert add_number(1,2) == 3