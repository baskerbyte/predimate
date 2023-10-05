from entity.operators import *


def interpret_formula(expr):
    if isinstance(expr, Operator) or isinstance(expr, Negation):
        return str(expr)
    else:
        return expr
