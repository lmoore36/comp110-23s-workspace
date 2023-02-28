""""unit test for sun function"""

from lessons.sum import sum

def test_empty() -> None:
    assert sum([]) == 0.0

def test_one_element() -> Nonee:
    test_list: list[float] = 1.0
    assert sum([test_list]) == 1.0
