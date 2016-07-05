# pylint: disable=missing-docstring,no-self-use
from nose.tools import assert_equals, assert_raises
from .common_interpreter import CommonInterpreter

class MockNode():
    def __init__(self, value):
        self.value = value


class TestNumbers():
    def test_valid_number_elements(self):
        test_cases = [
            ("zero", 0),
            ("one", 1),
            ("forty", 40),
            ("fourty", 40),
            ("million", 10**6),
            ("fourteen", 14),
            ("8", 8),
            (80, 80),
            ("hundred", 100)]
        interpreter = CommonInterpreter()
        for test_case in test_cases:
            assert_equals(
                interpreter.visit_number_element(MockNode(test_case[0]), None),
                test_case[1])

    def test_invalid_number_elements(self):
        test_cases = [
            "eleventyone",
            "pi"]
        interpreter = CommonInterpreter()
        for test_case in test_cases:
            with assert_raises(ValueError):
                interpreter.visit_number_element(MockNode(test_case), None)
                print(test_case)
