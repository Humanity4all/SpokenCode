"""Vim grammar for SpokenCode."""

import arpeggio


def vim_command():
    """Any valid vim command."""
    return [save_buffer, save_all]


def save_buffer():
    """Save currently focused buffer."""
    return "save buffer."


def save_all():
    """Save all open buffers."""
    return "save all."


def parse(instruction):
    """Parse vim instruction."""
    parser = arpeggio.ParserPython(vim_command, ignore_case=True)
    parse_tree = parser.parse(instruction)
