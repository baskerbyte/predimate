import unittest

from src.data.encode import encode_expression
from src.entity.operators import *


class TestEncode(unittest.TestCase):
    def test_encode_conjunction(self):
        self.assertEqual(
            Conjunction(left='P', right='Q'),
            encode_expression("(P^Q)")
        )

        self.assertEqual(
            Conjunction(left=Conjunction(left='A', right='B'), right='C'),
            encode_expression("((A^B)^C)")
        )

        self.assertEqual(
            Conjunction(left=Conjunction(left=Conjunction(left='D', right='E'), right='F'), right='G'),
            encode_expression("(((D^E)^F)^G)")
        )

        self.assertEqual(
            Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left='H', right='I'), right='J'), right='K'), right='L'),
            encode_expression("((((H^I)^J)^K)^L)")
        )

        self.assertEqual(
            Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left='M', right='N'), right='O'), right='P'), right='Q'), right='R'),
            encode_expression("(((((M^N)^O)^P)^Q)^R)")
        )

    def test_encode_disjunction(self):
        self.assertEqual(
            Disjunction(left='P', right='Q'),
            encode_expression("PvQ")
        )

        self.assertEqual(
            Disjunction(left=Disjunction(left='A', right='B'), right='C'),
            encode_expression("((AvB)vC)")
        )

        self.assertEqual(
            Disjunction(left='D', right=Disjunction(left='E', right='F')),
            encode_expression("Dv(EvF)")
        )

        self.assertEqual(
            Disjunction(left=Disjunction(left=Disjunction(left=Disjunction(left='P', right='Q'), right=Disjunction(left='R', right=Disjunction(left='S', right='T'))), right=Disjunction(left='U', right=Disjunction(left='V', right=Disjunction(left='W', right=Disjunction(left='X', right='Y'))))), right='Z'),
            encode_expression("(((PvQ)v(Rv(SvT)))v(Uv(Vv(Wv(XvY)))))vZ")
        )

        self.assertEqual(
            Disjunction(left=Disjunction(left=Disjunction(left='J', right='K'), right='L'), right='M'),
            encode_expression("((JvK)vL)vM")
        )

    def test_encode_conditional(self):
        self.assertEqual(
            Conditional(left='P', right='Q'),
            encode_expression("P->Q")
        )

        self.assertEqual(
            Conditional(left=Conditional(left=Conditional(left='P', right=Conditional(left='R', right=Conditional(left='T', right='V'))), right=Conditional(left='R', right='G')), right='R'),
            encode_expression("((P->(R->(T->V)))->(R->G))->R")
        )

        self.assertEqual(
            Conditional(left=Conditional(left=Conditional(left='A', right=Conditional(left='B', right='C')), right=Conditional(left='D', right=Conditional(left='E', right='F'))), right='G'),
            encode_expression("((A->(B->C))->(D->(E->F)))->G")
        )

        self.assertEqual(
            Conditional(left=Conditional(left=Conditional(left=Conditional(left='P', right='Q'), right=Conditional(left='R', right='S')), right=Conditional(left=Conditional(left='T', right='U'), right=Conditional(left='V', right='W'))), right='X'),
            encode_expression("(((P->Q)->(R->S))->((T->U)->(V->W)))->X")
        )

        self.assertEqual(
            Conditional(left=Conditional(left=Conditional(left='P', right='Q'), right=Conditional(left='R', right=Conditional(left='S', right=Conditional(left='T', right=Conditional(left='U', right=Conditional(left='V', right=Conditional(left='W', right=Conditional(left='X', right=Conditional(left='Y', right='Z'))))))))), right=Conditional(left=Conditional(left=Conditional(left='A', right='B'), right=Conditional(left='C', right=Conditional(left='D', right=Conditional(left='E', right=Conditional(left='F', right=Conditional(left='G', right=Conditional(left='H', right='I'))))))), right='J')),
            encode_expression("((P->Q)->(R->(S->(T->(U->(V->(W->(X->(Y->Z)))))))))->(((A->B)->(C->(D->(E->(F->(G->(H->I)))))))->J)")
        )

    def test_encode_biconditional(self):
        self.assertEqual(
            BiConditional(left='P', right='Q'),
            encode_expression("P<->Q")
        )

        self.assertEqual(
            BiConditional(left=BiConditional(left='P', right='Q'), right=BiConditional(left='R', right=BiConditional(left='S', right=BiConditional(left='T', right=BiConditional(left='U', right=BiConditional(left='V', right=BiConditional(left='W', right=BiConditional(left='X', right=BiConditional(left='Y', right='Z'))))))))),
            encode_expression("(P<->Q)<->(R<->(S<->(T<->(U<->(V<->(W<->(X<->(Y<->Z))))))))"),
        )

        self.assertEqual(
            BiConditional(left=BiConditional(left='P', right=BiConditional(left='Q', right=BiConditional(left='R', right=BiConditional(left='S', right=BiConditional(left='T', right='U'))))), right='V'),
            encode_expression("(P<->(Q<->(R<->(S<->(T<->U)))))<->V"),
        )

        self.assertEqual(
            BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left='A', right='B'), right='C'), right='D'), right='E'), right='F'), right='G'),
            encode_expression("(((((A<->B)<->C)<->D)<->E)<->F)<->G"),
        )

        self.assertEqual(
            BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left='P', right='Q'), right='R'), right='S'), right='T'), right='U'), right='V'), right='W'), right='X'), right='Y'),
            encode_expression("((((((((P<->Q)<->R)<->S)<->T)<->U)<->V)<->W)<->X)<->Y")
        )

    def test_encode_negation(self):
        self.assertEqual(
            Negation(expr='P'),
            encode_expression("~P")
        )

    def test_encode(self):
        self.assertEqual(
            Conjunction(left=Negation(expr=Disjunction(left=Disjunction(left='P', right='Q'), right=Conditional(left='P', right=Conjunction(left='Q', right='R')))), right=Disjunction(left=BiConditional(left='P', right='R'), right=Conditional(left='T', right='U'))),
            encode_expression("~((PvQ)v(P->(Q^R)))^((P<->R)v(T->U))")
        )

        self.assertEqual(
            Conjunction(left=Disjunction(left='P', right='Q'), right=Negation(expr='P')),
            encode_expression("(PvQ)^~P"),
        )

        self.assertEqual(
            Disjunction(left=Negation(expr=Conjunction(left='P', right='Q')), right=Conditional(left=Disjunction(left='R', right='S'), right=BiConditional(left=Disjunction(left='T', right='U'), right=Negation(expr='W')))),
            encode_expression("~(P^Q)v((RvS)->((TvU)<->~W))")
        )

        self.assertEqual(
            Conjunction(left=Conjunction(left='A', right=Disjunction(left='B', right='C')), right=Conditional(left=Disjunction(left='D', right=Disjunction(left='E', right='F')), right=Conjunction(left=BiConditional(left='G', right=BiConditional(left='H', right='I')), right=Conjunction(left='J', right=Disjunction(left='K', right='L'))))),
            encode_expression("(A^(BvC))^((Dv(EvF))->((G<->(H<->I))^(J^(KvL))))")
        )

        self.assertEqual(
            Negation(expr=Disjunction(left=Negation(expr=Negation(expr=Disjunction(left='P', right='Q'))), right=Conditional(left=Negation(expr=Disjunction(left='R', right='S')), right=Negation(expr=BiConditional(left=Disjunction(left='T', right='U'), right='W'))))),
            encode_expression("~(~(~(PvQ))v(~(RvS)->~((TvU)<->W)))")
        )


if __name__ == '__main__':
    unittest.main()
