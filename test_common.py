import arpeggio
from nose.tools import assert_raises

from SpokenCode import common


def parse(instruction):
    """Parse vim instruction."""
    parser = arpeggio.ParserPython(
        common.single_quoted_string,
        ignore_case=True)
    parse_tree = parser.parse(instruction)


class Test_single_quoted_string(object):

    def test_empty_string(self):
        parse("''")

    def test_valid_string(self):
        for string in [
                "'asdf'",
                """'"Hello," I said. "How are you?"'""",
                r"'Say it isn\'t so.'",
                r"'Say it really isn\\\'t so.'",
                r"'Say it is not so.\\'",
                r"'Say it \ is not so.'"]:
            parse(string)

    def test_invalid_string(self):
        for string in [
                "'Missing close quote",
                "Missing opening quote'",
                "No quotes",
                "'Unescaped ' quote'",
                r"\'Escaped opening quote'",
                r"'Escaped final quote\'"]:
            with assert_raises(arpeggio.NoMatch):
                parse(string)
