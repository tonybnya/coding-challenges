"""
Test file.
"""

import pytest

from stacks import Stack


def test_stack_initial_state():
    """
    Test for init Stack.
    """
    stack = Stack()
    assert stack.is_empty() is True
    assert stack.size() == 0


def test_stack_push():
    """
    Test for push() method.
    """
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.is_empty() is False
    assert stack.size() == 3
    assert stack.peek() == 30
    assert repr(stack) == "Stack(bottom → top): [10, 20, 30]"


def test_stack_pop():
    """
    Test for pop() method.
    """
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.size() == 2
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty() is True


def test_stack_pop_empty():
    """
    Test for pop() empty Stack.
    """
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()


def test_stack_peek_empty():
    """
    Test for peek() empty Stack.
    """
    stack = Stack()
    with pytest.raises(IndexError):
        stack.peek()
