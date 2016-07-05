"""Interpreter for common grammar."""
from arpeggio import PTNodeVisitor


class CommonInterpreter(PTNodeVisitor):

    """Interpreter for common grammar."""

    def visit_number_element(self, node, _):
        """Interpret number element."""
        if str(node.value).isdigit():
            return int(node.value)
        number_translations = [
            ("zero", 0),
            ("one", 1),
            ("two", 2),
            ("three", 3),
            ("four", 4),
            ("five", 5),
            ("six", 6),
            ("seven", 7),
            ("eight", 8),
            ("nine", 9),
            ("ten", 10),
            ("eleven", 11),
            ("twelve", 12),
            ("thirteen", 13),
            ("fourteen", 14),
            ("fifteen", 15),
            ("sixteen", 16),
            ("seventeen", 17),
            ("eighteen", 18),
            ("nineteen", 19),
            ("twenty", 20),
            ("thirty", 30),
            ("fourty", 40),
            ("forty", 40),
            ("fifty", 50),
            ("sixty", 60),
            ("seventy", 70),
            ("eighty", 80),
            ("ninety", 90),
            ("hundred", 10**2),
            ("thousand", 10**3),
            ("million", 10**6),
            ("billion", 10**9),
            ("trillion", 10**12)]
        for element in number_translations:
            if node.value == element[0]:
                return element[1]
        raise ValueError("Not a valid number element: {}".format(node.value))
