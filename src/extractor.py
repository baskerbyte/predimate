from operators import *


def wrap_formula(expr):
    i = 0
    result = []

    while i < len(expr):
        if expr[i] == '(':
            sub_expr, i = wrap_parentheses(expr, i)

            result.append(wrap_formula(sub_expr))
        elif expr[i] == '^':
            # Ignore conjunction size
            i += 1

            return wrap_conjunction(expr[i:], result)
        elif expr[i] == 'v':
            # Ignore disjunction size
            i += 1

            return wrap_disjunction(expr[i:], result)
        elif expr[i:i + 2] == '->':
            # Ignore conditional size
            i += 2

            return wrap_conditional(expr[i:], result)
        elif expr[i:i + 3] == '<->':
            # Ignore biconditional size
            i += 3

            return wrap_biconditional(expr[i:], result)
        elif expr[i] == '~':
            # Ignore negation size
            i += 1

            if expr[i] == '(':
                sub_expr, i = wrap_parentheses(expr, i)

                result.append(Negation(wrap_formula(sub_expr)))
            else:
                result.append(Negation(expr[i]))

                i += 1
        elif expr[i].isalpha():
            result.append(expr[i])
            i += 1
        else:
            i += 1

    if len(result) == 1:
        return result[0]


def wrap_parentheses(expr, i):
    sub_expr = ""
    # Ignore parentheses size
    i += 1

    while i < len(expr) and expr[i] != ')':
        sub_expr += expr[i]
        i += 1
    # Ignore parentheses size
    i += 1

    return sub_expr, i


def wrap_conjunction(expr, result):
    right = wrap_formula(expr)
    left = result.pop()

    return Conjunction(left, right)


def wrap_disjunction(expr, result):
    right = wrap_formula(expr)
    left = result.pop()

    return Disjunction(left, right)


def wrap_conditional(expr, result):
    right = wrap_formula(expr)
    left = result.pop()

    return Conditional(left, right)


def wrap_biconditional(expr, result):
    right = wrap_formula(expr)
    left = result.pop()

    return BiConditional(left, right)
