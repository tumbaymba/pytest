from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], -4, -1) == [2, 3, 4]
    assert arrs.my_slice([], 1, 4) == []
    assert arrs.my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], 10) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -3) == [3, 4, 5]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -10) == []
