"""Test vim grammar."""

import arpeggio
from SpokenCode import vim
from nose.tools import assert_equals


def test_saving():
    """Test saving syntax."""
    valid_syntax = [
        "Save buffer.",
        "Save all."]
    vim.parse(valid_syntax[0])
    vim.parse(valid_syntax[1])

    test_cases = [
        "Invalid syntax.",
        "Save buffer",
        "Save all. And some other junk."]
    for test_case in test_cases:
        try:
            vim.parse(test_case)
        except arpeggio.NoMatch:
            assert True
        else:
            print("Incorrectly passed testcase: {}".format(test_case))
            assert False
