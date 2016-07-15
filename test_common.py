# pylint: disable=missing-docstring,no-self-use
import arpeggio
from nose.tools import assert_raises

from SpokenCode import common


def parse(instruction, rule):
    """Parse vim instruction."""
    def new_rule():
        return (rule, arpeggio.EOF)
    parser = arpeggio.ParserPython(new_rule, ignore_case=True)
    parser.parse(instruction)


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

    def test_invalid_number_element(self):
        with assert_raises(arpeggio.NoMatch):
            parse("random", common.number_element)

    def test_signed_integer(self):
        test_cases = [
            "-one",
            "minus twohundred",
            "two-thousand and five",
            "fourteen hundred",
            "386"]
        for test_case in test_cases:
            parse(test_case, common.signed_integer)

    def test_invalid_signed_integer(self):
        for test_case in [
                "eleventyone",
                "and four",
                "14.5",
                "random"]:
            with assert_raises(arpeggio.NoMatch):
                parse(test_case, common.signed_integer)

    def test_unsigned_integer(self):
        test_cases = [
            "twentyfive",
            "427",
            "nineteen"]
        for test_case in test_cases:
            parse(test_case, common.unsigned_integer)

    def test_invalid_unsigned_integer(self):
        for test_case in [
                "-five",
                "eleventyone",
                "and four",
                "14.5",
                "random"]:
            with assert_raises(arpeggio.NoMatch):
                parse(test_case, common.unsigned_integer)

    def test_signed_float(self):
        test_cases = [
            "-one dot zero",
            "minus twohundred point",
            "dot two-thousand and five",
            "fourteen hundred point two",
            "twentyfive.6",
            "fourtyfive dot nine",
            "sixty-seven point threehundredseven4",
            "386."]
        for test_case in test_cases:
            parse(test_case, common.signed_float)

    def test_invalid_signed_float(self):
        for test_case in [
                "eleventyone",
                "and four",
                "14.7.8",
                "random"]:
            with assert_raises(arpeggio.NoMatch):
                parse(test_case, common.signed_float)

    def test_unsigned_float(self):
        test_cases = [
            "twentyfive.",
            "427.",
            "3.14",
            "forty two point zero",
            "point nineteen"]
        for test_case in test_cases:
            parse(test_case, common.unsigned_float)

    def test_invalid_unsigned_float(self):
        for test_case in [
                "-five",
                "eleventyone",
                "and four",
                "1,235.584",
                "1,548,536.20",
                "random"]:
            with assert_raises(arpeggio.NoMatch):
                parse(test_case, common.unsigned_float)
