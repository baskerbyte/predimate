import unittest

from src.data.decode import interpret_formula
from src.entity.operators import *


class TestDecode(unittest.TestCase):
    def test_decode_conjunction(self):
        self.assertEqual(
            "P^Q",
            interpret_formula(Conjunction(left='P', right='Q'))
        )

        self.assertEqual(
            "(A^B)^C",
            interpret_formula(Conjunction(left=Conjunction(left='A', right='B'), right='C'))
        )

        self.assertEqual(
            "((D^E)^F)^G",
            interpret_formula(Conjunction(left=Conjunction(left=Conjunction(left='D', right='E'), right='F'), right='G'))
        )

        self.assertEqual(
            "(((H^I)^J)^K)^L",
            interpret_formula(Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left='H', right='I'), right='J'), right='K'), right='L'))
        )

        self.assertEqual(
            "((((M^N)^O)^P)^Q)^R",
            interpret_formula(Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left='M', right='N'), right='O'), right='P'), right='Q'), right='R'))
        )

    def test_decode_disjunction(self):
        self.assertEqual(
            "PvQ",
            interpret_formula(Disjunction(left='P', right='Q'))
        )

        self.assertEqual(
            "(AvB)vC",
            interpret_formula(Disjunction(left=Disjunction(left='A', right='B'), right='C'))
        )

        self.assertEqual(
            "Dv(EvF)",
            interpret_formula(Disjunction(left='D', right=Disjunction(left='E', right='F')))
        )

        self.assertEqual(
            "(((PvQ)v(Rv(SvT)))v(Uv(Vv(Wv(XvY)))))vZ",
            interpret_formula(Disjunction(left=Disjunction(left=Disjunction(left=Disjunction(left='P', right='Q'), right=Disjunction(left='R', right=Disjunction(left='S', right='T'))), right=Disjunction(left='U', right=Disjunction(left='V', right=Disjunction(left='W', right=Disjunction(left='X', right='Y'))))), right='Z'))
        )

        self.assertEqual(
            "((JvK)vL)vM",
            interpret_formula(Disjunction(left=Disjunction(left=Disjunction(left='J', right='K'), right='L'), right='M'))
        )

    def test_decode_conditional(self):
        self.assertEqual(
            "P->Q",
            interpret_formula(Conditional(left='P', right='Q'))
        )

        self.assertEqual(
            "((P->(R->(T->V)))->(R->G))->R",
            interpret_formula(Conditional(left=Conditional(left=Conditional(left='P', right=Conditional(left='R', right=Conditional(left='T', right='V'))), right=Conditional(left='R', right='G')), right='R'))
        )

        self.assertEqual(
            "((A->(B->C))->(D->(E->F)))->G",
            interpret_formula(Conditional(left=Conditional(left=Conditional(left='A', right=Conditional(left='B', right='C')), right=Conditional(left='D', right=Conditional(left='E', right='F'))), right='G'))
        )

        self.assertEqual(
            "(((P->Q)->(R->S))->((T->U)->(V->W)))->X",
            interpret_formula(Conditional(left=Conditional(left=Conditional(left=Conditional(left='P', right='Q'), right=Conditional(left='R', right='S')), right=Conditional(left=Conditional(left='T', right='U'), right=Conditional(left='V', right='W'))), right='X'))
        )

        self.assertEqual(
            "((P->Q)->(R->(S->(T->(U->(V->(W->(X->(Y->Z)))))))))->(((A->B)->(C->(D->(E->(F->(G->(H->I)))))))->J)",
            interpret_formula(Conditional(left=Conditional(left=Conditional(left='P', right='Q'), right=Conditional(left='R', right=Conditional(left='S', right=Conditional(left='T', right=Conditional(left='U', right=Conditional(left='V', right=Conditional(left='W', right=Conditional(left='X', right=Conditional(left='Y', right='Z'))))))))), right=Conditional(left=Conditional(left=Conditional(left='A', right='B'), right=Conditional(left='C', right=Conditional(left='D', right=Conditional(left='E', right=Conditional(left='F', right=Conditional(left='G', right=Conditional(left='H', right='I'))))))), right='J')))
        )

    def test_decode_biconditional(self):
        self.assertEqual(
            "P<->Q",
            interpret_formula(BiConditional(left='P', right='Q'))
        )

        self.assertEqual(
            "(P<->Q)<->(R<->(S<->(T<->(U<->(V<->(W<->(X<->(Y<->Z))))))))",
            interpret_formula(BiConditional(left=BiConditional(left='P', right='Q'), right=BiConditional(left='R', right=BiConditional(left='S', right=BiConditional(left='T', right=BiConditional(left='U', right=BiConditional(left='V', right=BiConditional(left='W', right=BiConditional(left='X', right=BiConditional(left='Y', right='Z'))))))))))
        )

        self.assertEqual(
            "(P<->(Q<->(R<->(S<->(T<->U)))))<->V",
            interpret_formula(BiConditional(left=BiConditional(left='P', right=BiConditional(left='Q', right=BiConditional(left='R', right=BiConditional(left='S', right=BiConditional(left='T', right='U'))))), right='V'))
        )

        self.assertEqual(
            "(((((A<->B)<->C)<->D)<->E)<->F)<->G",
            interpret_formula(BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left='A', right='B'), right='C'), right='D'), right='E'), right='F'), right='G'))
        )

        self.assertEqual(
            "((((((((P<->Q)<->R)<->S)<->T)<->U)<->V)<->W)<->X)<->Y",
            interpret_formula(BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left='P', right='Q'), right='R'), right='S'), right='T'), right='U'), right='V'), right='W'), right='X'), right='Y'))
        )

    def test_decode_negation(self):
        self.assertEqual(
            "~P",
            interpret_formula(Negation(expr='P'))
        )

    def test_decode(self):
        self.assertEqual(
            "~((PvQ)v(P->(Q^R)))^((P<->R)v(T->U))",
            interpret_formula(Conjunction(left=Negation(expr=Disjunction(left=Disjunction(left='P', right='Q'), right=Conditional(left='P', right=Conjunction(left='Q', right='R')))), right=Disjunction(left=BiConditional(left='P', right='R'), right=Conditional(left='T', right='U'))))
        )

        self.assertEqual(
            "(PvQ)^~P",
            interpret_formula(Conjunction(left=Disjunction(left='P', right='Q'), right=Negation('P')))
        )

        self.assertEqual(
            "P->Q",
            interpret_formula(Conditional(left='P', right='Q'))
        )

        self.assertEqual(
            "~(P^Q)v((RvS)->((TvU)<->~W))",
            interpret_formula(Disjunction(left=Negation(expr=Conjunction(left='P', right='Q')), right=Conditional(left=Disjunction(left='R', right='S'), right=BiConditional(left=Disjunction(left='T', right='U'), right=Negation(expr='W')))))
        )

        self.assertEqual(
            "(A^(BvC))^((Dv(EvF))->((G<->(H<->I))^(J^(KvL))))",
            interpret_formula(Conjunction(left=Conjunction(left='A', right=Disjunction(left='B', right='C')), right=Conditional(left=Disjunction(left='D', right=Disjunction(left='E', right='F')), right=Conjunction(left=BiConditional(left='G', right=BiConditional(left='H', right='I')), right=Conjunction(left='J', right=Disjunction(left='K', right='L'))))))
        )

        self.assertEqual(
            "~(~(~(PvQ))v(~(RvS)->~((TvU)<->W)))",
            interpret_formula(Negation(expr=Disjunction(left=Negation(expr=Negation(expr=Disjunction(left='P', right='Q'))), right=Conditional(left=Negation(expr=Disjunction(left='R', right='S')), right=Negation(expr=BiConditional(left=Disjunction(left='T', right='U'), right='W'))))))
        )


if __name__ == '__main__':
    unittest.main()
