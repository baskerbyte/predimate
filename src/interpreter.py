from operators import *
from extractor import wrap_formula


def interpret_formula(expr):
    if isinstance(expr, Operator):
        return str(expr)
    else:
        return expr


print(repr(wrap_formula("~((PvQ)v(P->(Q^R)))^((P<->R)v(T->U))")))
print(interpret_formula(Conjunction(left=Negation(expr=Disjunction(left=Disjunction(left='P', right='Q'), right=Conditional(left='P', right=Conjunction(left='Q', right='R')))), right=Disjunction(left=BiConditional(left='P', right='R'), right=Conditional(left='T', right='U')))

                        ))