from stack_queue.stack import Stack
from stack_queue.pseudo_queue import PseudoQueue

import pytest


def test_import():
    assert PseudoQueue


# @pytest.fixture
# def P():
#     P = PseudoQueue()
#     return P


# Can successfully enqueue onto an empty queue
def test_enqueue_empty():
    P1 = PseudoQueue()
    P1.enqueue("Windrunner")
    expected = P1.stack2.top.value
    assert expected == "Windrunner"


# Can successfully enqueue multiple values into a queue
def test_enqueue_multiple():
    P2 = PseudoQueue()
    P2.enqueue("Skybreaker")
    P2.enqueue("Windrunner")
    P2.enqueue("Lightweaver")
    P2.enqueue("Edgedancer")
    expected = P2.stack2.top.value
    assert expected == "Skybreaker"


# Can successfully dequeue the first value from a queue
def test_dequeue():
    P3 = PseudoQueue()
    P3.enqueue("Windrunner")
    P3.enqueue("Stoneward")
    P3.enqueue("Elsecaller")
    P3.dequeue()
    expected = P3.stack2.top.value
    assert expected == "Stoneward"


# Can successfully dequeue multiple values from a queue
def test_dequeue_multiple():
    P4 = PseudoQueue()
    P4.enqueue("Windrunner")
    P4.enqueue("Stoneward")
    P4.enqueue("Elsecaller")
    P4.dequeue()
    P4.dequeue()
    expected = P4.stack2.top.value
    assert expected == "Elsecaller"


def test_enqueue_dequeue():
    P5 = PseudoQueue()
    P5.enqueue("Windrunner")
    P5.enqueue("Stoneward")
    P5.dequeue()
    P5.enqueue("Elsecaller")
    P5.dequeue()
    expected = P5.stack2.top.value
    assert expected == "Elsecaller"
