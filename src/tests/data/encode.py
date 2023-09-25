import unittest

from src.data.encode import wrap_formula
from src.entity.operators import *


class TestEncode(unittest.TestCase):
    def test_encode_conjunction(self):
        self.assertEqual(
            wrap_formula("(P^Q)"),
            Conjunction(left='P', right='Q')
        )

        self.assertEqual(
            wrap_formula("((A^B)^C)"),
            Conjunction(left=Conjunction(left='A', right='B'), right='C')
        )

        self.assertEqual(
            wrap_formula("(((D^E)^F)^G)"),
            Conjunction(left=Conjunction(left=Conjunction(left='D', right='E'), right='F'), right='G')
        )

        self.assertEqual(
            wrap_formula("((((H^I)^J)^K)^L)"),
            Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left='H', right='I'), right='J'), right='K'), right='L')
        )

        self.assertEqual(
            wrap_formula("(((((M^N)^O)^P)^Q)^R)"),
            Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left='M', right='N'), right='O'), right='P'), right='Q'), right='R')
        )

    def test_encode_disjunction(self):
        self.assertEqual(
            wrap_formula("PvQ"),
            Disjunction(left='P', right='Q')
        )

        self.assertEqual(
            wrap_formula("((AvB)vC)"),
            Disjunction(left=Disjunction(left='A', right='B'), right='C')
        )

        self.assertEqual(
            wrap_formula("Dv(EvF)"),
            Disjunction(left='D', right=Disjunction(left='E', right='F'))
        )

        self.assertEqual(
            wrap_formula("(((PvQ)v(Rv(SvT)))v(Uv(Vv(Wv(XvY)))))vZ"),
            Disjunction(left=Disjunction(left=Disjunction(left=Disjunction(left='P', right='Q'), right=Disjunction(left='R', right=Disjunction(left='S', right='T'))), right=Disjunction(left='U', right=Disjunction(left='V', right=Disjunction(left='W', right=Disjunction(left='X', right='Y'))))), right='Z')
        )

        self.assertEqual(
            wrap_formula("((JvK)vL)vM"),
            Disjunction(left=Disjunction(left=Disjunction(left='J', right='K'), right='L'), right='M')
        )

    def test_encode_conditional(self):
        self.assertEqual(
            wrap_formula("P->Q"),
            Conditional(left='P', right='Q')
        )

        self.assertEqual(
            wrap_formula("((P->(R->(T->V)))->(R->G))->R"),
            Conditional(left=Conditional(left=Conditional(left='P', right=Conditional(left='R', right=Conditional(left='T', right='V'))), right=Conditional(left='R', right='G')), right='R')
        )

        self.assertEqual(
            wrap_formula("((A->(B->C))->(D->(E->F)))->G"),
            Conditional(left=Conditional(left=Conditional(left='A', right=Conditional(left='B', right='C')), right=Conditional(left='D', right=Conditional(left='E', right='F'))), right='G')
        )

        self.assertEqual(
            wrap_formula("(((P->Q)->(R->S))->((T->U)->(V->W)))->X"),
            Conditional(left=Conditional(left=Conditional(left=Conditional(left='P', right='Q'), right=Conditional(left='R', right='S')), right=Conditional(left=Conditional(left='T', right='U'), right=Conditional(left='V', right='W'))), right='X')
        )

        self.assertEqual(
            wrap_formula("((P->Q)->(R->(S->(T->(U->(V->(W->(X->(Y->Z)))))))))->(((A->B)->(C->(D->(E->(F->(G->(H->I)))))))->J)"),
            Conditional(left=Conditional(left=Conditional(left='P', right='Q'), right=Conditional(left='R', right=Conditional(left='S', right=Conditional(left='T', right=Conditional(left='U', right=Conditional(left='V', right=Conditional(left='W', right=Conditional(left='X', right=Conditional(left='Y', right='Z'))))))))), right=Conditional(left=Conditional(left=Conditional(left='A', right='B'), right=Conditional(left='C', right=Conditional(left='D', right=Conditional(left='E', right=Conditional(left='F', right=Conditional(left='G', right=Conditional(left='H', right='I'))))))), right='J'))
        )

    def test_encode_biconditional(self):
        self.assertEqual(
            wrap_formula("P<->Q"),
            BiConditional(left='P', right='Q')
        )

        self.assertEqual(
            wrap_formula("(P<->Q)<->(R<->(S<->(T<->(U<->(V<->(W<->(X<->(Y<->Z))))))))"),
            BiConditional(left=BiConditional(left='P', right='Q'), right=BiConditional(left='R', right=BiConditional(left='S', right=BiConditional(left='T', right=BiConditional(left='U', right=BiConditional(left='V', right=BiConditional(left='W', right=BiConditional(left='X', right=BiConditional(left='Y', right='Z')))))))))
        )

        self.assertEqual(
            wrap_formula("(P<->(Q<->(R<->(S<->(T<->U)))))<->V"),
            BiConditional(left=BiConditional(left='P', right=BiConditional(left='Q', right=BiConditional(left='R', right=BiConditional(left='S', right=BiConditional(left='T', right='U'))))), right='V')
        )

        self.assertEqual(
            wrap_formula("(((((A<->B)<->C)<->D)<->E)<->F)<->G"),
            BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left='A', right='B'), right='C'), right='D'), right='E'), right='F'), right='G')
        )

        self.assertEqual(
            wrap_formula("((((((((P<->Q)<->R)<->S)<->T)<->U)<->V)<->W)<->X)<->Y"),
            BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left='P', right='Q'), right='R'), right='S'), right='T'), right='U'), right='V'), right='W'), right='X'), right='Y')
        )

    def test_encode_negation(self):
        self.assertEqual(
            wrap_formula("~P"),
            Negation(expr='P')
        )

    def test_encode(self):
        self.assertEqual(
            wrap_formula("~((PvQ)v(P->(Q^R)))^((P<->R)v(T->U))"),
            Conjunction(left=Negation(expr=Disjunction(left=Disjunction(left='P', right='Q'), right=Conditional(left='P', right=Conjunction(left='Q', right='R')))), right=Disjunction(left=BiConditional(left='P', right='R'), right=Conditional(left='T', right='U')))
        )

        self.assertEqual(
            wrap_formula("(PvQ)^~P"),
            Conjunction(left=Disjunction(left='P', right='Q'), right=Negation(expr='P'))
        )

        self.assertEqual(
            wrap_formula("~(P^Q)v((RvS)->((TvU)<->~W))"),
            Disjunction(left=Negation(expr=Conjunction(left='P', right='Q')), right=Conditional(left=Disjunction(left='R', right='S'), right=BiConditional(left=Disjunction(left='T', right='U'), right=Negation(expr='W'))))
        )

        self.assertEqual(
            wrap_formula("(A^(BvC))^((Dv(EvF))->((G<->(H<->I))^(J^(KvL))))"),
            Conjunction(left=Conjunction(left='A', right=Disjunction(left='B', right='C')), right=Conditional(left=Disjunction(left='D', right=Disjunction(left='E', right='F')), right=Conjunction(left=BiConditional(left='G', right=BiConditional(left='H', right='I')), right=Conjunction(left='J', right=Disjunction(left='K', right='L')))))
        )

        self.assertEqual(
            wrap_formula("~(~(~(PvQ))v(~(RvS)->~((TvU)<->W)))"),
            Disjunction(left=Negation(expr=Negation(expr=Negation(expr=Disjunction(left='P', right='Q')))), right=Conditional(left=Negation(expr=Disjunction(left='R', right='S')), right=Negation(expr=BiConditional(left=Disjunction(left='T', right='U'), right='W'))))
        )


if __name__ == '__main__':
    unittest.main()
