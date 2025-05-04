"""
Test file.
"""

import pytest

from hashmaps import HashMap


def test_insert_and_get():
    """
    Test insert and get.
    """
    hm: HashMap = HashMap(10)
    hm.insert("apple", 100)
    hm.insert("banana", 200)
    assert hm.get("apple") == 100
    assert hm.get("banana") == 200


def test_get_missing_key():
    """
    Test missing key.
    """
    hm: HashMap = HashMap(5)
    with pytest.raises(Exception, match="sorry, key not found"):
        hm.get("ghost")


def test_repr():
    """
    Test string representation.
    """
    hm: HashMap = HashMap(3)
    hm.insert("cat", 9)
    hm.insert("dog", 4)
    repr_str = repr(hm)
    assert isinstance(repr_str, str)
    assert "cat" in repr_str or "dog" in repr_str
