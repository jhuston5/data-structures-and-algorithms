from stack_queue.stack import Stack
from stack_queue.queue import Queue
from stack_queue.animal_shelter import AnimalShelter
import pytest


def test_import():
    assert AnimalShelter


# Test that you can enqueue Animals into an empty Shelter
def test_enqueue_empty():
    S1 = AnimalShelter()
    S1.enqueue("dog")
    expected = S1.queue.front.value
    assert expected == "dog"


# Test to enqueue multiple Animals into a Shelter
def test_enqueue_multiple():
    S2 = AnimalShelter()
    S2.enqueue("dog")
    S2.enqueue("cat")
    S2.enqueue("dog")
    S2.enqueue("cat")
    expected = S2.queue.rear.value
    assert expected == "cat"


# Test if we can dequeue an animal from the middle of the Shelter
def test_dequeue():
    S3 = AnimalShelter()
    S3.enqueue("dog")
    S3.enqueue("cat")
    S3.enqueue("dog")
    expected = S3.dequeue("cat")
    assert expected == "cat"


# Test if we can dequeue an animal from the middle, and return the correct value from the reordered Queue
def test_dequeue_front():
    S4 = AnimalShelter()
    S4.enqueue("dog")
    S4.enqueue("cat")
    S4.enqueue("cat")
    S4.dequeue("cat")
    expected = S4.queue.rear.value
    assert expected == "dog"
