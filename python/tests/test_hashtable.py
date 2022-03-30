from hashtable.hashtable import Hashtable


import pytest


def test_import():
    assert Hashtable


# @pytest.fixture
# def H():
#     H = Hashtable()
#     return H


# @pytest.fixture
# def HT():
#     HT = Hashtable()
#     HT.add("Cat", "calico")œ
#     HT.add("Dog", "dachsund")
#     HT.add("Shark", "mako")
#     print(HT)
#     return HT


def test_add():
    H = Hashtable()
    H.add("Shark", "mako")
    expected = "mako"
    actual = H.get("Shark")
    assert actual == expected


def test_keys():
    HT = Hashtable()
    HT.add("Cat", "calico")
    HT.add("Dog", "dachsund")
    HT.add("Shark", "mako")
    expected = HT.keys()
    actual = ["Cat", "Dog", "Shark"]
    assert actual == expected


def test_contains():
    HT = Hashtable()
    HT.add("Cat", "calico")
    HT.add("Dog", "dachsund")
    HT.add("Shark", "mako")
    expected = HT.contains("Shark")
    actual = True
    assert actual == expected


# # Can successfully enqueue into a queue
# def test_enqueue(H):
#     H.enqueue("Wax")
#     expected = Q.peek()
#     assert expected == "Wax"
