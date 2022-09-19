import pytest
from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calculator = Calculator

    def test_multiply_calculate_correct(self):
        assert self.calculator.multiply(self, 2, 2) == 4

    def test_multiply_calculate_failed(self):
        assert  self.calculator.multiply(self, 2, 2) == 5

    def test_division_calculate_correct(self):
        assert self.calculator.division(self, 16, 8) == 2

    def test_division_calculate_failed(self):
        assert self.calculator.division(self, 16, 8) == 1

    def test_adding_calculate_correct(self):
        assert self.calculator.adding(self, 5, 6) == 11

    def test_adding_calculate_failed(self):
        assert self.calculator.adding(self, 5, 6) == 23

    def test_substraction_calculate_correct(self):
        assert  self.calculator.subtraction(self, 10, 7) == 3

    def test_substraction_calculate_failed(self):
        assert  self.calculator.subtraction(self, 10, 7) == 1
