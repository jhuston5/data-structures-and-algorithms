from insertion_sort.insertion import insertion_sort

import pytest


def test_insertion():
    test_list = [8, 4, 23, 42, 16, 15]
    expected = [4, 8, 15, 16, 23, 42]
    actual = insertion_sort(test_list)
    assert expected == actual


def test_insertion_few_unique():
    test_list = [5, 12, 7, 5, 5, 7]
    expected = [5, 5, 5, 7, 7, 12]
    actual = insertion_sort(test_list)
    assert expected == actual


def test_insertion_nearly_sorted():
    test_list = [2, 3, 5, 7, 13, 11]
    expected = [2, 3, 5, 7, 11, 13]
    actual = insertion_sort(test_list)
    assert expected == actual


def test_insertion_reverse_sorted():
    test_list = [20, 18, 12, 8, 5, -2]
    expected = [-2, 5, 8, 12, 18, 20]
    actual = insertion_sort(test_list)
    assert expected == actual
