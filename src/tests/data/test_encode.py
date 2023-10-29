import unittest

from src.data.encode import encode_expression
from src.entity.operators import *


class TestEncode(unittest.TestCase):
    def test_encode_conjunction(self):
        self.assertEqual(
            Conjunction(left=Preposition(prep='P'), right=Preposition('Q')),
            encode_expression("(P^Q)")
        )

        self.assertEqual(
            Conjunction(left=Conjunction(left=Preposition(prep='A'), right=Preposition(prep='B')), right=Preposition(prep='C')),
            encode_expression("((A^B)^C)")
        )

        self.assertEqual(
            Conjunction(left=Conjunction(left=Conjunction(left=Preposition(prep='D'), right=Preposition(prep='E')), right=Preposition(prep='F')), right=Preposition(prep='G')),
            encode_expression("(((D^E)^F)^G)")
        )

        self.assertEqual(
            Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left=Preposition(prep='H'), right=Preposition(prep='I')), right=Preposition(prep='J')), right=Preposition(prep='K')), right=Preposition(prep='L')),
            encode_expression("((((H^I)^J)^K)^L)")
        )

        self.assertEqual(
            Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left=Conjunction(left=Preposition(prep='M'), right=Preposition(prep='N')), right=Preposition(prep='O')), right=Preposition(prep='P')), right=Preposition(prep='Q')), right=Preposition(prep='R')),
            encode_expression("(((((M^N)^O)^P)^Q)^R)")
        )

    def test_encode_disjunction(self):
        self.assertEqual(
            Disjunction(left=Preposition(prep='P'), right=Preposition(prep='Q')),
            encode_expression("PvQ")
        )

        self.assertEqual(
            Disjunction(left=Disjunction(left=Preposition(prep='A'), right=Preposition(prep='B')), right=Preposition(prep='C')),
            encode_expression("((AvB)vC)")
        )

        self.assertEqual(
            Disjunction(left=Preposition(prep='D'), right=Disjunction(left=Preposition(prep='E'), right=Preposition(prep='F'))),
            encode_expression("Dv(EvF)")
        )

        self.assertEqual(
            Disjunction(left=Disjunction(left=Disjunction(left=Disjunction(left=Preposition(prep='P'), right=Preposition(prep='Q')), right=Disjunction(left=Preposition(prep='R'), right=Disjunction(left=Preposition(prep='S'), right=Preposition(prep='T')))), right=Disjunction(left=Preposition(prep='U'), right=Disjunction(left=Preposition(prep='V'), right=Disjunction(left=Preposition(prep='W'), right=Disjunction(left=Preposition(prep='X'), right=Preposition(prep='Y')))))), right=Preposition(prep='Z')),
            encode_expression("(((PvQ)v(Rv(SvT)))v(Uv(Vv(Wv(XvY)))))vZ")
        )

        self.assertEqual(
            Disjunction(left=Disjunction(left=Disjunction(left=Preposition(prep='J'), right=Preposition(prep='K')), right=Preposition(prep='L')), right=Preposition(prep='M')),
            encode_expression("((JvK)vL)vM")
        )

    def test_encode_conditional(self):
        self.assertEqual(
            Conditional(left=Preposition(prep='P'), right=Preposition(prep='Q')),
            encode_expression("P->Q")
        )

        self.assertEqual(
            Conditional(left=Conditional(left=Conditional(left=Preposition(prep='P'), right=Conditional(left=Preposition(prep='R'), right=Conditional(left=Preposition(prep='T'), right=Preposition(prep='V')))), right=Conditional(left=Preposition(prep='R'), right=Preposition(prep='G'))), right=Preposition(prep='R')),
            encode_expression("((P->(R->(T->V)))->(R->G))->R")
        )

        self.assertEqual(
            Conditional(left=Conditional(left=Conditional(left=Preposition(prep='A'), right=Conditional(left=Preposition(prep='B'), right=Preposition(prep='C'))), right=Conditional(left=Preposition(prep='D'), right=Conditional(left=Preposition(prep='E'), right=Preposition(prep='F')))), right=Preposition(prep='G')),
            encode_expression("((A->(B->C))->(D->(E->F)))->G")
        )

        self.assertEqual(
            Conditional(left=Conditional(left=Conditional(left=Conditional(left=Preposition(prep='P'), right=Preposition(prep='Q')), right=Conditional(left=Preposition(prep='R'), right=Preposition(prep='S'))), right=Conditional(left=Conditional(left=Preposition(prep='T'), right=Preposition(prep='U')), right=Conditional(left=Preposition(prep='V'), right=Preposition(prep='W')))), right=Preposition(prep='X')),
            encode_expression("(((P->Q)->(R->S))->((T->U)->(V->W)))->X")
        )

        self.assertEqual(
            Conditional(left=Conditional(left=Conditional(left=Preposition(prep='P'), right=Preposition(prep='Q')), right=Conditional(left=Preposition(prep='R'), right=Conditional(left=Preposition(prep='S'), right=Conditional(left=Preposition(prep='T'), right=Conditional(left=Preposition(prep='U'), right=Conditional(left=Preposition(prep='V'), right=Conditional(left=Preposition(prep='W'), right=Conditional(left=Preposition(prep='X'), right=Conditional(left=Preposition(prep='Y'), right=Preposition(prep='Z')))))))))), right=Conditional(left=Conditional(left=Conditional(left=Preposition(prep='A'), right=Preposition(prep='B')), right=Conditional(left=Preposition(prep='C'), right=Conditional(left=Preposition(prep='D'), right=Conditional(left=Preposition(prep='E'), right=Conditional(left=Preposition(prep='F'), right=Conditional(left=Preposition(prep='G'), right=Conditional(left=Preposition(prep='H'), right=Preposition(prep='I')))))))), right=Preposition(prep='J'))),            encode_expression("((P->Q)->(R->(S->(T->(U->(V->(W->(X->(Y->Z)))))))))->(((A->B)->(C->(D->(E->(F->(G->(H->I)))))))->J)")
        )

    def test_encode_biconditional(self):
        self.assertEqual(
            BiConditional(left=Preposition(prep='P'), right=Preposition(prep='Q')),
            encode_expression("P<->Q")
        )

        self.assertEqual(
            BiConditional(left=BiConditional(left=Preposition(prep='P'), right=Preposition(prep='Q')), right=BiConditional(left=Preposition(prep='R'), right=BiConditional(left=Preposition(prep='S'), right=BiConditional(left=Preposition(prep='T'), right=BiConditional(left=Preposition(prep='U'), right=BiConditional(left=Preposition(prep='V'), right=BiConditional(left=Preposition(prep='W'), right=BiConditional(left=Preposition(prep='X'), right=BiConditional(left=Preposition(prep='Y'), right=Preposition(prep='Z')))))))))),
            encode_expression("(P<->Q)<->(R<->(S<->(T<->(U<->(V<->(W<->(X<->(Y<->Z))))))))"),
        )

        self.assertEqual(
            BiConditional(left=BiConditional(left=Preposition(prep='P'), right=BiConditional(left=Preposition(prep='Q'), right=BiConditional(left=Preposition(prep='R'), right=BiConditional(left=Preposition(prep='S'), right=BiConditional(left=Preposition(prep='T'), right=Preposition(prep='U')))))), right=Preposition(prep='V')),
            encode_expression("(P<->(Q<->(R<->(S<->(T<->U)))))<->V"),
        )

        self.assertEqual(
            BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=Preposition(prep='A'), right=Preposition(prep='B')), right=Preposition(prep='C')), right=Preposition(prep='D')), right=Preposition(prep='E')), right=Preposition(prep='F')), right=Preposition(prep='G')),
            encode_expression("(((((A<->B)<->C)<->D)<->E)<->F)<->G"),
        )

        self.assertEqual(
            BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=BiConditional(left=Preposition(prep='P'), right=Preposition(prep='Q')), right=Preposition(prep='R')), right=Preposition(prep='S')), right=Preposition(prep='T')), right=Preposition(prep='U')), right=Preposition(prep='V')), right=Preposition(prep='W')), right=Preposition(prep='X')), right=Preposition(prep='Y')),
            encode_expression("((((((((P<->Q)<->R)<->S)<->T)<->U)<->V)<->W)<->X)<->Y")
        )

    def test_encode_negation(self):
        self.assertEqual(
            Negation(expr=Preposition(prep='P')),
            encode_expression("~P")
        )

    def test_encode(self):
        self.assertEqual(
            Conjunction(left=Negation(expr=Disjunction(left=Disjunction(left=Preposition(prep='P'), right=Preposition(prep='Q')), right=Conditional(left=Preposition(prep='P'), right=Conjunction(left=Preposition(prep='Q'), right=Preposition(prep='R'))))), right=Disjunction(left=BiConditional(left=Preposition(prep='P'), right=Preposition(prep='R')), right=Conditional(left=Preposition(prep='T'), right=Preposition(prep='U')))),
            encode_expression("~((PvQ)v(P->(Q^R)))^((P<->R)v(T->U))")
        )

        self.assertEqual(
            Conjunction(left=Disjunction(left=Preposition(prep='P'), right=Preposition(prep='Q')), right=Negation(expr=Preposition(prep='P'))),
            encode_expression("(PvQ)^~P"),
        )

        self.assertEqual(
            Disjunction(left=Negation(expr=Conjunction(left=Preposition(prep='P'), right=Preposition(prep='Q'))), right=Conditional(left=Disjunction(left=Preposition(prep='R'), right=Preposition(prep='S')), right=BiConditional(left=Disjunction(left=Preposition(prep='T'), right=Preposition(prep='U')), right=Negation(expr=Preposition(prep='W'))))),
            encode_expression("~(P^Q)v((RvS)->((TvU)<->~W))")
        )

        self.assertEqual(
            Conjunction(left=Conjunction(left=Preposition(prep='A'), right=Disjunction(left=Preposition(prep='B'), right=Preposition(prep='C'))), right=Conditional(left=Disjunction(left=Preposition(prep='D'), right=Disjunction(left=Preposition(prep='E'), right=Preposition(prep='F'))), right=Conjunction(left=BiConditional(left=Preposition(prep='G'), right=BiConditional(left=Preposition(prep='H'), right=Preposition(prep='I'))), right=Conjunction(left=Preposition(prep='J'), right=Disjunction(left=Preposition(prep='K'), right=Preposition(prep='L')))))),
            encode_expression("(A^(BvC))^((Dv(EvF))->((G<->(H<->I))^(J^(KvL))))")
        )

        self.assertEqual(
            Negation(expr=Disjunction(left=Negation(expr=Negation(expr=Disjunction(left=Preposition(prep='P'), right=Preposition(prep='Q')))), right=Conditional(left=Negation(expr=Disjunction(left=Preposition(prep='R'), right=Preposition(prep='S'))), right=Negation(expr=BiConditional(left=Disjunction(left=Preposition(prep='T'), right=Preposition(prep='U')), right=Preposition(prep='W')))))),
            encode_expression("~(~(~(PvQ))v(~(RvS)->~((TvU)<->W)))")
        )


if __name__ == '__main__':
    unittest.main()
