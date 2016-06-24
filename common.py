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


def unsigned_integer():
    """Unsigned integer."""
    return (
        number_element,
        arpeggio.ZeroOrMore(arpeggio.Optional(["and", "-"]), number_element))


def signed_integer():
    """Signed Integer."""
    return (
        arpeggio.Optional(["minus", "-"]),
        unsigned_integer)


def unsigned_float():
    """Unsigned float."""
    return (
        unsigned_integer,
        arpeggio.Optional(
            [",", "comma", ".", "period", "dot", "point"],
            unsigned_integer))


def signed_float():
    """Signed float."""
    return (
        signed_integer,
        arpeggio.Optional(
            [",", "comma", ".", "period", "dot", "point"],
            unsigned_integer))


def number_element():
    """Any word that can be part of a number."""
    return [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "thirthy",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
        "hundred",
        "thousand",
        "million",
        "billion",
        "trillion",
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        _("[0-9]")]
