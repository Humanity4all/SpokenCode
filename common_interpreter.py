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

    def visit_unsigned_integer(self, _, children):
        """Interpret unsigned integer.

        """
        if all(item < 10 for item in children):
            return int("".join(str(item) for item in children))

        MULTIPLIERS = [1e2, 1e3, 1e6, 1e9, 1e12]
        stack = []
        # English numbers are built up like this:
        # ..., how many million, how many thousand, how many hundred, how many ones.
        # The 'how many' part can itself be built up like a number, but will
        # never be bigger than its multiplier. Here are two examples:
        #
        #  Example one: 19 1000 4 100 20 3 -> 19423
        #  19   -> [19]
        #
        #  1000 -> [19] + 1000 -> [19000]
        #          # because 1000 is a multiplier
        #
        #  4    -> [19000] + 4 -> [19000, 4]
        #          # Let's not commit, see what follows.
        #
        #  100  -> [19000, 4] + 100 -> [19000, 400]
        #          # because 100 is a multiplier
        #
        #  20   -> [19000, 400] + 20 -> [19000, 400, 20]
        #          # let's not commit
        #
        #  3    -> [19000, 400, 20] + 3 -> [19000, 400, 20, 3]
        #          # let's not commit
        #
        #  []   -> [19000, 400, 20, 3] + [] -> 19423
        #          # At the end of the list, just sum it all
        #
        # ============================
        #
        #  Example two: 100 90 100 -> 19000.
        #   100 -> [100]
        #
        #    90 -> [100] + 90 -> [100, 90]
        #          # let's not commit
        #
        #  1000 -> [100, 90] + 1000 -> [19000]
        #          # because 1000 is a multiplier, so sum the stack and multiply
        #
        #    [] -> [19000]          -> 19000
        #          # at the end of the list, just sum it all

        for child in children:
            if len(stack) == 0:
                stack = [child]
            elif child in MULTIPLIERS:
                # child is a multiplier. Use everything smaller than the
                # multiplier for the multiplier
                bigger_items = [item for item in stack if child < item]
                rest = [item for item in stack if item < child]
                stack = bigger_items + [sum(rest) * child]
            else:
                stack.append(child)
        result = sum(stack)
        return result

    def visit_minus_sign(self, _n, _c):
        """Turn 'minus' or '-' into '-'."""
        return '-'

    def visit_decimal_mark(self, _n, _c):
        """Turn variants of '.' into '.'."""
        return '.'

    def visit_signed_integer(self, _n, children):
        return int(''.join(str(child) for child in children))

    def visit_unsigned_float(self, _n, children):
        return float(''.join(str(child) for child in children))

    def visit_signed_float(self, _n, children):
        return float(''.join(str(child) for child in children))
