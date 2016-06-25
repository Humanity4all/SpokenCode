# pylint: disable=missing-docstring,no-self-use
import arpeggio
from nose.tools import assert_raises

from SpokenCode import common


def parse(instruction, rule):
    """Parse vim instruction."""
    new_rule = (rule, arpeggio.EOF)
    parser = arpeggio.ParserPython(new_rule, ignore_case=True)
    parse_tree = parser.parse(instruction)


class TestSingleQuotedString(object):

    def test_empty_string(self):
        parse("''", common.single_quoted_string)

    def test_valid_string(self):
        for string in [
                "'asdf'",
                """'"Hello," I said. "How are you?"'""",
                r"'Say it isn\'t so.'",
                r"'Say it really isn\\\'t so.'",
                r"'Say it is not so.\\'",
                r"'Say it \ is not so.'"]:
            parse(string, common.single_quoted_string)

    def test_invalid_string(self):
        for string in [
                "'Missing close quote",
                "Missing opening quote'",
                "No quotes",
                "'Unescaped ' quote'",
                r"\'Escaped opening quote'",
                r"'Escaped final quote\'"]:
            with assert_raises(arpeggio.NoMatch):
                parse(string, common.single_quoted_string)
                print(string)


class TestDoubleQuotedString(object):

    def test_empty_string(self):
        parse('""', common.double_quoted_string)

    def test_valid_string(self):
        for string in [
                '"asdf"',
                '''"'Hello,' I said. 'How are you?'"''',
                r'"Say it isn\"t so."',
                r'"Say it really isn\\\"t so."',
                r'"Say it is not so.\\"',
                r'"Say it \ is not so."']:
            parse(string, common.double_quoted_string)

    def test_invalid_string(self):
        for string in [
                '"Missing close quote',
                'Missing opening quote"',
                'No quotes',
                '"Unescaped " quote"',
                r'\"Escaped opening quote"',
                r'"Escaped final quote\"']:
            with assert_raises(arpeggio.NoMatch):
                parse(string, common.double_quoted_string)


class TestNumbers():


    def test_number_element(self):
        test_cases = [
            "one",
            "fourteen",
            "four",
            "hundred",
            "5"]
        for test_case in test_cases:
            parse(test_case, common.number_element)

    def test_signed_integer(self):
        test_cases = [
            "-one",
            "minus twohundred",
            "two-thousand and five",
            "fourteen hundred",
            "386"]
        for test_case in test_cases:
            parse(test_case, common.signed_integer)

    def test_unsigned_integer(self):
        test_cases = [
            "twentyfive",
            "427",
            "nineteen"]
        for test_case in test_cases:
            parse(test_case, common.unsigned_integer)
