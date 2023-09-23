from src.entity.operators import *


def interpret_formula(expr):
    if isinstance(expr, Operator):
        return str(expr)
    else:
        return expr
