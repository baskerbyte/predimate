from src.entity.operators import *


def decode_expression(expr):
    if isinstance(expr, Base):
        return str(expr)
    else:
        return expr
