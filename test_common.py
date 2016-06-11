import arpeggio
from nose.tools import assert_raises

from SpokenCode import common


def parse(instruction, rule):
    """Parse vim instruction."""
    parser = arpeggio.ParserPython(rule, ignore_case=True)
    parse_tree = parser.parse(instruction)


class Test_single_quoted_string(object):

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


class Test_double_quoted_string(object):

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
