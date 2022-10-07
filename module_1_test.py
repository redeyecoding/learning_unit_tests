"""And example of a test module in pytest"""

from module_1 import total, join_things


def test_total_empty() -> None:
    """Total of empty list should be equal to 0.0"""
    assert total([]) == 0.0

def test_total_single_item() -> None:
    """The total of a single item should be the first item's value"""
    assert total([8.2]) == 8.2

def test_total_multiple_items() -> None:
    """Total for multiple floats in list should be sum of items in list."""
    assert total([1.0,1.0,3.0,5.0,4.0]) == 14.0

def test_join_things_empty() -> str:
    """An Empty list or an empty delimiter should result in an empty string """
    assert join_things([],) == ""

def test_join_things_single_item_no_delimiter() -> str:
    """A a single item in the list with no delimiter should return a string """
    assert join_things([4],) == "4"

def test_join_things_multiple_items_no_delimiter() -> str:
    """Multiple items in the list with no delimiter should return a string """
    assert join_things([4,6,2,100],) == "462100"

def test_join_things_single_item_with_delimiter() -> str:
    """A a single item in the list with a delimiter should return a string """
    assert join_things([4],'-') == "4-"

def test_join_things_empty_list_with_delimiter() -> str:
    """A empty list with a delimiter should return an empty string """
    assert join_things([],'-') == ""

def test_join_things_multiple_items_with_delimiter() -> str:
    """Multiple items in the list with a delimiter should return a string """
    assert join_things([1,2,3,4,5,6,7,8,9,10],'-') == "1-2-3-4-5-6-7-8-9-10"