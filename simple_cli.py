"""Simple Command line Interface."""
import arpeggio

# from . import common
import common
from common_interpreter import CommonInterpreter


def parse(instruction):
    """Parse vim instruction."""
    def new_rule():
        return (
            arpeggio.ZeroOrMore([
                common.string,
                common.unsigned_float,
                common.signed_float,
                common.unsigned_integer,
                common.signed_integer,]),
            arpeggio.EOF)
    parser = arpeggio.ParserPython(new_rule, ignore_case=True)
    return parser.parse(instruction)

if __name__ == "__main__":
    while True:
        # pylint: disable = invalid-name
        code = input("> ")
        # print(code)
        parse_tree = parse(code)
        interpreted_parse_tree = arpeggio.visit_parse_tree(parse_tree, CommonInterpreter())
        print(interpreted_parse_tree)
