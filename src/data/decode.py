from src.entity.operators import *


def decode_expression(expr):
    if isinstance(expr, Operator) or isinstance(expr, Negation):
        return str(expr)
    else:
        return expr
