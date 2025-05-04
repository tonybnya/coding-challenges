"""
Test file.
"""

import pytest

from hashmaps import HashMap


def test_insert_and_get():
    hm = HashMap(10)
    hm.insert("apple", 100)
    hm.insert("banana", 200)
    assert hm.get("apple") == 100
    assert hm.get("banana") == 200


def test_collision_handling():
    hm = HashMap(2)  # Force collisions
    hm.insert("ab", 1)
    hm.insert("ba", 2)
    assert hm.get("ab") == 1
    assert hm.get("ba") == 2


def test_overwrite_value():
    hm = HashMap(5)
    hm.insert("key", 5)
    hm.insert("key", 99)  # Overwrite
    assert hm.get("key") == 99


def test_get_missing_key():
    hm = HashMap(3)
    with pytest.raises(Exception, match="sorry, key not found"):
        hm.get("ghost")


def test_delete_key():
    hm = HashMap(5)
    hm.insert("key", 123)
    assert hm.get("key") == 123
    hm.delete("key")
    with pytest.raises(Exception):
        hm.get("key")


def test_repr():
    hm = HashMap(5)
    hm.insert("a", 1)
    hm.insert("b", 2)
    assert "a" in repr(hm) or "b" in repr(hm)
