from base import Base

class Operator(Base):
    def __init__(self, left, right):
        self.left = left
        self.right = right

        self.left_str = f'({self.left})' if isinstance(self.left, Operator) else str(self.left)
        self.right_str = f'({self.right})' if isinstance(self.right, Operator)  else str(self.right)


class Conjunction(Operator):
    def __str__(self):
        return f'{self.left_str}^{self.right_str}'


class Disjunction(Operator):
    def __str__(self):
        return f'{self.left_str}v{self.right_str}'


class Conditional(Operator):
    def __str__(self):
        return f'{self.left_str}->{self.right_str}'


class BiConditional(Operator):
    def __str__(self):
        return f'{self.left_str}<->{self.right_str}'

class Negation(Base):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        expr_str = f'({self.expr})' if isinstance(self.expr, Operator) else str(self.expr)

        return f'~{expr_str}'
    
