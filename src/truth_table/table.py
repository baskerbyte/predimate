from collections import OrderedDict
from itertools import product

from src.entity.operators import *


def generate_combinations(prepositions):
    """
    Generate all possible combinations of True and False for a list of prepositions.

    Args:
        prepositions (list of str): A list of prepositions for which combinations are generated.

    Returns:
        list of tuples: A list of tuples representing all possible combinations of True and False for prepositions.
   """
    return list(product([True, False], repeat=len(prepositions)))


def evaluate_expression(expr, result, row):
    """
    Recursively evaluate a logical expression.

    Args:
        prepositions (list of str): A list of prepositions in the expression.
        expr (Any): The logical expression to be evaluated.
        combination (tuple): A list of tuples representing combinations of True and False for prepositions.
        result (dict): A list of evaluation results for each expression.

    Returns:
        bool: The result of the evaluation.

    This function recursively evaluates logical expressions, either prepositions or compound expressions, and stores
    the results in the 'result' list.

    When the expression is a preposition (a string), it retrieves the corresponding value from the combinations.

    When the expression is a Negation or an Operator (e.g., Conjunction, Disjunction), it evaluates the subexpressions
    and calculates the result, which is then stored in the 'result' list.

    The function returns the final result of the evaluation.
    """
    value = None

    if expr in result and len(result[expr]) > row:
        return result[expr][row]

    if isinstance(expr, Operator):
        left_value = evaluate_expression(expr.left, result, row)
        right_value = evaluate_expression(expr.right, result, row)

        if isinstance(expr, Conjunction):
            value = left_value and right_value
        elif isinstance(expr, Disjunction):
            value = left_value or right_value
        elif isinstance(expr, Conditional):
            value = (not left_value) or right_value
        elif isinstance(expr, BiConditional):
            value = left_value == right_value
    elif isinstance(expr, Negation):
        value = not evaluate_expression(expr.expr, result, row)
    else:
        return result[expr][row]

    result.setdefault(expr, []).append(value)

    return value


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
    prep_combinations = list(zip(*combinations))
    result = {Preposition(preposition): prep_combinations[i] for i, preposition in enumerate(prepositions)}

    for i in range(len(combinations)):
        for expr in expressions:
            evaluate_expression(expr, result, i)

    keys = list(result.keys())

    return OrderedDict(
        sorted(
            result.items(),
            key=lambda item: (
                not isinstance(item[0], Preposition),
                not (isinstance(item[0], Negation) and isinstance(item[0].expr, Preposition)),
                str(item[0].expr) if isinstance(item[0], Negation) and isinstance(item[0].expr, Preposition) else None,
                keys.index(item[0])
            )
        )
    )


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


def is_valid(results, premises, conclusion):
    """
    Checks the validity of a logical argument based on premise and conclusion truth values.

    Args:
        results (dict): A dictionary mapping propositional variables to their truth values.
        premises (list): A list of strings representing the premises of the argument.
        conclusion (str): A string representing the conclusion of the argument.

    Returns:
        bool: True if the argument is logically valid, False otherwise.

    The `is_valid` function verifies whether a logical argument is valid based on the truth values of the premises
    and the conclusion. It uses a truth table to assess the argument's validity.
    """
        
    final_premises = [results[premise] for premise in premises]
    final_conclusion = results[conclusion]

    for row_premises, row_conclusion in zip(zip(*final_premises), final_conclusion):
        if (all(row_premises) and not row_conclusion) or not any(row_premises):
            return False

    return True
