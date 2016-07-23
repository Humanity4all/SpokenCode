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
    )

def couple_word():
    return ["and", "-"]

def unsigned_integer():
    """Unsigned integer."""
    return (
        number_element,
        arpeggio.ZeroOrMore(arpeggio.Optional(couple_word), number_element))


def minus_sign():
    """Minus sign."""
    return ["minus", "-"]


def signed_integer():
    """Signed Integer."""
    return (arpeggio.Optional(minus_sign), unsigned_integer)


def decimal_mark():
    """Decimal mark."""
    return [".", "period", "dot", "point"]


def unsigned_float():
    """Unsigned float."""
    return [
        (unsigned_integer, decimal_mark, unsigned_integer),
        (unsigned_integer, decimal_mark),
        (decimal_mark, unsigned_integer)]


def signed_float():
    """Signed float."""
    return (arpeggio.Optional(minus_sign), unsigned_float)

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
        "fourty",
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
