import unittest

from src.data.decode import decode_expression
from src.entity.operators import *


class TestDecode(unittest.TestCase):
    def test_decode_conjunction(self):
        self.assertEqual(
            "P^Q",
            decode_expression(Conjunction(left=Preposition(prep='P'), right=Preposition('Q')))
        )

        self.assertEqual(
            "(A^B)^C",
            decode_expression(Conjunction(left=Conjunction(left=Preposition(prep='A'), right=Preposition(prep='B')), right=Preposition(prep='C')))
        )

        self.assertEqual(
            "((D^E)^F)^G",
            decode_expression(Conjunction(left=Conjunction(left=Conjunction(left=Preposition(prep='D'), right=Preposition(prep='E')), right=Preposition(prep='F')), right=Preposition(prep='G')))
        )

        self.assertEqual(
            "(((H^I)^J)^K)^L",
            decode_expression(Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left=Preposition(prep='H'), right=Preposition(prep='I')), right=Preposition(prep='J')), right=Preposition(prep='K')), right=Preposition(prep='L')))
        )

        self.assertEqual(
            "((((M^N)^O)^P)^Q)^R",
            decode_expression(Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left='M', right='N'), right='O'), right='P'), right='Q'), right='R'))
        )

    def test_decode_disjunction(self):
        self.assertEqual(
            "PvQ",
            decode_expression(Disjunction(left='P', right='Q'))
        )

        self.assertEqual(
            "(AvB)vC",
            decode_expression(Disjunction(left=Disjunction(left='A', right='B'), right='C'))
        )

        self.assertEqual(
            "Dv(EvF)",
            decode_expression(Disjunction(left='D', right=Disjunction(left='E', right='F')))
        )

        self.assertEqual(
            "(((PvQ)v(Rv(SvT)))v(Uv(Vv(Wv(XvY)))))vZ",
            decode_expression(Disjunction(left=Disjunction(left=Disjunction(left=Disjunction(left='P', right='Q'), right=Disjunction(left='R', right=Disjunction(left='S', right='T'))), right=Disjunction(left='U', right=Disjunction(left='V', right=Disjunction(left='W', right=Disjunction(left='X', right='Y'))))), right='Z'))
        )

        self.assertEqual(
            "((JvK)vL)vM",
            decode_expression(Disjunction(left=Disjunction(left=Disjunction(left='J', right='K'), right='L'), right='M'))
        )

    def test_decode_conditional(self):
        self.assertEqual(
            "P->Q",
            decode_expression(Conditional(left='P', right='Q'))
        )

        self.assertEqual(
            "((P->(R->(T->V)))->(R->G))->R",
            decode_expression(Conditional(left=Conditional(left=Conditional(left='P', right=Conditional(left='R', right=Conditional(left='T', right='V'))), right=Conditional(left='R', right='G')), right='R'))
        )

        self.assertEqual(
            "((A->(B->C))->(D->(E->F)))->G",
            decode_expression(Conditional(left=Conditional(left=Conditional(left='A', right=Conditional(left='B', right='C')), right=Conditional(left='D', right=Conditional(left='E', right='F'))), right='G'))
        )

        self.assertEqual(
            "(((P->Q)->(R->S))->((T->U)->(V->W)))->X",
            decode_expression(Conditional(left=Conditional(left=Conditional(left=Conditional(left='P', right='Q'), right=Conditional(left='R', right='S')), right=Conditional(left=Conditional(left='T', right='U'), right=Conditional(left='V', right='W'))), right='X'))
        )

        self.assertEqual(
            "((P->Q)->(R->(S->(T->(U->(V->(W->(X->(Y->Z)))))))))->(((A->B)->(C->(D->(E->(F->(G->(H->I)))))))->J)",
            decode_expression(Conditional(left=Conditional(left=Conditional(left='P', right='Q'), right=Conditional(left='R', right=Conditional(left='S', right=Conditional(left='T', right=Conditional(left='U', right=Conditional(left='V', right=Conditional(left='W', right=Conditional(left='X', right=Conditional(left='Y', right='Z'))))))))), right=Conditional(left=Conditional(left=Conditional(left='A', right='B'), right=Conditional(left='C', right=Conditional(left='D', right=Conditional(left='E', right=Conditional(left='F', right=Conditional(left='G', right=Conditional(left='H', right='I'))))))), right='J')))
        )

    def test_decode_biconditional(self):
        self.assertEqual(
            "P<->Q",
            decode_expression(BiConditional(left='P', right='Q'))
        )

        self.assertEqual(
            "(P<->Q)<->(R<->(S<->(T<->(U<->(V<->(W<->(X<->(Y<->Z))))))))",
            decode_expression(BiConditional(left=BiConditional(left='P', right='Q'), right=BiConditional(left='R', right=BiConditional(left='S', right=BiConditional(left='T', right=BiConditional(left='U', right=BiConditional(left='V', right=BiConditional(left='W', right=BiConditional(left='X', right=BiConditional(left='Y', right='Z'))))))))))
        )

        self.assertEqual(
            "(P<->(Q<->(R<->(S<->(T<->U)))))<->V",
            decode_expression(BiConditional(left=BiConditional(left='P', right=BiConditional(left='Q', right=BiConditional(left='R', right=BiConditional(left='S', right=BiConditional(left='T', right='U'))))), right='V'))
        )

        self.assertEqual(
            "(((((A<->B)<->C)<->D)<->E)<->F)<->G",
            decode_expression(BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left='A', right='B'), right='C'), right='D'), right='E'), right='F'), right='G'))
        )

        self.assertEqual(
            "((((((((P<->Q)<->R)<->S)<->T)<->U)<->V)<->W)<->X)<->Y",
            decode_expression(BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left='P', right='Q'), right='R'), right='S'), right='T'), right='U'), right='V'), right='W'), right='X'), right='Y'))
        )

    def test_decode_negation(self):
        self.assertEqual(
            "~P",
            decode_expression(Negation(expr='P'))
        )

    def test_decode(self):
        self.assertEqual(
            "~((PvQ)v(P->(Q^R)))^((P<->R)v(T->U))",
            decode_expression(Conjunction(left=Negation(expr=Disjunction(left=Disjunction(left='P', right='Q'), right=Conditional(left='P', right=Conjunction(left='Q', right='R')))), right=Disjunction(left=BiConditional(left='P', right='R'), right=Conditional(left='T', right='U'))))
        )

        self.assertEqual(
            "(PvQ)^~P",
            decode_expression(Conjunction(left=Disjunction(left='P', right='Q'), right=Negation('P')))
        )

        self.assertEqual(
            "P->Q",
            decode_expression(Conditional(left='P', right='Q'))
        )

        self.assertEqual(
            "~(P^Q)v((RvS)->((TvU)<->~W))",
            decode_expression(Disjunction(left=Negation(expr=Conjunction(left='P', right='Q')), right=Conditional(left=Disjunction(left='R', right='S'), right=BiConditional(left=Disjunction(left='T', right='U'), right=Negation(expr='W')))))
        )

        self.assertEqual(
            "(A^(BvC))^((Dv(EvF))->((G<->(H<->I))^(J^(KvL))))",
            decode_expression(Conjunction(left=Conjunction(left='A', right=Disjunction(left='B', right='C')), right=Conditional(left=Disjunction(left='D', right=Disjunction(left='E', right='F')), right=Conjunction(left=BiConditional(left='G', right=BiConditional(left='H', right='I')), right=Conjunction(left='J', right=Disjunction(left='K', right='L'))))))
        )

        self.assertEqual(
            "~(~(~(PvQ))v(~(RvS)->~((TvU)<->W)))",
            decode_expression(Negation(expr=Disjunction(left=Negation(expr=Negation(expr=Disjunction(left='P', right='Q'))), right=Conditional(left=Negation(expr=Disjunction(left='R', right='S')), right=Negation(expr=BiConditional(left=Disjunction(left='T', right='U'), right='W'))))))
        )


if __name__ == '__main__':
    unittest.main()
