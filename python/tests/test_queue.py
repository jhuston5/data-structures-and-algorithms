from stack_queue.node import Node
from stack_queue.stack import Stack
from stack_queue.queue import Queue

import pytest


def test_import():
    assert Queue


@pytest.fixture
def Q():
    Q = Queue()
    return Q


# Can successfully enqueue into a queue
def test_enqueue(Q):
    Q.enqueue("Wax")
    expected = Q.peek()
    assert expected == "Wax"


# Can successfully enqueue multiple values into a queue
def test_multiple_enqueue(Q):
    Q.enqueue("Dalinar")
    Q.enqueue("Shallan")
    Q.enqueue("Kaladin")
    expected = Q.peek()
    assert expected == "Dalinar"


# Can successfully dequeue out of a queue the expected value
def test_dequeue(Q):
    Q.enqueue("Dalinar")
    Q.enqueue("Shallan")
    Q.enqueue("Kaladin")
    expected = Q.dequeue()
    assert expected == "Dalinar"


# Can successfully peek into a queue, seeing the expected value
def test_peek(Q):
    Q.enqueue("Wax")
    expected = Q.peek()
    assert expected == "Wax"


# Can successfully empty a queue after multiple dequeues
def test_empty_queue(Q):
    Q.enqueue("Dalinar")
    Q.enqueue("Shallan")
    while Q.front is not None:
        Q.dequeue()
    expected = Q.isEmpty()
    assert expected == True


# Can successfully instantiate an empty queue
def test_instantiate_empty_queue(Q):
    expected = Q.isEmpty()
    assert expected == True


# Calling dequeue or peek on empty queue raises exception
# def test_empty_queue_exception():
def test_empty_queue_exception(Q):
    with pytest.raises(Exception):
        Q.push("Gavilar")
        Q.pop()
        Q.pop()
        Q.peek()
