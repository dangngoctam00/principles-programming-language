import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_301(self):
        input = """Var:a[2] = {7,2, {9, {2}}}, c = "d", b = False;"""
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([IntLiteral(7),IntLiteral(2),ArrayLiteral([IntLiteral(9),ArrayLiteral([IntLiteral(2)])])])),VarDecl(Id("c"),[],StringLiteral("d")),VarDecl(Id("b"),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_302(self):
        input = """ Var: x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_303(self):
        input = """Var: x[5] = {  {2 ,   3,5    },  {3,    3}    ,{4}   }; """
        expect = Program([VarDecl(Id("x"),[5],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(5)]),ArrayLiteral([IntLiteral(3),IntLiteral(3)]),ArrayLiteral([IntLiteral(4)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_304(self):
        input = """ Function: main
        Body:
        Var: x,y,z;
        x = 10;
        fact (x);
        EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))
    def test_305(self):
        input = """Var: x;
    Function: fact
    Parameter: n
    Body:
    If (n == 0) Then
    Return 1;
    EndIf.
    EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("fact"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))
    def test_306(self):
        input = """Function: foo
                Parameter: z
                Body:
                Var: x,y;
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))
    def test_307(self):
        input = """Function: foo
                Parameter: z
                Body:
                a = 1;
                b = 2;
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([],[Assign(Id("a"),IntLiteral(1)),Assign(Id("b"),IntLiteral(2))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))
    def test_308(self):
        input = """Function: foo
                Parameter: z
                Body:
                a = fun(2);
                b = a;
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([],[Assign(Id("a"),CallExpr(Id("fun"),[IntLiteral(2)])),Assign(Id("b"),Id("a"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))
    def test_309(self):
        input = """ Function: foo
                Parameter: z
                Body:
                Var: x[5],y;
                x = 4;
                y = 10 + 26 + x;
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([VarDecl(Id("x"),[5],None),VarDecl(Id("y"),[],None)],[Assign(Id("x"),IntLiteral(4)),Assign(Id("y"),BinaryOp("+",BinaryOp("+",IntLiteral(10),IntLiteral(26)),Id("x")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))
    def test_310(self):
        input = """Function: foo
                Parameter: z
                Body:
                Var:x,y;
                y = x;
                x = foo(2);
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[Assign(Id("y"),Id("x")),Assign(Id("x"),CallExpr(Id("foo"),[IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))
    def test_311(self):
        input = """Function: foo
                Parameter: z
                Body:
                a = foo(4);
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(4)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))
    def test_312(self):
        input = """Function: foo
                Parameter: z
                Body:
                x[5] = 123 + z % 5;
                x = 7;
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([],[Assign(ArrayCell(Id("x"),[IntLiteral(5)]),BinaryOp("+",IntLiteral(123),BinaryOp("%",Id("z"),IntLiteral(5)))),Assign(Id("x"),IntLiteral(7))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))
    def test_313(self):
        input = """Function: foo
                Parameter: z
                Body:
                Var: x,y;
                If n == 0 Then
                Return 1;
                Else
                Return n * fact (n - 1);
                EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))
    def test_314(self):
        input = """Function: foo
                Parameter: z
                Body:
                Var:x,y;
                If n == 0 Then
                Return 1;
                EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))
    def test_315(self):
        input = """Function: foo
                Parameter: z
                Body:
                Var:x,y;
                If n == 0 Then
                Return 1;
                ElseIf n == 1 Then
                Return n * fact (n - 1);
                EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))]),(BinaryOp("==",Id("n"),IntLiteral(1)),[],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))
    def test_316(self):
        input = """ Function: foo
                Parameter: z
                Body:
                If n == 0 Then
                Return 1;
                ElseIf n == 1 Then
                x = 3;
                Else
                Return n * fact (n - 1);
                EndIf.
                EndBody. """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))]),(BinaryOp("==",Id("n"),IntLiteral(1)),[],[Assign(Id("x"),IntLiteral(3))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))
    def test_317(self):
        input = """ Function: foo
                Parameter: z
                Body:
                If n == 0 Then
                Return 1;
                EndIf.
                If n == 1 Then
                x = 3;
                Else
                Return n * fact (n - 1);
                EndIf.
                EndBody. """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[])),If([(BinaryOp("==",Id("n"),IntLiteral(1)),[],[Assign(Id("x"),IntLiteral(3))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))
    def test_318(self):
        input = """ Function: foo
                Parameter: z
                Body:
                If n == 0 Then
                Return 1;
                EndIf.
                If n == 1 Then
                x = 3;
                ElseIf n==2 Then
                Return n * fact (n - 1);
                EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[])),If([(BinaryOp("==",Id("n"),IntLiteral(1)),[],[Assign(Id("x"),IntLiteral(3))]),(BinaryOp("==",Id("n"),IntLiteral(2)),[],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))
    def test_319(self):
        input = """ Function: foo
                Parameter: z
                Body:
                While (x < 5) && (x == 3) Do 
                x = x+1;
                EndWhile.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([],[While(BinaryOp("&&",BinaryOp("<",Id("x"),IntLiteral(5)),BinaryOp("==",Id("x"),IntLiteral(3))),([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))
    def test_320(self):
        input = """ Function: foo
                Parameter: z
                Body:
                While x < 5 Do 
                x = x-1;
                If (x == 1) Then
                Break;
                EndIf.
                EndWhile.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([],[While(BinaryOp("<",Id("x"),IntLiteral(5)),([],[Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1))),If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Break()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))
    def test_321(self):
        input = """ Function: foo
                Parameter: x
                Body:
                While x < 5 Do 
                If (x == 1) Then
                Break;
                EndIf.
                EndWhile.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[While(BinaryOp("<",Id("x"),IntLiteral(5)),([],[If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Break()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))
    def test_322(self):
        input = """ Function: foo
                Parameter: x
                Body:
                While x < 5 Do 
                While n > 1 Do
                n = n+1;
                x = x-1;
                EndWhile.
                If (x == 1) Then
                Break;
                EndIf.
                EndWhile.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[While(BinaryOp("<",Id("x"),IntLiteral(5)),([],[While(BinaryOp(">",Id("n"),IntLiteral(1)),([],[Assign(Id("n"),BinaryOp("+",Id("n"),IntLiteral(1))),Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1)))])),If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Break()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))
    def test_323(self):
        input = """  Function: foo
                Parameter: x
                Body:
                Do
                n = n+1;
                x = x-1;
                While x < 1
                EndDo.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[Dowhile(([],[Assign(Id("n"),BinaryOp("+",Id("n"),IntLiteral(1))),Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1)))]),BinaryOp("<",Id("x"),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))
    def test_324(self):
        input = """ Function: foo
                Parameter: x
                Body:
                Do
                n = n+1;
                x = x-1;
                If (x == 1) Then
                Break;
                EndIf.
                While x < 1
                EndDo.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[Dowhile(([],[Assign(Id("n"),BinaryOp("+",Id("n"),IntLiteral(1))),Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1))),If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Break()])],([],[]))]),BinaryOp("<",Id("x"),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))
    def test_325(self):
        input = """ Function: foo
                Parameter: x
                Body:
                Do
                n = n+1;
                Do
                x = x-1;
                While x > 0
                EndDo.
                While x < 1
                EndDo.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[Dowhile(([],[Assign(Id("n"),BinaryOp("+",Id("n"),IntLiteral(1))),Dowhile(([],[Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1)))]),BinaryOp(">",Id("x"),IntLiteral(0)))]),BinaryOp("<",Id("x"),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))
    def test_326(self):
        input = """Function: foo
                Parameter: x
                Body:
                Do
                n = n+1;
                Do
                x = x-1;
                If (x == 1) Then
                Break;
                EndIf.
                While x > 0
                EndDo.
                While x < 1
                EndDo.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[Dowhile(([],[Assign(Id("n"),BinaryOp("+",Id("n"),IntLiteral(1))),Dowhile(([],[Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1))),If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Break()])],([],[]))]),BinaryOp(">",Id("x"),IntLiteral(0)))]),BinaryOp("<",Id("x"),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))
    def test_327(self):
        input = """Function: foo
                Parameter: x
                Body:
                For (i = 0, i < 10, 2) Do
                writeln(i);
                EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id("writeln"),[Id("i")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))
    def test_328(self):
        input = """Function: foo
                Parameter: x
                Body:
                For (a = 0, a < 5, 1) Do
                print(a);
                b = b * a;
                EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[For(Id("a"),IntLiteral(0),BinaryOp("<",Id("a"),IntLiteral(5)),IntLiteral(1),([],[CallStmt(Id("print"),[Id("a")]),Assign(Id("b"),BinaryOp("*",Id("b"),Id("a")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))
    def test_329(self):
        input = """ Function: foo
                Parameter: x
                Body:
                For (i = 0, i < 10, 2) Do
                For (j = 0, j < i, 1) Do
                s = s + i*j ; 
                EndFor.
                EndFor.
                EndBody. """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[Assign(Id("s"),BinaryOp("+",Id("s"),BinaryOp("*",Id("i"),Id("j"))))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))
    def test_330(self):
        input = """ Function: foo
                Parameter: x
                Body:
                For (a = 8, a < 18, 2) Do
                For (j = 8, j < i,  1) Do
                EndFor.
                EndFor.
                EndBody. """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[For(Id("a"),IntLiteral(8),BinaryOp("<",Id("a"),IntLiteral(18)),IntLiteral(2),([],[For(Id("j"),IntLiteral(8),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))
    def test_331(self):
        input = """ Function: foo
                Parameter: x
                Body:
                For (i = 0, i < 10,  2) Do
                Break;
                EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))
    def test_332(self):
        input = """Function: foo
                Parameter: x
                Body:
                For (i = 0, i < 10,  2) Do
                Continue;
                EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))
    def test_333(self):
        input = """ Function: foo
                Parameter: x
                Body:
                For (i = 0, i < 10, 2) Do
                Return i;
                EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[Return(Id("i"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))
    def test_334(self):
        input = """Function: foo
                Parameter: x
                Body:
                For (i = 0, i < 10,2) Do
                Return foo(5);
                EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[Return(CallExpr(Id("foo"),[IntLiteral(5)]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))
    def test_335(self):
        input = """Function: foo
                Parameter: x
                Body:
                For (i = 0, i < 10, 2) Do
                If (x == 1) Then
                Return i;
                EndIf.
                EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Return(Id("i"))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))
    def test_336(self):
        input = """Function: foo
                Parameter: x
                Body:
                foo();
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[CallStmt(Id("foo"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))
    def test_337(self):
        input = """Function: foo
                Body:
                foo(5, 7);
                Return foo(2);
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[CallStmt(Id("foo"),[IntLiteral(5),IntLiteral(7)]),Return(CallExpr(Id("foo"),[IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))
    def test_338(self):
        input = """Function: foo
                Parameter: x
                Body:
                If (x == 1) Then
                Return foo(i);
                EndIf.
                read();
                Return foo(5);
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Return(CallExpr(Id("foo"),[Id("i")]))])],([],[])),CallStmt(Id("read"),[]),Return(CallExpr(Id("foo"),[IntLiteral(5)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))
    def test_339(self):
        input = """Function: foo
                Parameter: x
                Body:
                For (i = 0, i < 10,2) Do
                If (x == 1) Then
                foo(5);
                EndIf.
                EndFor.
                foo(15,2,a);
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[CallStmt(Id("foo"),[IntLiteral(5)])])],([],[]))])),CallStmt(Id("foo"),[IntLiteral(15),IntLiteral(2),Id("a")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))
    def test_340(self):
        input = """Function: foo
                Parameter: x
                Body:
                read();
                printLn();
                Return foo(15,2,a);
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[CallStmt(Id("read"),[]),CallStmt(Id("printLn"),[]),Return(CallExpr(Id("foo"),[IntLiteral(15),IntLiteral(2),Id("a")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))
    def test_341(self):
        input = """Function: foo
                Parameter: z
                Body:
                While x < 5 Do 
                x = x-1;
                If (x == 1) Then
                Break;
                ElseIf x == 2 Then 
                x = x +1;
                EndIf.
                EndWhile.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([],[While(BinaryOp("<",Id("x"),IntLiteral(5)),([],[Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1))),If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Break()]),(BinaryOp("==",Id("x"),IntLiteral(2)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))
    def test_342(self):
        input = """ Var: x,y;
        Function: foo
                Parameter: z
                Body:
                If (x == 1) Then
                Break;
                Else 
                While x < 5 Do
                x = x-1;
                EndWhile.
                EndIf.
                EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([],[If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Break()])],([],[While(BinaryOp("<",Id("x"),IntLiteral(5)),([],[Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))
    def test_343(self):
        input = """Var: x,y;
                Function: foo
                Parameter: x
                Body:
                If (x == 1) Then
                Break;
                Else 
                While x < 5 Do
                x = x-1;
                EndWhile.
                EndIf.
                EndBody.
                Function: main
                Body:
                foo(5);
                EndBody.
                """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Break()])],([],[While(BinaryOp("<",Id("x"),IntLiteral(5)),([],[Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1)))]))]))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("foo"),[IntLiteral(5)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))
    def test_344(self):
        input = """ Var: a,b[5];
        Function: foo
                Parameter: z
                Body:
                If (x == 1) Then
                Break;
                Else 
                EndIf.
                EndBody.
                Function: main
                Body:
                foo(a);
                EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[5],None),FuncDecl(Id("foo"),[VarDecl(Id("z"),[],None)],([],[If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Break()])],([],[]))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("foo"),[Id("a")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))
    
    def test_345(self):
        input = """Function: main
        Body:
        x = 10;
        fact(x);
        ab = 1+ 2 - -3;
        EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")]),Assign(Id("ab"),BinaryOp("-",BinaryOp("+",IntLiteral(1),IntLiteral(2)),UnaryOp("-",IntLiteral(3))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_346(self):
        input = """ Var: x ,y = 10;
        Function: foo
                Parameter: x
                Body:
                While x < 5 Do
                **x = x-1;**
                EndWhile.
                EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(10)),FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[While(BinaryOp("<",Id("x"),IntLiteral(5)),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_347(self):
        input = """**this is a testcase**
        Function: foo
                Parameter: x, y ,arr
                Body:
                For (j = 0, j < i,  1) Do
                s = s + i*j ; 
                If s > 100 Then
                Return s;
                EndIf.
                EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("arr"),[],None)],([],[For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[Assign(Id("s"),BinaryOp("+",Id("s"),BinaryOp("*",Id("i"),Id("j")))),If([(BinaryOp(">",Id("s"),IntLiteral(100)),[],[Return(Id("s"))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))
    def test_348(self):
        input = """ Var: x ,y = 10;
        Function: foo
                Parameter: x
                Body:
                While x < 5 Do
                **x = x-1;**
                EndWhile.
                EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(10)),FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[While(BinaryOp("<",Id("x"),IntLiteral(5)),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))
    def test_349(self):
        input = """ Var: x ,y = 10;
                Function: foo
                Parameter: x
                Body:
                read();
                For (j = 0, j < i,  1) Do
                s = s + i*j ; 
                **If s > 100 Then
                Return s;
                EndIf.**
                EndFor.
                EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(10)),FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[CallStmt(Id("read"),[]),For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[Assign(Id("s"),BinaryOp("+",Id("s"),BinaryOp("*",Id("i"),Id("j"))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))
    def test_350(self):
        input = """Var: x ,y = 10;
                Function: foo
                Parameter: x
                Body:
                read();
                Do
                s = s + i*j ; 
                **sfdsfsdf**
                While x < 5
                EndDo.
                print(x);
                EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(10)),FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[CallStmt(Id("read"),[]),Dowhile(([],[Assign(Id("s"),BinaryOp("+",Id("s"),BinaryOp("*",Id("i"),Id("j"))))]),BinaryOp("<",Id("x"),IntLiteral(5))),CallStmt(Id("print"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))
    def test_351(self):
        input = """Var: x ,y = 10;
                Function: foo
                Parameter: x
                Body:
                read();
                Do
                s = s + i*j ; 
                **sfdsfsdf**
                While x < 5
                EndDo.
                print(x);
                EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(10)),FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[CallStmt(Id("read"),[]),Dowhile(([],[Assign(Id("s"),BinaryOp("+",Id("s"),BinaryOp("*",Id("i"),Id("j"))))]),BinaryOp("<",Id("x"),IntLiteral(5))),CallStmt(Id("print"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))
    def test_352(self):
        input = """Var: x ,y = 10;
                Function: foo
                Parameter: x
                Body:
                read();
                Do
                x = x+1;
                While x < 51
                EndDo.
                print(x);
                EndBody.
                Function: main
                Body:
                foo(5);
                EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(10)),FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[CallStmt(Id("read"),[]),Dowhile(([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),BinaryOp("<",Id("x"),IntLiteral(51))),CallStmt(Id("print"),[Id("x")])])),FuncDecl(Id("main"),[],([],[CallStmt(Id("foo"),[IntLiteral(5)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))
    def test_353(self):
        input = """Function: sumoffive
                Parameter: a[5]
                Body:
                Var: s = 0;
                For (i=0, i < n, 1) Do
                If (a[i] % 5 == 0) Then
                s = s + a[i];
                EndIf.
                EndFor.
                print(s);
                EndBody."""
        expect = Program([FuncDecl(Id("sumoffive"),[VarDecl(Id("a"),[5],None)],([VarDecl(Id("s"),[],IntLiteral(0))],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("n")),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",ArrayCell(Id("a"),[Id("i")]),IntLiteral(5)),IntLiteral(0)),[],[Assign(Id("s"),BinaryOp("+",Id("s"),ArrayCell(Id("a"),[Id("i")])))])],([],[]))])),CallStmt(Id("print"),[Id("s")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))
    def test_354(self):
        input = """Function: sumoffive
                Parameter: a[5]
                Body:
                Var: s = 0;
                For (i=0, i < n, 1) Do
                If (a[i] % 5 == 0) Then
                s = s + a[i];
                EndIf.
                EndFor.
                print(s);
                EndBody."""
        expect = Program([FuncDecl(Id("sumoffive"),[VarDecl(Id("a"),[5],None)],([VarDecl(Id("s"),[],IntLiteral(0))],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("n")),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",ArrayCell(Id("a"),[Id("i")]),IntLiteral(5)),IntLiteral(0)),[],[Assign(Id("s"),BinaryOp("+",Id("s"),ArrayCell(Id("a"),[Id("i")])))])],([],[]))])),CallStmt(Id("print"),[Id("s")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))
    def test_355(self):
        input = """Function: dem
                Parameter: x
                Body:
                Var: s = 0;
                For (i=0, i < x, 1) Do
                s = s + a[i];
                EndFor.
                print(s);
                EndBody."""
        expect = Program([FuncDecl(Id("dem"),[VarDecl(Id("x"),[],None)],([VarDecl(Id("s"),[],IntLiteral(0))],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("x")),IntLiteral(1),([],[Assign(Id("s"),BinaryOp("+",Id("s"),ArrayCell(Id("a"),[Id("i")])))])),CallStmt(Id("print"),[Id("s")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))
    def test_356(self):
        input = """Function: replay
                Parameter: a[5], x, y
                Body:
                For (i=0, i < 5, 1) Do
                If (a[i] == x) Then
                a[i] = y;
                EndIf.
                EndFor.
                print(s);
                EndBody."""
        expect = Program([FuncDecl(Id("replay"),[VarDecl(Id("a"),[5],None),VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(1),([],[If([(BinaryOp("==",ArrayCell(Id("a"),[Id("i")]),Id("x")),[],[Assign(ArrayCell(Id("a"),[Id("i")]),Id("y"))])],([],[]))])),CallStmt(Id("print"),[Id("s")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))
    def test_357(self):
        input = """Function: check
                Parameter: a[10]
                Body:
                For (i=0, i < 10, 1) Do
                If (a[i] + a[(i+1)] > 10) Then
                a[i] = 10;
                a[i+1] = 10;
                i = i+1;
                EndIf.
                EndFor.
                print(s);
                EndBody."""
        expect = Program([FuncDecl(Id("check"),[VarDecl(Id("a"),[10],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),([],[If([(BinaryOp(">",BinaryOp("+",ArrayCell(Id("a"),[Id("i")]),ArrayCell(Id("a"),[BinaryOp("+",Id("i"),IntLiteral(1))])),IntLiteral(10)),[],[Assign(ArrayCell(Id("a"),[Id("i")]),IntLiteral(10)),Assign(ArrayCell(Id("a"),[BinaryOp("+",Id("i"),IntLiteral(1))]),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],([],[]))])),CallStmt(Id("print"),[Id("s")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))
    def test_358(self):
        input = """Function: checksys
                Parameter: a[20]
                Body:
                For (i=0, i < 20,1) Do
                If (a[i] != a[(19-i)]) Then
                Return False;
                EndIf.
                EndFor.
                Return True;
                EndBody."""
        expect = Program([FuncDecl(Id("checksys"),[VarDecl(Id("a"),[20],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(20)),IntLiteral(1),([],[If([(BinaryOp("!=",ArrayCell(Id("a"),[Id("i")]),ArrayCell(Id("a"),[BinaryOp("-",IntLiteral(19),Id("i"))])),[],[Return(BooleanLiteral(False))])],([],[]))])),Return(BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))
    def test_359(self):
        input = """Function: checkincrease
                Parameter: a[20]
                Body:
                ** check wheather an array is increase **
                For (i=1, i < 20, 1) Do
                If (a[i] <= a[(i-1)]) Then
                Return False;
                EndIf.
                EndFor.
                Return True;
                EndBody."""
        expect = Program([FuncDecl(Id("checkincrease"),[VarDecl(Id("a"),[20],None)],([],[For(Id("i"),IntLiteral(1),BinaryOp("<",Id("i"),IntLiteral(20)),IntLiteral(1),([],[If([(BinaryOp("<=",ArrayCell(Id("a"),[Id("i")]),ArrayCell(Id("a"),[BinaryOp("-",Id("i"),IntLiteral(1))])),[],[Return(BooleanLiteral(False))])],([],[]))])),Return(BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))
    def test_360(self):
        input = """Function: checkstring
                Parameter: xyz[5], k
                Body:
                Var:dfdfd = 0;
                Do
                If (a[i] + k != a[i+1]) Then
                Return True;
                EndIf.
                i = i+5;
                asd = 45;
                While i < 26
                EndDo.
                Return False;
                EndBody."""
        expect = Program([FuncDecl(Id("checkstring"),[VarDecl(Id("xyz"),[5],None),VarDecl(Id("k"),[],None)],([VarDecl(Id("dfdfd"),[],IntLiteral(0))],[Dowhile(([],[If([(BinaryOp("!=",BinaryOp("+",ArrayCell(Id("a"),[Id("i")]),Id("k")),ArrayCell(Id("a"),[BinaryOp("+",Id("i"),IntLiteral(1))])),[],[Return(BooleanLiteral(True))])],([],[])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(5))),Assign(Id("asd"),IntLiteral(45))]),BinaryOp("<",Id("i"),IntLiteral(26))),Return(BooleanLiteral(False))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))
    def test_361(self):
        input = """Function: inserttoarray
                Parameter: a[21], k, n
                Body:
                Var:i = 0;
                For (i=20, i > k, 1) Do
                a[i]  = a[(i-1)];
                EndFor.
                a[k] = n;
                EndBody."""
        expect = Program([FuncDecl(Id("inserttoarray"),[VarDecl(Id("a"),[21],None),VarDecl(Id("k"),[],None),VarDecl(Id("n"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[For(Id("i"),IntLiteral(20),BinaryOp(">",Id("i"),Id("k")),IntLiteral(1),([],[Assign(ArrayCell(Id("a"),[Id("i")]),ArrayCell(Id("a"),[BinaryOp("-",Id("i"),IntLiteral(1))]))])),Assign(ArrayCell(Id("a"),[Id("k")]),Id("n"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))
    def test_362(self):
        input = """Function: giaithua
                Parameter: n
                Body:
                If n > 1 Then
                Return n * giaithua(n-1);
                EndIf.
                Return 1;
                EndBody. """
        expect = Program([FuncDecl(Id("giaithua"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp(">",Id("n"),IntLiteral(1)),[],[Return(BinaryOp("*",Id("n"),CallExpr(Id("giaithua"),[BinaryOp("-",Id("n"),IntLiteral(1))])))])],([],[])),Return(IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))
    def test_363(self):
        input = """Function: fibo
                Parameter: n
                Body:
                If n >= 1 Then
                Return fibo (n-1) + fibo(n-2);
                EndIf.
                Return 1;
                EndBody."""
        expect = Program([FuncDecl(Id("fibo"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp(">=",Id("n"),IntLiteral(1)),[],[Return(BinaryOp("+",CallExpr(Id("fibo"),[BinaryOp("-",Id("n"),IntLiteral(1))]),CallExpr(Id("fibo"),[BinaryOp("-",Id("n"),IntLiteral(2))])))])],([],[])),Return(IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))
    def test_364(self):
        input = """Function: checkprimity
                Parameter: n
                Body:
                For (i=2, i < n \\ 2, 1) Do
                If (n % i == 0) Then
                Return False;
                EndIf.
                EndFor.
                Return True;
                EndBody."""
        expect = Program([FuncDecl(Id("checkprimity"),[VarDecl(Id("n"),[],None)],([],[For(Id("i"),IntLiteral(2),BinaryOp("<",Id("i"),BinaryOp("\\",Id("n"),IntLiteral(2))),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),[],[Return(BooleanLiteral(False))])],([],[]))])),Return(BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))
    def test_365(self):
        input = """Function: revertnum
                Parameter: n
                Body:
                Var: res = 0;
                While n > 0 Do
                res = res * 10 + n % 10;
                n = n \\ 10;
                EndWhile.
                Return res;
                EndBody."""
        expect = Program([FuncDecl(Id("revertnum"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("res"),[],IntLiteral(0))],[While(BinaryOp(">",Id("n"),IntLiteral(0)),([],[Assign(Id("res"),BinaryOp("+",BinaryOp("*",Id("res"),IntLiteral(10)),BinaryOp("%",Id("n"),IntLiteral(10)))),Assign(Id("n"),BinaryOp("\\",Id("n"),IntLiteral(10)))])),Return(Id("res"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))
    def test_366(self):
        input = """Function: ucln
                Parameter: a ,b
                Body:
                If a > b Then
                Return ucln (a-b,b);
                ElseIf a < b Then
                Return ucln(a,b-a);
                Else 
                Return a;
                EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id("ucln"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",Id("a"),Id("b")),[],[Return(CallExpr(Id("ucln"),[BinaryOp("-",Id("a"),Id("b")),Id("b")]))]),(BinaryOp("<",Id("a"),Id("b")),[],[Return(CallExpr(Id("ucln"),[Id("a"),BinaryOp("-",Id("b"),Id("a"))]))])],([],[Return(Id("a"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))
    def test_367(self):
        input = """Function: main
                Parameter: r,dt,cv
                Body:
                Var: pi = 3.14;
                print("print nha");
                print("----------------------------");
                print ("nha ban kinh R=");
                read(r);
                dt = pi*r*r;
                cv = 2*pi*r;
                print("Dien tich nha:",dt);
                print("Chu vi nha:",cv);
                EndBody.                                
                """
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("r"),[],None),VarDecl(Id("dt"),[],None),VarDecl(Id("cv"),[],None)],([VarDecl(Id("pi"),[],FloatLiteral(3.14))],[CallStmt(Id("print"),[StringLiteral("print nha")]),CallStmt(Id("print"),[StringLiteral("----------------------------")]),CallStmt(Id("print"),[StringLiteral("nha ban kinh R=")]),CallStmt(Id("read"),[Id("r")]),Assign(Id("dt"),BinaryOp("*",BinaryOp("*",Id("pi"),Id("r")),Id("r"))),Assign(Id("cv"),BinaryOp("*",BinaryOp("*",IntLiteral(2),Id("pi")),Id("r"))),CallStmt(Id("print"),[StringLiteral("Dien tich nha:"),Id("dt")]),CallStmt(Id("print"),[StringLiteral("Chu vi nha:"),Id("cv")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))
    def test_368(self):
        input = """Function: ucln
                Parameter:  c, a ,b[5]
                Body:
                EndBody. """
        expect = Program([FuncDecl(Id("ucln"),[VarDecl(Id("c"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[5],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))
    def test_369(self):
        input = """Function: ucln
                Parameter: a ,b
                Body:
                If asd Then b = c;
                EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id("ucln"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[If([(Id("asd"),[],[Assign(Id("b"),Id("c"))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))
    def test_370(self):
        input = """ Var: a[5][2] = {{2,3},{3,    3}    , {4}, 5   } ;"""
        expect = Program([VarDecl(Id("a"),[5,2],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(3),IntLiteral(3)]),ArrayLiteral([IntLiteral(4)]),IntLiteral(5)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))
    def test_371(self):
        input="""** test array**
        Var: x = 5, y[2] = {2, {3}};"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(5)),VarDecl(Id("y"),[2],ArrayLiteral([IntLiteral(2),ArrayLiteral([IntLiteral(3)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))
    def test_372(self):
        input= """
               Var: x = 5, y[2] = {2, {3}};
               """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(5)),VarDecl(Id("y"),[2],ArrayLiteral([IntLiteral(2),ArrayLiteral([IntLiteral(3)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))
    def test_373(self):
        input= """Function: dem
                Parameter: a,b, c
                Body:
                If a == b Then b = c;
                EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id("dem"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],([],[If([(BinaryOp("==",Id("a"),Id("b")),[],[Assign(Id("b"),Id("c"))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))
    def test_374(self):
        input= """Function: ucln
                Parameter: a[5] ,b[7]
                Body:
                If cl[156321546] == b Then b = c;
                EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id("ucln"),[VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[7],None)],([],[If([(BinaryOp("==",ArrayCell(Id("cl"),[IntLiteral(156321546)]),Id("b")),[],[Assign(Id("b"),Id("c"))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))
    def test_375(self):
        input= """Function: du
                Parameter: a,b, c, d
                Body:
                If a == b Then b = c+1;
                EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id("du"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],None)],([],[If([(BinaryOp("==",Id("a"),Id("b")),[],[Assign(Id("b"),BinaryOp("+",Id("c"),IntLiteral(1)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))
    def test_376(self):
        input= """Function: dem
                Parameter: a,b,z
                Body:
                If a == b Then b = c;
                EndIf.
                abs = sd + sdf - 9;
                EndBody."""
        expect = Program([FuncDecl(Id("dem"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("z"),[],None)],([],[If([(BinaryOp("==",Id("a"),Id("b")),[],[Assign(Id("b"),Id("c"))])],([],[])),Assign(Id("abs"),BinaryOp("-",BinaryOp("+",Id("sd"),Id("sdf")),IntLiteral(9)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))
    def test_377(self):
        input= """Function: dem
                Parameter: dfsd,b, c
                Body:
                print();
                cal("s");
                EndBody."""
        expect = Program([FuncDecl(Id("dem"),[VarDecl(Id("dfsd"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],([],[CallStmt(Id("print"),[]),CallStmt(Id("cal"),[StringLiteral("s")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))
    def test_378(self):
        input= """Function: dem
                Parameter: a,b, c
                Body:
                If sdf == b Then
                Else  b = c;
                EndIf.
                If sdf == a Then
                Else  a = c;
                EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id("dem"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],([],[If([(BinaryOp("==",Id("sdf"),Id("b")),[],[])],([],[Assign(Id("b"),Id("c"))])),If([(BinaryOp("==",Id("sdf"),Id("a")),[],[])],([],[Assign(Id("a"),Id("c"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))
    def test_379(self):
        input= """Function: dem
                Parameter: a,b, c
                Body:
                For (a = 2, a < b, 1) Do
                EndFor.
                If sdf == a Then
                Else  a = c;
                EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id("dem"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],([],[For(Id("a"),IntLiteral(2),BinaryOp("<",Id("a"),Id("b")),IntLiteral(1),([],[])),If([(BinaryOp("==",Id("sdf"),Id("a")),[],[])],([],[Assign(Id("a"),Id("c"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))
    def test_380(self):
        input= """Function: dem
                Parameter: a,b, c
                Body:
                For (i = 2, i < n \\ 2, 1) Do
                If sdf == a Then
                Else  a = c;
                EndIf.
                EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("dem"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],([],[For(Id("i"),IntLiteral(2),BinaryOp("<",Id("i"),BinaryOp("\\",Id("n"),IntLiteral(2))),IntLiteral(1),([],[If([(BinaryOp("==",Id("sdf"),Id("a")),[],[])],([],[Assign(Id("a"),Id("c"))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))
    def test_381(self):
        input= """Function: dem
                Parameter: a,b, c
                Body:
                If ssff == a Then
                Else  a = ss;
                EndIf.
                For (i = 1651, i < 52, 1) Do
                EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("dem"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],([],[If([(BinaryOp("==",Id("ssff"),Id("a")),[],[])],([],[Assign(Id("a"),Id("ss"))])),For(Id("i"),IntLiteral(1651),BinaryOp("<",Id("i"),IntLiteral(52)),IntLiteral(1),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))
    def test_382(self):
        input= """Function: dem
                Body:
                For (i = 2, i < (5+4*nkj), 1) Do
                EndFor.
                adf = 45;
                EndBody."""
        expect = Program([FuncDecl(Id("dem"),[],([],[For(Id("i"),IntLiteral(2),BinaryOp("<",Id("i"),BinaryOp("+",IntLiteral(5),BinaryOp("*",IntLiteral(4),Id("nkj")))),IntLiteral(1),([],[])),Assign(Id("adf"),IntLiteral(45))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))
    def test_383(self):
        input= """Var: a = 9, xx_z[2] = {23, 5};"""
        expect = Program([VarDecl(Id("a"),[],IntLiteral(9)),VarDecl(Id("xx_z"),[2],ArrayLiteral([IntLiteral(23),IntLiteral(5)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))
    def test_384(self):
        input= """
            **foo(3);**
            """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))
    def test_385(self):
        input= """
            Var: array[15];
            """
        expect = Program([VarDecl(Id("array"),[15],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))
    def test_386(self):
        input= """Function: dem
                Parameter: a[5],b, c
                Body:
                asd = 5;
                For (sdf = 77, i < (n+2), 1) Do
                EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("dem"),[VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],([],[Assign(Id("asd"),IntLiteral(5)),For(Id("sdf"),IntLiteral(77),BinaryOp("<",Id("i"),BinaryOp("+",Id("n"),IntLiteral(2))),IntLiteral(1),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))
    def test_387(self):
        input= """
            Function: prime
                Parameter: i, j
                Body:
                For (j = 2, j < i, 1) Do
                If ( i % j == 0) Then
                Break;
                EndIf.
                EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("prime"),[VarDecl(Id("i"),[],None),VarDecl(Id("j"),[],None)],([],[For(Id("j"),IntLiteral(2),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("i"),Id("j")),IntLiteral(0)),[],[Break()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))
    def test_388(self):
        input= """
         Var: a,b[5][8];
         Function: foo
        Parameter: a[123], b
        Body:
            If a[12] > b Then
                For (j = 2, j < i, 1) Do
                If ( i % j == 0) Then
                Break;
                EndIf.
                EndFor.
            EndIf.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[5,8],None),FuncDecl(Id("foo"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",ArrayCell(Id("a"),[IntLiteral(12)]),Id("b")),[],[For(Id("j"),IntLiteral(2),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("i"),Id("j")),IntLiteral(0)),[],[Break()])],([],[]))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))
    def test_389(self):
        input= """
            Function: prime
            Parameter: i, j
            Body:
            For (j = 2, j < i, 1) Do
            If ( i % j == 0) Then
            Break;
            EndIf.
            EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id("prime"),[VarDecl(Id("i"),[],None),VarDecl(Id("j"),[],None)],([],[For(Id("j"),IntLiteral(2),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("i"),Id("j")),IntLiteral(0)),[],[Break()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))
    def test_390(self):
        input= """
            Function: error
                Parameter: i, j
                Body:
                    For (j = 2, j < i, 1) Do
                        If ( i % j == 0) Then
                            If ( i % j == 0) Then
                                Break;
                            EndIf.
                        EndIf.
                    EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("error"),[VarDecl(Id("i"),[],None),VarDecl(Id("j"),[],None)],([],[For(Id("j"),IntLiteral(2),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("i"),Id("j")),IntLiteral(0)),[],[If([(BinaryOp("==",BinaryOp("%",Id("i"),Id("j")),IntLiteral(0)),[],[Break()])],([],[]))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))
    def test_391(self):
        input= """
        Var: a = True, d;
        Function: error
        Parameter: sd[445], v
        Body:
            If d > g Then
                Do 
                    r = r+1;
                While (r == dsf)  EndDo.
            EndIf.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("d"),[],None),FuncDecl(Id("error"),[VarDecl(Id("sd"),[445],None),VarDecl(Id("v"),[],None)],([],[If([(BinaryOp(">",Id("d"),Id("g")),[],[Dowhile(([],[Assign(Id("r"),BinaryOp("+",Id("r"),IntLiteral(1)))]),BinaryOp("==",Id("r"),Id("dsf")))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))
    def test_392(self):
        input= """
            Function: error
                Body:
                For (j = 2, j < i, 1) Do
                If  (i % j == 0) Then
                Break;
                EndIf.
                If  (i == 0) Then
                a = sd +d * sdf - 5;
                b = s +d * sdf - 5;
                EndIf.
                EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("error"),[],([],[For(Id("j"),IntLiteral(2),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("i"),Id("j")),IntLiteral(0)),[],[Break()])],([],[])),If([(BinaryOp("==",Id("i"),IntLiteral(0)),[],[Assign(Id("a"),BinaryOp("-",BinaryOp("+",Id("sd"),BinaryOp("*",Id("d"),Id("sdf"))),IntLiteral(5))),Assign(Id("b"),BinaryOp("-",BinaryOp("+",Id("s"),BinaryOp("*",Id("d"),Id("sdf"))),IntLiteral(5)))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))
    def test_393(self):
        input= """
            Function: error
                Body:
                For (j = 2, j < i, 1) Do
                If ( i % j == 0) Then
                Break;
                EndIf.
                EndFor.
                EndBody.
            Function: error
                Body:
                a = a+5;
                retur();
                EndBody."""
        expect = Program([FuncDecl(Id("error"),[],([],[For(Id("j"),IntLiteral(2),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("i"),Id("j")),IntLiteral(0)),[],[Break()])],([],[]))]))])),FuncDecl(Id("error"),[],([],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(5))),CallStmt(Id("retur"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))
    
    def test_394(self):
        input= """
            Function: ok
                Body:
                For (j = 2, j < i, 1) Do
                If ( i % j == 0) Then
                Break;
                EndIf.
                EndFor.
                EndBody."""
            
        expect = Program([FuncDecl(Id("ok"),[],([],[For(Id("j"),IntLiteral(2),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("i"),Id("j")),IntLiteral(0)),[],[Break()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_395(self):
        input= """
            Function: oke
                Body:
                For (j = 2, j < i, 1) Do
                read();
                EndFor.
                EndBody."""
            
        expect = Program([FuncDecl(Id("oke"),[],([],[For(Id("j"),IntLiteral(2),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[CallStmt(Id("read"),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))
    def test_396(self):
        input= """
            Function: oke
                Body:
                For (j = 2, j < i, 1) Do
                read();
                EndFor.
                For (j = 5, r < 8, 1) Do
                print("hihihaha");
                EndFor.
                If ( i % j == 0) Then
                Break;
                EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id("oke"),[],([],[For(Id("j"),IntLiteral(2),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[CallStmt(Id("read"),[])])),For(Id("j"),IntLiteral(5),BinaryOp("<",Id("r"),IntLiteral(8)),IntLiteral(1),([],[CallStmt(Id("print"),[StringLiteral("hihihaha")])])),If([(BinaryOp("==",BinaryOp("%",Id("i"),Id("j")),IntLiteral(0)),[],[Break()])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))
    
    def test_397(self):
        input= """
            Function: oke
                Parameter: a, b
                Body:
                For (j = 2, j < i, 1) Do
                read();
                EndFor.
                return();
                EndBody."""
        expect = Program([FuncDecl(Id("oke"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[For(Id("j"),IntLiteral(2),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[CallStmt(Id("read"),[])])),CallStmt(Id("return"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))
    
    def test_398(self):
        input= """
            Function: oke
                Body:
                return();
                For (j = 2, j < i, 1) Do
                return();
                read();
                EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id("oke"),[],([],[CallStmt(Id("return"),[]),For(Id("j"),IntLiteral(2),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[CallStmt(Id("return"),[]),CallStmt(Id("read"),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_399(self):
        input= """
            Function: oke
                Parameter: sss[45],s
                Body:
                For (j = 2, j < i, 1) Do
                a = b;
                EndFor.
                read();
                EndBody."""
        expect = Program([FuncDecl(Id("oke"),[VarDecl(Id("sss"),[45],None),VarDecl(Id("s"),[],None)],([],[For(Id("j"),IntLiteral(2),BinaryOp("<",Id("j"),Id("i")),IntLiteral(1),([],[Assign(Id("a"),Id("b"))])),CallStmt(Id("read"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_400(self):
        input= """
            Function: oke
                Parameter:m, n ,o, p ,s ,s, sdf[5]
                Body:
                Var: a,bsss;
                EndBody."""
        expect = Program([FuncDecl(Id("oke"),[VarDecl(Id("m"),[],None),VarDecl(Id("n"),[],None),VarDecl(Id("o"),[],None),VarDecl(Id("p"),[],None),VarDecl(Id("s"),[],None),VarDecl(Id("s"),[],None),VarDecl(Id("sdf"),[5],None)],([VarDecl(Id("a"),[],None),VarDecl(Id("bsss"),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))