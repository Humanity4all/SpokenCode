# pylint: disable=missing-docstring,no-self-use
from nose.tools import assert_equals, assert_raises
from .common_interpreter import CommonInterpreter

class MockNode():
    def __init__(self, value):
        self.value = value

def make_list_of_mock_nodes(plain_list):
    node_list = []
    for item in plain_list:
        node_list.append(MockNode(item))
    return node_list

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

    def test_unsigned_integer(self):
        test_cases = [
            ([1, 100], 100),
            ([14], 14),
            ([1, 2, 3, 4], 1234),
            ([19, 1000, 4, 100, 20, 3], 19423),
            ([100, 90, 1000], 190000),
            ([100, 90, 8, 1000], 198000),
            ([200, 90, 8, 1000], 298000),
            ([1, 100, 90, 8, 1000], 198000),
            ([1e6, 400, 1000], 1400000)]
        interpreter = CommonInterpreter()
        for test_case in test_cases:
            assert_equals(
                interpreter.visit_unsigned_integer(
                    None,
                    test_case[0]),
                test_case[1])
