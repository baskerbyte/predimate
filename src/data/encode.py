from src.entity.operators import *


def encode_expression(expr: str) -> Base:
    i = 0
    result = []

    while i < len(expr):
        if expr[i] == '(':
            i += 1
            j = find_parentheses_end(expr[i:]) + i + 1

            result.append(encode_expression(expr[i:j]))
            i = j
        elif expr[i] == ')':
            i += 1
        elif expr[i] != 'v' and expr[i].isalpha():
            result.append(expr[i].upper())
            i += 1
        else:
            operator = find_operator(expr[i:i + 3])
            i += len(operator)

            if operator != '~':
                right = encode_expression(expr[i:])
                left = result.pop()

                return operators[operator](left, right)
            else:
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
    found_operator = None

    for operator in operators:
        if expr.startswith(operator):
            found_operator = operator
            break

    return found_operator
