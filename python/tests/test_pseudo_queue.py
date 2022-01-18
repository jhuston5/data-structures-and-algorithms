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


# # Can successfully push multiple values onto a stack
# def test_stack_push_multiple(S):
#     S.push("Elhokar")
#     S.push("Navani")
#     S.push("Dalinar")
#     expected = S.pop()
#     assert expected == "Dalinar"


# # Can successfully pop off the stack
# def test_stack_pop(S):
#     S.push("Navani")
#     expected = S.pop()
#     assert expected == "Navani"


# # Can successfully empty a stack after multiple pops
# def test_stack_empty(S):
#     S.push("Elhokar")
#     S.push("Navani")
#     S.push("Dalinar")
#     while S.top is not None:
#         S.pop()
#     expected = S.top
#     assert expected == None


# # Can successfully peek the next item on the stack
# def test_peek(S):
#     S.push("Syl")
#     S.push("Teft")
#     S.push("Rock")
#     expected = S.peek()
#     assert expected == "Rock"


# # Can successfully instantiate an empty stack
# def test_empty_stack(S):
#     expected = S.isEmpty()
#     assert expected == True


# # Calling pop or peek on empty stack raises exception
# def test_stack_pop_exception(S):
#     with pytest.raises(Exception):
#         S.push("Gavilar")
#         S.pop()
#         S.pop()
#         S.peek()
