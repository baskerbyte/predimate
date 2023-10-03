import itertools

from src.entity.operators import *


def extract_expressions(expr, expressions=None):
    if expressions is None:
        expressions = []

    if isinstance(expr, Negation):
        extract_expressions(expr.expr, expressions)
    elif isinstance(expr, Operator):
        extract_expressions(expr.right, expressions)
        extract_expressions(expr.left, expressions)

    if expr not in expressions:
        expressions.append(expr)

    return expressions


def generate_combinations(prepositions):
    return list(itertools.product([True, False], repeat=len(prepositions)))


def evaluate_expression(expr, premises, combinations):
    if isinstance(expr, Operator):
        left_value = evaluate_expression(expr.left, premises, combinations)
        right_value = evaluate_expression(expr.right, premises, combinations)
        result_value = None

        if isinstance(expr, Conjunction):
            result_value = left_value and right_value
        elif isinstance(expr, Disjunction):
            result_value = left_value or right_value
        elif isinstance(expr, Conditional):
            result_value = (not left_value) or right_value
        elif isinstance(expr, BiConditional):
            result_value = left_value == right_value

        return result_value
    elif isinstance(expr, Negation):
        value = evaluate_expression(expr.expr, premises, combinations)

        return not value
    else:
        return combinations[premises.index(expr)]


def evaluate_expressions(expressions, combinations):
    result = []

    for combination in combinations:
        row = []

        for expr in expressions[1]:
            row.append(evaluate_expression(expr, expressions[0], combination))

        result.append(list(combination) + row)

    return result
