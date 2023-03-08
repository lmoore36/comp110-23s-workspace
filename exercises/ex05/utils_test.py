"""Unit test for EX05 functions."""

__author__ = "730556876"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_only_evens_use() -> None:
    """Use case test only_evens."""
    test_list: list[int] = [2, 4, 7, 3, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_only_evens_edge1() -> None:
    """No list 2."""
    test_list: list[int] = [7, 3]
    assert only_evens(test_list) == []


def test_only_evens_edge2() -> None:
    """No list 1."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_concat_use() -> None:
    """Use case test concat."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [4, 5, 6]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6]


def test_concat_edge1() -> None:
    """No list 2."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == [1, 2, 3]


def test_concat_edge2() -> None:
    """No list 1."""
    test_list1: list[int] = []
    test_list2: list[int] = [5, 6, 7, 8, 10]
    assert concat(test_list1, test_list2) == [5, 6, 7, 8, 10]


def test_sub_use() -> None:
    """Use case test sub."""
    test_list: list[int] = [10, 20, 30, 40]
    idx1: int = 1
    idx2: int = 3
    assert sub(test_list, idx1, idx2) == [20, 30]


def test_sub_edge1() -> None:
    """Idx2 larger than length."""
    test_list: list[int] = [10, 20, 30, 40]
    idx1: int = 1
    idx2: int = 5
    assert sub(test_list, idx1, idx2) == [20, 30, 40]


def test_sub_edge2() -> None:
    """Negative Idx1."""
    test_list: list[int] = [10, 20, 30, 40]
    idx1: int = -1
    idx2: int = 3
    assert sub(test_list, idx1, idx2) == [10, 20, 30]