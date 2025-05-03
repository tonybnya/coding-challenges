"""
Test file.
"""

from queues import Queue


def test_queue_initial_state():
    """
    Test for init queue.
    """
    queue = Queue()
    assert queue.is_empty() is True
    assert queue.size() == 0


def test_queue_push():
    """
    Test for push() method.
    """
    queue = Queue()
    queue.push(10)
    queue.push(20)
    queue.push(30)
    assert queue.is_empty() is False
    assert queue.size() == 3
    assert queue.peek() == 10
    assert repr(queue) == "Queue(tail → head): [30, 20, 10]"


def test_queue_pop():
    """
    Test for pop() method.
    """
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    assert queue.pop() == 1
    assert queue.size() == 2
    assert queue.peek() == 2
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.is_empty() is True


def test_queue_pop_empty():
    """
    Test for pop() empty Queue.
    """
    queue = Queue()
    assert queue.pop() is None


def test_queue_peek_empty():
    """
    Test for peek() empty Queue.
    """
    queue = Queue()
    assert queue.peek() is None
