"""Common grammar elements."""

import arpeggio
from arpeggio import RegExMatch as _


def string():
    """Any string literal."""
    return [single_quoted_string, double_quoted_string]


def single_quoted_string():
    """Single quoted string literal."""
    return (
        "'",
        arpeggio.ZeroOrMore([
            r"\\",
            r"\'",
            _("[^']")
        ]),
        "'",
        arpeggio.EOF
    )


def double_quoted_string():
    """Double quoted string literal."""
    return (
        '"',
        arpeggio.ZeroOrMore([
            r'\\',
            r'\"',
            _('[^"]')
        ]),
        '"',
        arpeggio.EOF
    )
