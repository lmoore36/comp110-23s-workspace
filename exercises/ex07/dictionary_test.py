"""Tests uses of dictionary functions."""

from exercises.ex07.dictionary import invert, count, favorite_color


def test_invert_use1() -> None:
    """Use case test 1."""
    test_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(test_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_use2() -> None:
    """Use case test 2."""
    test_dict: dict[str, str] = {'apple': 'cat'}
    assert invert(test_dict) == {'cat': 'apple'}


def test_invert_edge() -> None:
    """Edge case test."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_favorite_color_use1() -> None:
    """Use case test 1."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test_dict) == ('blue')


def test_favorite_color_use2() -> None:
    """Use case test 1."""
    test_dict: dict[str, str] = {"aarya": "navy", "madi": "purple", "hari": "yellow", "lucy": "yellow"}
    assert favorite_color(test_dict) == ('yellow')


def test_favorite_color_edge() -> None:
    """Edge case test."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ''


def test_count_use1() -> None:
    """Use case test 1."""
    test_list: list[str] = ['20', '30', '40', '40', '50', '60', '30', '30', '20', '10', '40']
    assert count(test_list) == {'20': 2, '30': 3, '40': 3, '50': 1, '60': 1, '10': 1}


def test_count_use2() -> None:
    """Use case test 2."""
    test_list: list[str] = ["lucy", "aarya", "christina", "kate", "lucy", "kate"]
    assert count(test_list) == {'lucy': 2, 'aarya': 1, 'christina': 1, 'kate': 2}


def test_count_edge() -> None:
    """Edge case test."""
    test_list: list[str] = []
    assert count(test_list) == {}