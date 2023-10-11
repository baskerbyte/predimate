import itertools

from src.entity.operators import *


def generate_combinations(prepositions):
    return list(itertools.product([True, False], repeat=len(prepositions)))


def evaluate_expression(premises, expr, combinations, result):
    if isinstance(expr, Operator):
        left_value = evaluate_expression(premises, expr.left, combinations, result)
        right_value = evaluate_expression(premises, expr.right, combinations, result)
        result_value = None

        if isinstance(expr, Conjunction):
            result_value = left_value and right_value
        elif isinstance(expr, Disjunction):
            result_value = left_value or right_value
        elif isinstance(expr, Conditional):
            result_value = (not left_value) or right_value
        elif isinstance(expr, BiConditional):
            result_value = left_value == right_value

        idx = find_or_add_element(result, expr)
        result[idx].append(result_value)

        return result_value
    elif isinstance(expr, Negation):
        value = not evaluate_expression(premises, expr.expr, combinations, result)

        idx = find_or_add_element(result, expr)
        result[idx].append(value)

        return value
    elif isinstance(expr, str):
        return combinations[premises.index(expr)]


def find_or_add_element(lst, element):
    for i, item in enumerate(lst):
        if item[0] == element:
            return i

    lst.append([element])
    return len(lst) - 1


def evaluate_expressions(prepositions, expressions, combinations):
    result = []

    for combination in combinations:
        for expr in expressions:
            evaluate_expression(prepositions, expr, combination, result)

    return result


def table_type(results):
    if all(result[-1] for result in results):
        return "Tautologia"
    elif all(not result[-1] for result in results):
        return "Contradição"
    else:
        return "Contingência"
