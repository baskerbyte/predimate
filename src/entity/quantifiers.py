from src.entity.base import Base
from src.entity.operators import Operator


class Quantifier(Base):
    symbol = ''

    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

        self._expr = f'({self.expr})' if isinstance(self.expr, Operator) else str(self.expr)

    def __str__(self):
        return f'{self.symbol}{self.var}{self._expr}'


class Universal(Quantifier):
    symbol = '∀'


class Existential(Quantifier):
    symbol = '∃'


class Predicate(Base):
    def __init__(self, predicate, letters=['x']):
        self.predicate = predicate.upper()
        self.letters = [letter.lower() for letter in letters]

    def __str__(self):
        return f'{self.predicate}{",".join(self.letters)}'


quantifiers = {
    "∀": Universal,
    "∃": Existential
}
