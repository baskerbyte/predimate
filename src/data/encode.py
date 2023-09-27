from src.data.decode import interpret_formula
from src.entity.operators import *


def wrap_formula(expr):
    i = 0

    result = []

    while i < len(expr):
        if expr[i] == '(':
            j = i + 1
            open_count = 1
            while j < len(expr):
                if expr[j] == '(':
                    open_count += 1
                elif expr[j] == ')':
                    open_count -= 1
                    if open_count == 0:
                        break
                j += 1
            if open_count != 0:
                raise ValueError("Parênteses desequilibrados")

            sub_expr = expr[i + 1:j]
            result.append(wrap_formula(sub_expr))

            i = j + 1
        elif expr[i] == '^':
            i += 1

            return wrap_conjunction(expr[i:], result)
        elif expr[i] == 'v':
            i += 1

            return wrap_disjunction(expr[i:], result)
        elif expr[i:i + 2] == '->':
            i += 2

            return wrap_conditional(expr[i:], result)
        elif expr[i:i + 3] == '<->':
            i += 3

            return wrap_biconditional(expr[i:], result)
        elif expr[i] == '~':
            i += 1

            j = i + 1
            open_count = 1

            while j < len(expr):
                if expr[j] == '(':
                    open_count += 1
                elif expr[j] == ')':
                    open_count -= 1
                    if open_count == 0:
                        break
                j += 1
            if open_count != 0 and not expr[i].isalpha():
                raise ValueError("Parênteses desequilibrados")

            if expr[i].isalpha():
                sub_result = wrap_formula(expr[i])
            else:
                sub_result = wrap_formula(expr[i + 1:j])

            result.append(Negation(sub_result))
            i = j
        elif expr[i].isalpha():
            result.append(expr[i].upper())
            i += 1
        else:
            i += 1

    if len(result) == 1:
        return result[0]


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
