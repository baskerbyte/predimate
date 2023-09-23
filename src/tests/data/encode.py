import unittest

from src.data.encode import wrap_formula
from src.entity.operators import *


class TestEncode(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(
            wrap_formula("~((PvQ)v(P->(Q^R)))^((P<->R)v(T->U))"),
            Conjunction(left=Negation(expr=Disjunction(left=Disjunction(left='P', right='Q'), right=Conditional(left='P', right=Conjunction(left='Q', right='R')))), right=Disjunction(left=BiConditional(left='P', right='R'), right=Conditional(left='T', right='U')))
        )

        self.assertEqual(
            wrap_formula("(PvQ)^~P"),
            Conjunction(left=Disjunction(left='P', right='Q'), right=Negation('P'))
        )

        self.assertEqual(
            wrap_formula("P->Q"),
            Conditional(left='P', right='Q')
        )


if __name__ == '__main__':
    unittest.main()
