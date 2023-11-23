from src.entity.operators import *
from src.entity.quantifiers import *


def encode_expression(expr: str) -> Base:
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
        # The operator with the most characters is <-> (3), so the substring
        elif operator := find_operator(expr[i:i + 3]):
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
                    j = find_end(expr[i:]) + i + 1
                    sub_result = encode_expression(expr[i:j])
                    i += j

                result.append(Negation(sub_result))
        elif quantifier := find_quantifier(expr[i:i + 2]):
            i += len(quantifier)

            if expr[i] == '(':
                i += 1
                j = find_parentheses_end(expr[i:]) + i
                sub_result = encode_expression(expr[i:j])
                i = j
            elif expr[i] == '~':
                i += 1
                j = find_end(expr[i:]) + i + 1
                sub_result = Negation(Predicate(expr[i - 1], [*expr[i:j]]))
                i = j
            else:
                i += 1
                j = find_end(expr[i:]) + i + 1
                sub_result = Predicate(expr[i - 1], [*expr[i:j]])
                i = j
            
            result.append(quantifiers[quantifier](sub_result))
        else:
            j = find_end(expr[i:]) + i + 1
            
            if j >= 2:
                sub_result = Predicate(expr[i], [*expr[i + 1:j]])
            else:
                sub_result = Preposition(expr[i].upper())

            result.append(sub_result)
            i += j

    if len(result) == 1:
        return result[0]


def find_parentheses_end(expr: str) -> int:
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


def find_operator(expr: str) -> str | None:
    for operator in operators:
        # Use startswith to avoid false truths like in PvQ, making sure that the start is an operator
        if expr.startswith(operator):
            return operator

    return None

def find_quantifier(expr: str) -> str | None:
    for quantifier in quantifiers:
        if expr.startswith(quantifier):
            return quantifier

    return None

def find_end(expr):
    for i in range(len(expr)):
        if not expr[i].isalpha() or expr[i] == 'v':
            return i - 1
        elif i == len(expr) - 1:
            return i
    
    return None