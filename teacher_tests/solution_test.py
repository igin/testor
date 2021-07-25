from exercise import solution


def test_add_3_and_1():
    result = solution(3, 1)
    assert result == 4


def test_add_5_and_10():
    result = solution(5, 10)
    assert result == 15
