import unittest

from src.data.decode import interpret_formula
from src.entity.operators import *


class TestDecode(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(
            interpret_formula(
                Conjunction(left=Negation(expr=Disjunction(left=Disjunction(left='P', right='Q'), right=Conditional(left='P', right=Conjunction(left='Q', right='R')))), right=Disjunction(left=BiConditional(left='P', right='R'), right=Conditional(left='T', right='U')))
            ),
            "~((PvQ)v(P->(Q^R)))^((P<->R)v(T->U))"
        )

        self.assertEqual(
            interpret_formula(
                Conjunction(left=Disjunction(left='P', right='Q'), right=Negation('P'))
            ),
            "(PvQ)^~P"
        )

        self.assertEqual(
            interpret_formula(Conditional(left='P', right='Q')),
            "P->Q"
        )


if __name__ == '__main__':
    unittest.main()
