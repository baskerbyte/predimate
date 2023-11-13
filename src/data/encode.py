from src.entity.operators import *


def encode_expression(expr: str) -> Base:
    """
    Recursively encodes a logical expression represented as a string into a tree of logical operations.

    Args:
        expr (str): The logical expression to be encoded.

    Returns:
        Base: The root of the encoded logical expression tree.

    Raises:
        ValueError: If there are unbalanced parentheses in the expression.
    """

    i = 0
    result = []

    while i < len(expr):
        if expr[i] == '(':
            # Ignore '('
            i += 1
            # Sum `i` to find the real position of parenthesis in current expr
            # Add 1 to the result to move to the character immediately after the closing parenthesis.
            j = find_parentheses_end(expr[i:]) + i + 1

            result.append(encode_expression(expr[i:j]))
            # Ignore everything inside the parentheses, because it will be solved in the recursion above
            i = j
        elif expr[i] == ')':
            # Ignore ')'
            i += 1
        # Append if char is a real preposition, like: P, Q, R. Ignore 'v' because it's an operator
        elif expr[i] != 'v' and expr[i].isalpha():
            result.append(Preposition(expr[i].upper()))
            i += 1
        else:
            # The operator with the most characters is <-> (3), so the substring
            operator = find_operator(expr[i:i + 3])
            i += len(operator)

            # The behavior of negation is different from the other operators
            # While operators have a left and right side to the expression, negation has only one parameter
            if operator != '~':
                right = encode_expression(expr[i:])
                left = result.pop()

                return operators[operator](left, right)
            else:
                # After the negation there can be a parenthesis or a literal, as in ~(P^Q) or ~P
                if expr[i] == '(':
                    i += 1
                    j = find_parentheses_end(expr[i:]) + i
                    sub_result = encode_expression(expr[i:j])
                    i = j
                else:
                    sub_result = encode_expression(expr[i])
                    i += 1

                result.append(Negation(sub_result))

    if len(result) == 1:
        return result[0]


def find_parentheses_end(expr: str) -> int:
    """
    Finds the index of the closing parenthesis that corresponds to the opening parenthesis at the start of `expr`.

    Args:
        expr (str): The string starting with an opening parenthesis.

    Returns:
        int: The index of the closing parenthesis.

    Raises:
        ValueError: If the parentheses are unbalanced.
    """
    # In the expr the first parenthesis is ignored, so we start the count with 1
    count = 1

    for i, char in enumerate(expr):
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count == 0:
                return i

    raise ValueError("Parênteses desequilibrados")


def find_operator(expr: str) -> str:
    """
    Finds the logical operator at the beginning of the expression.

    Args:
        expr (str): The string to search for a logical operator.

    Returns:
        str: The found logical operator or None if none is found.
    """

    for operator in operators:
        # Use startswith to avoid false truths like in PvQ, making sure that the start is an operator
        if expr.startswith(operator):
            return operator

    return None
