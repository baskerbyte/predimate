from src.entity.base import Base


class Operator(Base):
    """
    Base class for logical operators in a logical expression tree.

    Attributes:
        left: The left operand of the operator.
        right: The right operand of the operator.
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

        # String representations of left and right operands
        self._left_str = f'({self.left})' if isinstance(self.left, Operator) else str(self.left)
        self._right_str = f'({self.right})' if isinstance(self.right, Operator) else str(self.right)

    def __str__(self):
        return f'{self._left_str}{self.symbol}{self._right_str}'


class Conjunction(Operator):
    """
    Represents the logical `AND` operation in a logical expression tree.
    """

    symbol = '^'


class Disjunction(Operator):
    """
    Represents the logical `OR` operation in a logical expression tree.
    """

    symbol = 'v'


class Conditional(Operator):
    """
    Represents the logical `NOT` `OR` operation in a logical expression tree.
    """

    symbol = '->'


class BiConditional(Operator):
    """
    Represents the logical `EQ` operation in a logical expression tree.
    """

    symbol = '<->'


class Negation(Base):
    """
   Represents the logical `NOT` operation in a logical expression tree.

   Attributes:
       expr: The expression being negated.
   """

    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        expr_str = f'({self.expr})' if isinstance(self.expr, Operator) or isinstance(self.expr, Negation) \
            else str(self.expr)

        return f'~{expr_str}'


operators = {
    '^': Conjunction,
    'v': Disjunction,
    '->': Conditional,
    '<->': BiConditional,
    '~': Negation
}
