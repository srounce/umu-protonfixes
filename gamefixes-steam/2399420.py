"""Game fix for Le Mans Ultimate"""

from protonfixes import util

def main() -> None:
    """Use builtin d3dx11_43 for now"""
    util.winedll_override('d3dx11_43', util.OverrideOrder.BUILTIN)

