class Calculator:
    def sum(self, first: float, second: float) -> float:
        return first + second


def test_sum_of_two_numbers():
    # Arrange
    first = 10
    second = 20
    calc = Calculator()

    # Act
    result = calc.sum(first, second)

    # Assert
    assert 30 == result
