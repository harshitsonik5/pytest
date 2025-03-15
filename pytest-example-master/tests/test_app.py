import pytest

from myapp.app import multiply_by_two, divide_by_two


@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]


class TestApp:
    def test_multiplication(self, numbers):
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]
        

def test_area_calculation_student_id():
    from app import calculate_area  # Import the function from app.py
    assert calculate_area(62) == 3844  # last two digits of your student ID 

def test_area_calculation_student_id():
    from app import calculate_area
    assert calculate_area(23) == 500  # Incorrect value to force a failure
