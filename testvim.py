"""Test vim grammar."""

import arpeggio
from nose.tools import assert_raises

from SpokenCode import vim


def test_saving():
    """Test saving syntax."""
    valid_syntax = [
        "Save buffer.",
        "Save all."]
    vim.parse(valid_syntax[0])
    vim.parse(valid_syntax[1])

    test_cases = [
        "Invalid syntax.",
        "Save buffer"]
    for test_case in test_cases:
        with assert_raises(arpeggio.NoMatch):
            vim.parse(test_case)
