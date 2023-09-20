class Conjunction:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Conjunction({self.left}, {self.right})"


class Negation:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"Negation({self.expr})"


class Disjunction:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Disjunction({self.left}, {self.right})"


class Conditional:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Conditional({self.left}, {self.right})"


class BiConditional:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"BiConditional({self.left}, {self.right})"

class Preposition:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"Preposition({self.expr})"
