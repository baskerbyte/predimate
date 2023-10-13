import itertools

from src.entity.operators import *


def generate_combinations(prepositions):
    """
    Generate all possible combinations of True and False for a list of prepositions.

    Args:
        prepositions (list of str): A list of prepositions for which combinations are generated.

    Returns:
        list of tuples: A list of tuples representing all possible combinations of True and False for prepositions.
   """
    return list(itertools.product([True, False], repeat=len(prepositions)))


def evaluate_expression(prepositions, expr, combination, result):
    """
    Recursively evaluate a logical expression.

    Args:
        prepositions (list of str): A list of prepositions in the expression.
        expr (Base): The logical expression to be evaluated.
        combination (tuple): A list of tuples representing combinations of True and False for prepositions.
        result (list of list): A list of evaluation results for each expression.

    Returns:
        bool: The result of the evaluation.

    This function recursively evaluates logical expressions, either prepositions or compound expressions, and stores
    the results in the 'result' list.

    When the expression is a preposition (a string), it retrieves the corresponding value from the combinations.

    When the expression is a Negation or an Operator (e.g., Conjunction, Disjunction), it evaluates the subexpressions
    and calculates the result, which is then stored in the 'result' list.

    The function returns the final result of the evaluation.
    """

    if isinstance(expr, Operator):
        # Starts recursively until it reaches a str, to obtain its boolean value
        left_value = evaluate_expression(prepositions, expr.left, combination, result)
        right_value = evaluate_expression(prepositions, expr.right, combination, result)
        result_value = None

        if isinstance(expr, Conjunction):
            result_value = left_value and right_value
        elif isinstance(expr, Disjunction):
            result_value = left_value or right_value
        elif isinstance(expr, Conditional):
            result_value = (not left_value) or right_value
        elif isinstance(expr, BiConditional):
            result_value = left_value == right_value

        # For each horizontal combination, add the vertical value
        idx = find_or_add_element(result, expr)
        result[idx].append(result_value)

        return result_value
    elif isinstance(expr, Negation):
        value = not evaluate_expression(prepositions, expr.expr, combination, result)

        idx = find_or_add_element(result, expr)
        result[idx].append(value)

        return value
    elif isinstance(expr, str):
        # The prepositions are organized in alphabetical order, so you can deduce the position of the tuple
        return combination[prepositions.index(expr)]


def find_or_add_element(lst, element):
    for i, item in enumerate(lst):
        if item[0] == element:
            return i

    lst.append([element])
    return len(lst) - 1


def evaluate_expressions(prepositions, expressions, combinations):
    """
    Evaluate a list of logical expressions for all possible combinations of prepositions.

    Args:
        prepositions (list of str): A list of prepositions used in the expressions.
        expressions (list of Base): A list of logical expressions to evaluate.
        combinations (list of tuples): A list of tuples representing combinations of True and False for prepositions.

    Returns:
        list of lists: A list of evaluation results for each expression and each combination.

    This function evaluates a list of logical expressions (expressions) for all possible combinations of True and False
    for prepositions. It returns a list of evaluation results for each expression and each combination
    **in column orientation**.
    """

    result = []

    for combination in combinations:
        for expr in expressions:
            evaluate_expression(prepositions, expr, combination, result)

    return result


def table_type(results):
    """
    Determine the type of a logical table based on its final evaluation results.

    Args:
        results (list of lists): A list of evaluation results for logical expressions and combinations.

    Returns:
        str: The type of the logical table, which can be "Tautologia," "Contradição," or "Contingência."

    This function analyzes the evaluation results of logical expressions and returns the type of the logical table based on
    those results. If all results indicate True, the table is a "Tautologia." If all results indicate False, it is a
    "Contradição." Otherwise, it is a "Contingência."
   """

    if all(result[-1] for result in results):
        return "Tautologia"
    elif all(not result[-1] for result in results):
        return "Contradição"
    else:
        return "Contingência"
