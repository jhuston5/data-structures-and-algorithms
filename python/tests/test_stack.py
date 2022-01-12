from stack_queue.node import Node
from stack_queue.stack import Stack


import pytest


def test_import():
    assert Stack


@pytest.fixture
def S():
    S = Stack()
    return S


# Can successfully push onto a stack
def test_stack_push(S):
    S.push("Navani")
    expected = S.pop()
    assert expected == "Navani"


# Can successfully push multiple values onto a stack
def test_stack_push_multiple(S):
    S.push("Elhokar")
    S.push("Navani")
    S.push("Dalinar")
    expected = S.pop()
    assert expected == "Dalinar"


# Can successfully pop off the stack
def test_stack_pop(S):
    S.push("Navani")
    expected = S.pop()
    assert expected == "Navani"


# Can successfully empty a stack after multiple pops
def test_stack_empty(S):
    S.push("Elhokar")
    S.push("Navani")
    S.push("Dalinar")
    while S.top is not None:
        S.pop()
    expected = S.top
    assert expected == None


# Can successfully peek the next item on the stack
def test_peek(S):
    S.push("Syl")
    S.push("Teft")
    S.push("Rock")
    expected = S.peek()
    assert expected == "Rock"


# Can successfully instantiate an empty stack
def test_empty_stack(S):
    expected = S.isEmpty()
    assert expected == True


# Calling pop or peek on empty stack raises exception
def test_stack_pop_exception(S):
    with pytest.raises(Exception):
        S.push("Gavilar")
        S.pop()
        S.pop()
        S.peek()
