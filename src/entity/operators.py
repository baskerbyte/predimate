from src.entity.base import Base


class Operator(Base):
    symbol = ''

    def __init__(self, left, right):
        self.left = left
        self.right = right

        # String representations of left and right operands
        self._left_str = f'({self.left})' if isinstance(self.left, Operator) else str(self.left)
        self._right_str = f'({self.right})' if isinstance(self.right, Operator) else str(self.right)

    def __str__(self):
        return f'{self._left_str}{self.symbol}{self._right_str}'


class Conjunction(Operator):
    symbol = '^'


class Disjunction(Operator):
    symbol = 'v'


class Conditional(Operator):
    symbol = '->'


class BiConditional(Operator):
    symbol = '<->'


class Negation(Base):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        expr_str = f'({self.expr})' if isinstance(self.expr, Operator) or isinstance(self.expr, Negation) \
            else str(self.expr)

        return f'~{expr_str}'


class Preposition(Base):
    def __init__(self, prep):
        self.prep = prep

    def __str__(self):
        return f'{self.prep}'


operators = {
    '^': Conjunction,
    'v': Disjunction,
    '->': Conditional,
    '<->': BiConditional,
    '~': Negation
}
