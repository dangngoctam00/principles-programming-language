import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    # def test_380(self):
    #     input = """
    #         Var: x[3] = {0xA12, 0o7777, 0O123, 0XFFFFF};
    #         Var: x[3][0xAAA][0O12370], f = {2,3,4, True, False, "\\n\\f\\bstring\\b'\""};
    #         Function: func
    #         Body:  
    #             If x == 10.e+56 Then
    #                 If y =/= "'\"\\n\\b\\\\" Then
    #                     Do 
    #                         x = x -. 3;
    #                         func();
    #                         Return;
    #                         Continue;
    #                         Break;
    #                         f = !(a <. (b <= (c >= (d =/= (f == (g != (z >. (y >= t || f && g + f *. y \\. u % p \\ u))))))));
    #                     While x != 3.e-3 EndDo.
    #                 EndIf.
    #             EndIf.
    #         EndBody.
    #     """
    #     expect = []
    #     self.assertTrue(TestParser.checkParser(input, expect, 380))
    def test_374(self):
        input = """
        Var: a = True, d;
        Function: foods
        Parameter: a[123], b
        Body:
            c[2][3] = 5*10;
        EndBody.
        """
        # expect = Program([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("d"),[],None),FuncDecl(Id("foods"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",ArrayCell(Id("a"),[IntLiteral(12)]),Id("b")),[],[Dowhile(([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("d"),[],None)],[Assign(Id("a"),BinaryOp("||",BinaryOp("=/=",BinaryOp("-",BinaryOp("+",Id("b"),IntLiteral(3)),BinaryOp("*",Id("c"),Id("d"))),IntLiteral(5)),BinaryOp("<.",BinaryOp("-",Id("b"),Id("d")),IntLiteral(10)))),Assign(ArrayCell(ArrayCell(Id("c"),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp("+",BinaryOp("\.",BinaryOp("\\",IntLiteral(5),FloatLiteral(10.2)),CallExpr(Id("func"),[Id("a"),Id("b"),Id("c")])),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))])))]),BinaryOp("==",Id("x"),Id("y")))])],([],[]))])),FuncDecl(Id("abc"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Dowhile(([],[CallStmt(Id("foods"),[Id("a"),Id("v"),Id("t")])]),BinaryOp("+",Id("x"),Id("y")))]))])
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 374))