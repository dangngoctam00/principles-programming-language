import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_300(self):        
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))
    
    def test_301(self):        
        input = """Var:x = 2;"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(2))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))
    
    def test_302(self):        
        input = """Var:x = 2,x[2] = {3};"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(2)),VarDecl(Id("x"),[2],ArrayLiteral([IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_303(self):        
        input = """Var:x[2][2] = {3,2};"""
        expect = Program([VarDecl(Id("x"),[2,2],ArrayLiteral([IntLiteral(3),IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))
    
    def test_304(self):        
        input = """Var:x[2][2] = {3,2, {2}};"""
        expect = Program([VarDecl(Id("x"),[2,2],ArrayLiteral([IntLiteral(3),IntLiteral(2),ArrayLiteral([IntLiteral(2)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_305(self):        
        input = """Var:x[2][2] = {3,2, {2, {2}}};"""
        expect = Program([VarDecl(Id("x"),[2,2],ArrayLiteral([IntLiteral(3),IntLiteral(2),ArrayLiteral([IntLiteral(2),ArrayLiteral([IntLiteral(2)])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))
    def test_306(self):        
        input = """Var:x[2][2] = {3,2, {2, {2}}}, a = 2;"""
        expect = Program([VarDecl(Id("x"),[2,2],ArrayLiteral([IntLiteral(3),IntLiteral(2),ArrayLiteral([IntLiteral(2),ArrayLiteral([IntLiteral(2)])])])),VarDecl(Id("a"),[],IntLiteral(2))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))
    
    def test_307(self):        
        input = """Var:x[2][2];"""
        expect = Program([VarDecl(Id("x"),[2,2],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))
    
    def test_308(self):        
        input = """Var:x = 4;
                   Var:y = 5;             
        """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_309(self):        
        input = """Var:x, y;
                   Var:y = {True,2};             
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("y"),[],ArrayLiteral([BooleanLiteral(True),IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))
    
    def test_310(self):        
        input = """
            Function: foo
            Parameter: a
            Body:
                a = 2;
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([],[Assign(Id("a"),IntLiteral(2))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))
    
    def test_311(self):        
        input = """
            Function: foo
            Parameter: a
            Body:
                a = a -. 2;
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([],[Assign(Id("a"),BinaryOp("-.",Id("a"),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_312(self):        
        input = """
            Function: foo
            Parameter: a
            Body:
                Var: x[2] = 3;
                a = a -. 2;
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([VarDecl(Id("x"),[2],IntLiteral(3))],[Assign(Id("a"),BinaryOp("-.",Id("a"),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))
   
    def test_313(self):  
        input = """
            Function: foo
            Parameter: a
            Body:                
                If a Then c = 10;
                ElseIf c == 6 Then d = 12;
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([],[If([(Id("a"),[],[Assign(Id("c"),IntLiteral(10))]),(BinaryOp("==",Id("c"),IntLiteral(6)),[],[Assign(Id("d"),IntLiteral(12))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))


    def test_314(self):
        input = """
            Function: foo
            Body:
                Do a = b + 3; c[2][3] = 5; While x == y EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),IntLiteral(5))]),BinaryOp("==",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_315(self):
        input = """
            Function: foo
            Body:
                Do a = b + 3; c[2][3] = 5; While x == y EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),IntLiteral(5))]),BinaryOp("==",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_316(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3); c[2][3] = (((5))); While x == y EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),IntLiteral(5))]),BinaryOp("==",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))
    
    def test_317(self):
        input = """
            Function: foo
            Body:
                Var: x = 3;
                Var: y = {1,2,"\\n"};
                Var: x = True;
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([VarDecl(Id("x"),[],IntLiteral(3)),VarDecl(Id("y"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),StringLiteral("\\n")])),VarDecl(Id("x"),[],BooleanLiteral(True))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_318(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3);
                c[2][3] = (((5)));                
                While x == y EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),IntLiteral(5))]),BinaryOp("==",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_319(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3);
                c[2][3] = (((5)));
                While x == y EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),IntLiteral(5))]),BinaryOp("==",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_320(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3);
                                            xyz = x[3];
                c[2][3] = (((5)));
                While x == y EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(Id("xyz"),ArrayCell(Id("x"),[IntLiteral(3)])),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),IntLiteral(5))]),BinaryOp("==",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_321(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3);
                                            xyz = x[3];
                                c[func(3)+5*op[x[y[z[3]]]]] = 3;
                c[2][3] = (((5)));
                While x == y EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(Id("xyz"),ArrayCell(Id("x"),[IntLiteral(3)])),Assign(ArrayCell(Id("c"),[BinaryOp("+",CallExpr(Id("func"),[IntLiteral(3)]),BinaryOp("*",IntLiteral(5),ArrayCell(Id("op"),[ArrayCell(Id("x"),[ArrayCell(Id("y"),[ArrayCell(Id("z"),[IntLiteral(3)])])])])))]),IntLiteral(3)),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),IntLiteral(5))]),BinaryOp("==",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_322(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3);
                                            xyz = x[3];
                                c[func(3)+5*op[x[y[z[3]]]]] = 3;
                c[2][3] = (((5)));
                While x - y EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(Id("xyz"),ArrayCell(Id("x"),[IntLiteral(3)])),Assign(ArrayCell(Id("c"),[BinaryOp("+",CallExpr(Id("func"),[IntLiteral(3)]),BinaryOp("*",IntLiteral(5),ArrayCell(Id("op"),[ArrayCell(Id("x"),[ArrayCell(Id("y"),[ArrayCell(Id("z"),[IntLiteral(3)])])])])))]),IntLiteral(3)),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),IntLiteral(5))]),BinaryOp("-",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_323(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3);
                                            xyz = x[3];
                                c[func(3)+5*op[x[y[z[3]]]]] = 3;
                c[2][3] = (((5)));
                While x - y EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(Id("xyz"),ArrayCell(Id("x"),[IntLiteral(3)])),Assign(ArrayCell(Id("c"),[BinaryOp("+",CallExpr(Id("func"),[IntLiteral(3)]),BinaryOp("*",IntLiteral(5),ArrayCell(Id("op"),[ArrayCell(Id("x"),[ArrayCell(Id("y"),[ArrayCell(Id("z"),[IntLiteral(3)])])])])))]),IntLiteral(3)),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),IntLiteral(5))]),BinaryOp("-",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_324(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3);
                c[2][3] = (((5)));
                While x - y EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),IntLiteral(5))]),BinaryOp("-",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_325(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3);
                x(y)              ; ** hello **
                c[2][3] = (((5)));
                While x - y EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),CallStmt(Id("x"),[Id("y")]),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),IntLiteral(5))]),BinaryOp("-",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_326(self):
        input = """
            Function: foo
            Body:
                foo( );
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[CallStmt(Id("foo"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_327(self):
        input = """
            Function: foo
            Body:
                foo(x + 2, 4 \. y);
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[CallStmt(Id("foo"),[BinaryOp("+",Id("x"),IntLiteral(2)),BinaryOp("\.",IntLiteral(4),Id("y"))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_328(self):
        input = """
            Function: foo
            Body:
                foo(x + 2, 4 \. y);
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[CallStmt(Id("foo"),[BinaryOp("+",Id("x"),IntLiteral(2)),BinaryOp("\.",IntLiteral(4),Id("y"))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_329(self):
        input = """
            Function: foo
            Body:
                foo(func(a + 2, b \ 3) + 3 * 6, zz);
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[CallStmt(Id("foo"),[BinaryOp("+",CallExpr(Id("func"),[BinaryOp("+",Id("a"),IntLiteral(2)),BinaryOp("\\",Id("b"),IntLiteral(3))]),BinaryOp("*",IntLiteral(3),IntLiteral(6))),Id("zz")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_330(self):
        input = """
            Function: foo
            Body:
                foo(func(a + 2, b \ 3) + 3 * 6);
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[CallStmt(Id("foo"),[BinaryOp("+",CallExpr(Id("func"),[BinaryOp("+",Id("a"),IntLiteral(2)),BinaryOp("\\",Id("b"),IntLiteral(3))]),BinaryOp("*",IntLiteral(3),IntLiteral(6)))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_331(self):
        input = """
            Function: foo
            Body:
                x = foo(2 + 4, another_foo(2,3 \ 5));
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("x"),CallExpr(Id("foo"),[BinaryOp("+",IntLiteral(2),IntLiteral(4)),CallExpr(Id("another_foo"),[IntLiteral(2),BinaryOp("\\",IntLiteral(3),IntLiteral(5))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_332(self):
        input = """
            Function: foo
            Body:
                x = foo(2 + 4, another_foo(2,3 \ 5));
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("x"),CallExpr(Id("foo"),[BinaryOp("+",IntLiteral(2),IntLiteral(4)),CallExpr(Id("another_foo"),[IntLiteral(2),BinaryOp("\\",IntLiteral(3),IntLiteral(5))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_333(self):
        input = """
            Function: foo
            Body:
                While a == 3 Do x = x + 1; Break; EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[While(BinaryOp("==",Id("a"),IntLiteral(3)),([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_334(self):
        input = """
            Function: foo
            Body:
                While a == 3 Do x = x + 1; Break;
                Continue;
                EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[While(BinaryOp("==",Id("a"),IntLiteral(3)),([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),Break(),Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_335(self): #think
        input = """
            Function: foo
            Body:
                While a == 3 Do x = x + 1; EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[While(BinaryOp("==",Id("a"),IntLiteral(3)),([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_336(self): #think
        input = """
            Var: x = 3;
            **This is single line comment**
            Function: function
            Parameter: x, y
            Body:
            EndBody.            
        """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(3)),FuncDecl(Id("function"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_337(self):
        input = """
            Var: x = 3;
            **This is single line comment**
            Function: function
            Parameter: x, y
            Body:
            **This is a
            * multi-line
            * comment
            **
            EndBody.
            Function: testFunction
            Parameter: a[2], b, c
            Body:
                Var: b[3][2] = {{1,2,3}, {3,4,5}}, x = 12;
                For (a = 3, b && c || d && e,i \ 3)
                **////abc_xyz**
                Do x = x + 2; y = y + 3;
                EndFor.
            EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(3)),FuncDecl(Id("function"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([],[])),FuncDecl(Id("testFunction"),[VarDecl(Id("a"),[2],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],([VarDecl(Id("b"),[3,2],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(3),IntLiteral(4),IntLiteral(5)])])),VarDecl(Id("x"),[],IntLiteral(12))],[For(Id("a"),IntLiteral(3),BinaryOp("&&",BinaryOp("||",BinaryOp("&&",Id("b"),Id("c")),Id("d")),Id("e")),BinaryOp("\\",Id("i"),IntLiteral(3)),([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2))),Assign(Id("y"),BinaryOp("+",Id("y"),IntLiteral(3)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_338(self):
        input = """
            Var: x = 3;
            **This is single line comment**
            Function: function
            Parameter: x, y
            ** abc_xyz**
            Body:
            **This is a
            * multi-line
            * comment
            **
            EndBody.
            Function: testFunction
            Parameter: a[2], b, c
            Body:
                Var: b[3][2] = {{1,2,3}, {3,4,5}}, x = 12;
                For (a = 3, b && c || d && e, i \ 3)
                **////abc_xyz**
                Do x = x + 2; y = y + 3;
                EndFor.
            EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(3)),FuncDecl(Id("function"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([],[])),FuncDecl(Id("testFunction"),[VarDecl(Id("a"),[2],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],([VarDecl(Id("b"),[3,2],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(3),IntLiteral(4),IntLiteral(5)])])),VarDecl(Id("x"),[],IntLiteral(12))],[For(Id("a"),IntLiteral(3),BinaryOp("&&",BinaryOp("||",BinaryOp("&&",Id("b"),Id("c")),Id("d")),Id("e")),BinaryOp("\\",Id("i"),IntLiteral(3)),([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2))),Assign(Id("y"),BinaryOp("+",Id("y"),IntLiteral(3)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_339(self):
        input = """
            Var: x = 3;
            **This is single line comment**
            ****************Var: abc = 5;****
            Var: ff = 2;
        """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(3)),VarDecl(Id("abc"),[],IntLiteral(5)),VarDecl(Id("ff"),[],IntLiteral(2))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_340(self):
        input = """
            Var: x = 3;
            **This is single line comment**
            ****************************************************
        """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_341(self):
        input = """
            Var: x = 3;
            **This is single line comment**
            Function: fooaaaaa
            Parameter: a , b[2]
            Body:
                Var: r = 10., abc[25][16] = {{1,2,3}, {5,6,7}};
                x = (4. \. 3.) *. 3.14 *. r *. r *. r;
                a[3 + foo(2)] = a[b[2][3][4]] + 4;
            EndBody.
            ****************************************************
        """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(3)),FuncDecl(Id("fooaaaaa"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([VarDecl(Id("r"),[],FloatLiteral(10.0)),VarDecl(Id("abc"),[25,16],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(5),IntLiteral(6),IntLiteral(7)])]))],[Assign(Id("x"),BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("\.",FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id("r")),Id("r")),Id("r"))),Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(2)]))]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_342(self):
        input = """
            Var: x = 3;
            **This is single line comment**
            ****************************************************
            **
            Var !@#$%^&*()_+)
            **
            Var: x = 2,    b, c ,   d, e = 55;
        """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(3)),VarDecl(Id("x"),[],IntLiteral(2)),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],None),VarDecl(Id("e"),[],IntLiteral(55))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_343(self):
        input = """
            **This is single line comment**
            ****************************************************
            **
            Var !@#$%^&*()_+)
            **
            Var: x = 2, b, c , f[2][3] = 4,  d, e = 55;
        """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(2)),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("f"),[2,3],IntLiteral(4)),VarDecl(Id("d"),[],None),VarDecl(Id("e"),[],IntLiteral(55))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_344(self):
        input = """
    Function: main
        Body:
            While (n<10) && (m>0) && (check!= False) Do
                write(n);
                m = 1.2 +. n \\. i *. a[b[1][3]];
                If m*n!=0 Then
                    While (m>10000) && (m<=foo(z)) Do
                    m =n+m;
                    m=swap(m,a[m]);
                    recursive(a[m]-foo(3));
                    EndWhile.
                    n = random(m,n);
                Else m = k; n= p;
                EndIf.
                n = n-1;
            EndWhile.
        EndBody.
            """
        expect = Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("&&",BinaryOp("&&",BinaryOp("<",Id("n"),IntLiteral(10)),BinaryOp(">",Id("m"),IntLiteral(0))),BinaryOp("!=",Id("check"),BooleanLiteral(False))),([],[CallStmt(Id("write"),[Id("n")]),Assign(Id("m"),BinaryOp("+.",FloatLiteral(1.2),BinaryOp("*.",BinaryOp("\.",Id("n"),Id("i")),ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(1),IntLiteral(3)])])))),If([(BinaryOp("!=",BinaryOp("*",Id("m"),Id("n")),IntLiteral(0)),[],[While(BinaryOp("&&",BinaryOp(">",Id("m"),IntLiteral(10000)),BinaryOp("<=",Id("m"),CallExpr(Id("foo"),[Id("z")]))),([],[Assign(Id("m"),BinaryOp("+",Id("n"),Id("m"))),Assign(Id("m"),CallExpr(Id("swap"),[Id("m"),ArrayCell(Id("a"),[Id("m")])])),CallStmt(Id("recursive"),[BinaryOp("-",ArrayCell(Id("a"),[Id("m")]),CallExpr(Id("foo"),[IntLiteral(3)]))])])),Assign(Id("n"),CallExpr(Id("random"),[Id("m"),Id("n")]))])],([],[Assign(Id("m"),Id("k")),Assign(Id("n"),Id("p"))])),Assign(Id("n"),BinaryOp("-",Id("n"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_345(self):
        input = """
            Var: x,a=6;
            Function: add
            Parameter: a, b
            Body:
                Return a+b;
            EndBody.
            Function: func
            Parameter: a,b,v,c,d,aq,e,r,q
            Body:
                Return a<0 || (a < 3);
            EndBody.
            """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(6)),FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[Return(BinaryOp("+",Id("a"),Id("b")))])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("v"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],None),VarDecl(Id("aq"),[],None),VarDecl(Id("e"),[],None),VarDecl(Id("r"),[],None),VarDecl(Id("q"),[],None)],([],[Return(BinaryOp("<",Id("a"),BinaryOp("||",IntLiteral(0),BinaryOp("<",Id("a"),IntLiteral(3)))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_346(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3, "string"};
            Function: add
            Parameter: a, b
            Body:
               If(((((((x == 3))))))) Then
                    x = y + z;
                    func(3) ;
                x[func(3) + 3] = 5;
                EndIf.
                Return a+b;
            EndBody.
            """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(6)),VarDecl(Id("arr"),[3,4],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),StringLiteral("string")])),FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp("==",Id("x"),IntLiteral(3)),[],[Assign(Id("x"),BinaryOp("+",Id("y"),Id("z"))),CallStmt(Id("func"),[IntLiteral(3)]),Assign(ArrayCell(Id("x"),[BinaryOp("+",CallExpr(Id("func"),[IntLiteral(3)]),IntLiteral(3))]),IntLiteral(5))])],([],[])),Return(BinaryOp("+",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_347(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3};
            Function: add
            Parameter: a, b
            Body:
                Return a+b;
            EndBody.
            """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(6)),VarDecl(Id("arr"),[3,4],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[Return(BinaryOp("+",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_348(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3};
            Function: add
            Parameter: a, b
            Body:
                Var: x, y ,z ,t,f,a;
                While (a + b < 2.12) Do
                    i = i + 1;
                EndWhile.                
                Return a+b;
            EndBody.
            """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(6)),VarDecl(Id("arr"),[3,4],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),VarDecl(Id("t"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("a"),[],None)],[While(BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),FloatLiteral(2.12)),([],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])),Return(BinaryOp("+",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_349(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3};
            Function: add
            Parameter: a, b
            Body:
                x = 5;
                While (a == 12) Do
                    i = i + 1;
                EndWhile.
                Return a+b;
            EndBody.
            """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(6)),VarDecl(Id("arr"),[3,4],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[Assign(Id("x"),IntLiteral(5)),While(BinaryOp("==",Id("a"),IntLiteral(12)),([],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])),Return(BinaryOp("+",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_350(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3};
            Function: add
            Parameter: a, b
            Body:
                If(((((((x == 3))))))) Then
                    x = y + z;
                EndIf.
                While (a == 12) Do
                    i = i + 1;
                EndWhile.
                Return a+b;
            EndBody.
            """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(6)),VarDecl(Id("arr"),[3,4],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp("==",Id("x"),IntLiteral(3)),[],[Assign(Id("x"),BinaryOp("+",Id("y"),Id("z")))])],([],[])),While(BinaryOp("==",Id("a"),IntLiteral(12)),([],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])),Return(BinaryOp("+",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_351(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3};
            Function: add
            Parameter: a, b
            Body:
                While (a != 12) Do
                    Break;
                    Continue;
                    i = i + 1;
                EndWhile.
                Return a+b;
            EndBody.
            """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(6)),VarDecl(Id("arr"),[3,4],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[While(BinaryOp("!=",Id("a"),IntLiteral(12)),([],[Break(),Continue(),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])),Return(BinaryOp("+",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_352(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3, True};
            Function: add
            Parameter: f[2][3]
            Body:
                While (a != 12) Do
                    Break;
                    Continue;
                    Continue;
                    i = i + 1;
                EndWhile.
                Return a+b;
            EndBody.
            """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(6)),VarDecl(Id("arr"),[3,4],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),BooleanLiteral(True)])),FuncDecl(Id("add"),[VarDecl(Id("f"),[2,3],None)],([],[While(BinaryOp("!=",Id("a"),IntLiteral(12)),([],[Break(),Continue(),Continue(),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])),Return(BinaryOp("+",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))
    
    def test_353(self):
        input = """
            Function: add
            Body:
                While (a != 12) Do
                    x[a[a[3]]] = "hello";
                EndWhile.
            EndBody.
            """
        expect = Program([FuncDecl(Id("add"),[],([],[While(BinaryOp("!=",Id("a"),IntLiteral(12)),([],[Assign(ArrayCell(Id("x"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[IntLiteral(3)])])]),StringLiteral("hello"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_354(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3};
            Function: add
            Parameter: a, b
            Body:
                While (a != a[3]) Do
                    Break;
                    Continue;
                    i = i + 1;
                EndWhile.
                Return a+b;
            EndBody.
            """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(6)),VarDecl(Id("arr"),[3,4],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[While(BinaryOp("!=",Id("a"),ArrayCell(Id("a"),[IntLiteral(3)])),([],[Break(),Continue(),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])),Return(BinaryOp("+",Id("a"),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_355(self):
        input = """
            Function: add
            Body:
                While (a != 12) Do
                    x[a[a[3]]] = "hello";
                EndWhile.
            EndBody.
            """
        expect = Program([FuncDecl(Id("add"),[],([],[While(BinaryOp("!=",Id("a"),IntLiteral(12)),([],[Assign(ArrayCell(Id("x"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[IntLiteral(3)])])]),StringLiteral("hello"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))
    
    def test_356(self):
        input = """
            Function: add
            Body:
                While (a != 12) Do
                    x[a[a[3][2][1]]] = {1,2,3,4};
                EndWhile.
            EndBody.
            """
        expect = Program([FuncDecl(Id("add"),[],([],[While(BinaryOp("!=",Id("a"),IntLiteral(12)),([],[Assign(ArrayCell(Id("x"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[IntLiteral(3),IntLiteral(2),IntLiteral(1)])])]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))
    
    def test_357(self):
        input = """
            Function: add
            Body:
                Var: x[3] = 3;
                While (a != 12) Do
                    x[a[a[3]]] = {1,3,4};
                EndWhile.
            EndBody.
            Function: addhuman
            Body:
                Var: x[3] = 22;
                While (a != 12) Do
                    x[a[a[3]]] = {1,3,4};
                    If x == 3 Then
                    EndIf.
                EndWhile.
            EndBody.
            """
        expect = Program([FuncDecl(Id("add"),[],([VarDecl(Id("x"),[3],IntLiteral(3))],[While(BinaryOp("!=",Id("a"),IntLiteral(12)),([],[Assign(ArrayCell(Id("x"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[IntLiteral(3)])])]),ArrayLiteral([IntLiteral(1),IntLiteral(3),IntLiteral(4)]))]))])),FuncDecl(Id("addhuman"),[],([VarDecl(Id("x"),[3],IntLiteral(22))],[While(BinaryOp("!=",Id("a"),IntLiteral(12)),([],[Assign(ArrayCell(Id("x"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[IntLiteral(3)])])]),ArrayLiteral([IntLiteral(1),IntLiteral(3),IntLiteral(4)])),If([(BinaryOp("==",Id("x"),IntLiteral(3)),[],[])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))
    
    def test_358(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b,c,d,e
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return;
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],None),VarDecl(Id("e"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_359(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Body:
            While (a < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - d;
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[],([],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("a"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),Id("d")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))
    
    def test_360(self):
        input = """
        Var: x = "a\\n";
        Function: func
        Body:
            While (a < 5) && (j>6) || (k==7) Do
                i = i - b * a -. b \\ c -. d;
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("x"),[],StringLiteral("a\\n")),FuncDecl(Id("func"),[],([],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("a"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(Id("i"),BinaryOp("-.",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),Id("d")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_361(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Body:
            Var: string = "string\\b\\n\\r\\f";
            While (a < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
                a = (b + 3 - c * d =/= 5) || (b-d<.10); 
                c[2][3] = 5\\10.2\\.func(a,b,c)+a[2+func()+c[4]];
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[],([VarDecl(Id("string"),[],StringLiteral("string\\b\\n\\r\\f"))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("a"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d")))),Assign(Id("a"),BinaryOp("||",BinaryOp("=/=",BinaryOp("-",BinaryOp("+",Id("b"),IntLiteral(3)),BinaryOp("*",Id("c"),Id("d"))),IntLiteral(5)),BinaryOp("<.",BinaryOp("-",Id("b"),Id("d")),IntLiteral(10)))),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),BinaryOp("+",BinaryOp("\.",BinaryOp("\\",IntLiteral(5),FloatLiteral(10.2)),CallExpr(Id("func"),[Id("a"),Id("b"),Id("c")])),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))
    
    def test_362(self):
        input = """
        Var: a[3] = {True,2,3, "\\n"};
        Function: func
        Body:
            While (a < 5) && (j>6) || (k==7) Do
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3),StringLiteral("\\n")])),FuncDecl(Id("func"),[],([],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("a"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))
    
    def test_363(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: f[2][3][4][5]
        Body:
           string = "\\n\\f\\n";
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("f"),[2,3,4,5],None)],([],[Assign(Id("string"),StringLiteral("\\n\\f\\n"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))
    
    def test_364(self):
        input = """
        Var: a[3] = {True,False, 1.231341421};
        Function: func
        Parameter: a
        Body:
            
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),FloatLiteral(1.231341421)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_365(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, x[3]
        Body:
            While (a < 5) && (j>6) || (k==7) Do
            EndWhile.

            While (a < 5) && (j>6) || (k==7) Do
            EndWhile.

            If(((((((x == 3))))))) Then
                    x = y + z;
            EndIf.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("x"),[3],None)],([],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("a"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[])),While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("a"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[])),If([(BinaryOp("==",Id("x"),IntLiteral(3)),[],[Assign(Id("x"),BinaryOp("+",Id("y"),Id("z")))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_366(self):
        input = """
        Var: a[3] = {2};
        Function: func
        Parameter: a, x[3]
        Body:
            While (a < 5) && (j>=6) || (k==7) Do
            EndWhile.
            **
                    !@#$%^&*()_)
            **
            If(((((((x == 3))))))) Then
                    x = y + z;
                    func(3) ;
            x[func(3) + 3] = 5;
            EndIf.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(2)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("x"),[3],None)],([],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("a"),IntLiteral(5)),BinaryOp(">=",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[])),If([(BinaryOp("==",Id("x"),IntLiteral(3)),[],[Assign(Id("x"),BinaryOp("+",Id("y"),Id("z"))),CallStmt(Id("func"),[IntLiteral(3)]),Assign(ArrayCell(Id("x"),[BinaryOp("+",CallExpr(Id("func"),[IntLiteral(3)]),IntLiteral(3))]),IntLiteral(5))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_367(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, x[3]
        Body:
            While (True) && False || True >= False Do
            EndWhile.
            **
                    !@#$%^&*()_)
            **
            If(((((((x == 3))))))) Then
                    x = y + z;
                    While ((((((((((x != 3)))))))))) Do
                    hello = hello + 5;
                    EndWhile.
                    func(3) ;
            x[func(3) + 3] = 5;
            EndIf.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("x"),[3],None)],([],[While(BinaryOp(">=",BinaryOp("||",BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(True)),BooleanLiteral(False)),([],[])),If([(BinaryOp("==",Id("x"),IntLiteral(3)),[],[Assign(Id("x"),BinaryOp("+",Id("y"),Id("z"))),While(BinaryOp("!=",Id("x"),IntLiteral(3)),([],[Assign(Id("hello"),BinaryOp("+",Id("hello"),IntLiteral(5)))])),CallStmt(Id("func"),[IntLiteral(3)]),Assign(ArrayCell(Id("x"),[BinaryOp("+",CallExpr(Id("func"),[IntLiteral(3)]),IntLiteral(3))]),IntLiteral(5))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_368(self):
        input = """
            Function: foo
            Parameter: a
            Body:
                If c == 10 Then
                ElseIf a -   ** comment ** 3 Then
                ElseIf a -   ** comment ** 3 Then
                ElseIf a -   ** comment ** 3 Then
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([],[If([(BinaryOp("==",Id("c"),IntLiteral(10)),[],[]),(BinaryOp("-",Id("a"),IntLiteral(3)),[],[]),(BinaryOp("-",Id("a"),IntLiteral(3)),[],[]),(BinaryOp("-",Id("a"),IntLiteral(3)),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_369(self):
        input = """
            Function: foo
            Parameter: a
            Body:
                a = (b + 3 - c * d =/= 5) || (b-d<.10); 
                c[2][3] = 5\\10.2\\.func(a,b,c)+a[2+func()+c[4]];
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([],[Assign(Id("a"),BinaryOp("||",BinaryOp("=/=",BinaryOp("-",BinaryOp("+",Id("b"),IntLiteral(3)),BinaryOp("*",Id("c"),Id("d"))),IntLiteral(5)),BinaryOp("<.",BinaryOp("-",Id("b"),Id("d")),IntLiteral(10)))),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),BinaryOp("+",BinaryOp("\.",BinaryOp("\\",IntLiteral(5),FloatLiteral(10.2)),CallExpr(Id("func"),[Id("a"),Id("b"),Id("c")])),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_370(self):
        input = """
            Function: foo
            Parameter: a[3]
            Body:
                Var: x = 10.2, b = {1,2,3};
                a = (b + 3 - c * d =/= 5) || (b-d<.10); 
                c[2][3] = 5\\10.2\\.func(a,b,c)+a[2+func()+c[4]];
                If x == 3 Then
                    While a >. 3 Do
                        a(b[c[2]], "\\n\\bString_12\\f");
                        a[3 + 5 \ 2] = func("\\f\\b\\nString", funcc(1, 1.2)) * 2;
                    EndWhile.
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[3],None)],([VarDecl(Id("x"),[],FloatLiteral(10.2)),VarDecl(Id("b"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],[Assign(Id("a"),BinaryOp("||",BinaryOp("=/=",BinaryOp("-",BinaryOp("+",Id("b"),IntLiteral(3)),BinaryOp("*",Id("c"),Id("d"))),IntLiteral(5)),BinaryOp("<.",BinaryOp("-",Id("b"),Id("d")),IntLiteral(10)))),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),BinaryOp("+",BinaryOp("\.",BinaryOp("\\",IntLiteral(5),FloatLiteral(10.2)),CallExpr(Id("func"),[Id("a"),Id("b"),Id("c")])),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))]))),If([(BinaryOp("==",Id("x"),IntLiteral(3)),[],[While(BinaryOp(">.",Id("a"),IntLiteral(3)),([],[CallStmt(Id("a"),[ArrayCell(Id("b"),[ArrayCell(Id("c"),[IntLiteral(2)])]),StringLiteral("\\n\\bString_12\\f")]),Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),BinaryOp("\\",IntLiteral(5),IntLiteral(2)))]),BinaryOp("*",CallExpr(Id("func"),[StringLiteral("\\f\\b\\nString"),CallExpr(Id("funcc"),[IntLiteral(1),FloatLiteral(1.2)])]),IntLiteral(2)))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))
    
    def test_371(self):
        input = """
            Function: func
            Parameter: a  , b[3], b[2][5]
            Body:
                For (a = 3 + 5, a ,1) Do
                EndFor.
            EndBody.

            Function: funcc
            Parameter: b[3], b[2][4][3]
            Body:
                While exp == 3 Do
                EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[3],None),VarDecl(Id("b"),[2,5],None)],([],[For(Id("a"),BinaryOp("+",IntLiteral(3),IntLiteral(5)),Id("a"),IntLiteral(1),([],[]))])),FuncDecl(Id("funcc"),[VarDecl(Id("b"),[3],None),VarDecl(Id("b"),[2,4,3],None)],([],[While(BinaryOp("==",Id("exp"),IntLiteral(3)),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_372(self):
        input = """
            Function: func
            Parameter: a  , b[3], b[2][5]
            Body:
                For (a = 3 + 5, a ,1) Do
                EndFor.
            EndBody.

            Function: funcc
            Parameter: b[3], b[2][4][3]
            Body:
                While exp == 3 Do
                    If x == 5 Then
                        Do 
                            x = x + 2; 
                            Break;
                            Return;
                        While x == 3
                        EndDo.
                    EndIf.
                EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[3],None),VarDecl(Id("b"),[2,5],None)],([],[For(Id("a"),BinaryOp("+",IntLiteral(3),IntLiteral(5)),Id("a"),IntLiteral(1),([],[]))])),FuncDecl(Id("funcc"),[VarDecl(Id("b"),[3],None),VarDecl(Id("b"),[2,4,3],None)],([],[While(BinaryOp("==",Id("exp"),IntLiteral(3)),([],[If([(BinaryOp("==",Id("x"),IntLiteral(5)),[],[Dowhile(([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2))),Break(),Return(None)]),BinaryOp("==",Id("x"),IntLiteral(3)))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_373(self):
        input = """
        Function: func
        Parameter: a  , b[3], b[2][5]
        Body:
            For (a = 3 + 5, a ,1) Do
            EndFor.
        EndBody.

        Function: funcc
        Parameter: b[3], b[2][4][3]
        Body:
            While exp == 3 Do
                If x == 5 Then
                    Do 
                        x = x + 2; 
                        Break;
                        t = True;
                        goo("\\n\\b\\f\\t This is String :)");
                        Return;
                    While x == 3
                    EndDo.
                EndIf.
            EndWhile.
        EndBody.
            """
        expect = Program([FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[3],None),VarDecl(Id("b"),[2,5],None)],([],[For(Id("a"),BinaryOp("+",IntLiteral(3),IntLiteral(5)),Id("a"),IntLiteral(1),([],[]))])),FuncDecl(Id("funcc"),[VarDecl(Id("b"),[3],None),VarDecl(Id("b"),[2,4,3],None)],([],[While(BinaryOp("==",Id("exp"),IntLiteral(3)),([],[If([(BinaryOp("==",Id("x"),IntLiteral(5)),[],[Dowhile(([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2))),Break(),Assign(Id("t"),BooleanLiteral(True)),CallStmt(Id("goo"),[StringLiteral("\\n\\b\\f\\t This is String :)")]),Return(None)]),BinaryOp("==",Id("x"),IntLiteral(3)))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_374(self):
        input = """
            Function: func
            Parameter: a  , b[3], b[2][5]
            Body:  
                If x > 10.3E+5 Then
                EndIf.
            EndBody.

            Function: funcc
            Parameter: b[3], b[2][4][3]
            Body:
                While ( exp == 3) && (x == 3) Do
                    If x == (55) Then
                            x = x + 2; 
                            Break;
                            t = True;
                            goo("\\n\\b\\f\\t This is String :)");
                            Return;
                        While x == 3 Do
                        EndWhile.
                    EndIf.
                    y = (x == 5);
                EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[3],None),VarDecl(Id("b"),[2,5],None)],([],[If([(BinaryOp(">",Id("x"),FloatLiteral(1030000.0)),[],[])],([],[]))])),FuncDecl(Id("funcc"),[VarDecl(Id("b"),[3],None),VarDecl(Id("b"),[2,4,3],None)],([],[While(BinaryOp("&&",BinaryOp("==",Id("exp"),IntLiteral(3)),BinaryOp("==",Id("x"),IntLiteral(3))),([],[If([(BinaryOp("==",Id("x"),IntLiteral(55)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2))),Break(),Assign(Id("t"),BooleanLiteral(True)),CallStmt(Id("goo"),[StringLiteral("\\n\\b\\f\\t This is String :)")]),Return(None),While(BinaryOp("==",Id("x"),IntLiteral(3)),([],[]))])],([],[])),Assign(Id("y"),BinaryOp("==",Id("x"),IntLiteral(5)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    
    def test_375(self):
        input = """
        Var: x[3] = {10.5E+3};
            Function: func
            Parameter: a
            Body:  
                If x > 10.3E+5 Then
                EndIf.
            EndBody.
        """
        expect = Program([VarDecl(Id("x"),[3],ArrayLiteral([FloatLiteral(10500.0)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None)],([],[If([(BinaryOp(">",Id("x"),FloatLiteral(1030000.0)),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))
    
    def test_376(self):
        input = """
            Var: x[3] = {10.5E+3, 0x123};
        """
        expect = Program([VarDecl(Id("x"),[3],ArrayLiteral([FloatLiteral(10500.0),IntLiteral(291)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_377(self):
        input = """
            Var: x[3] = {0xA12, 0o7777, 0O123, 0XFFFFF};
        """
        expect = Program([VarDecl(Id("x"),[3],ArrayLiteral([IntLiteral(2578),IntLiteral(4095),IntLiteral(83),IntLiteral(1048575)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_378(self):
        input = """
            Var: x[3] = {0xA12, 0o7777, 0O123, 0XFFFFF};
            Var: x[3][0xAAA][0O12370], f = {2,3,4, True, False, "\\n\\f\\bstring\\b'\""};
        """
        expect = Program([VarDecl(Id("x"),[3],ArrayLiteral([IntLiteral(2578),IntLiteral(4095),IntLiteral(83),IntLiteral(1048575)])),VarDecl(Id("x"),[3,2730,5368],None),VarDecl(Id("f"),[],ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4),BooleanLiteral(True),BooleanLiteral(False),StringLiteral("\\n\\f\\bstring\\b\'\"")]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_379(self):
        input = """
            Var: x[3] = {0xA12, 0o7777, 0O123, 0XFFFFF};
            Var: x[3][0xAAA][0O12370], f = {2,3,4, True, False, "\\n\\f\\bstring\\b'\""};
            Function: func
            Body:  
                If x == 10.e+56 Then
                    If y == "'\"\\n\\b\\\\" Then
                        Do 
                            x = x +. 3;
                        While x >=. 3.e-3 EndDo.
                    EndIf.
                EndIf.
            EndBody.
        """
        expect = Program([VarDecl(Id("x"),[3],ArrayLiteral([IntLiteral(2578),IntLiteral(4095),IntLiteral(83),IntLiteral(1048575)])),VarDecl(Id("x"),[3,2730,5368],None),VarDecl(Id("f"),[],ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4),BooleanLiteral(True),BooleanLiteral(False),StringLiteral("\\n\\f\\bstring\\b\'\"")])),FuncDecl(Id("func"),[],([],[If([(BinaryOp("==",Id("x"),FloatLiteral(1e+57)),[],[If([(BinaryOp("==",Id("y"),StringLiteral("\'\"\\n\\b\\\\")),[],[Dowhile(([],[Assign(Id("x"),BinaryOp("+.",Id("x"),IntLiteral(3)))]),BinaryOp(">=.",Id("x"),FloatLiteral(0.003)))])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_380(self):
        input = """
            Var: x[3] = {0xA12, 0o7777, 0O123, 0XFFFFF, 0.e-3};
            Var: x[3][0xAAA][0O12370], f = {2,3,4, True, False, "\\n\\f\\bstring\\b'\""};
            Function: func
            Body:  
                If x == 10.e+56 Then
                    If y =/= "'\"\\n\\b\\\\" Then
                        Do 
                            x = x -. 3;
                            func();
                            Return;
                            Continue;
                            Break;
                            f = !(a <. (b <= (c >= (d =/= (f == (g != (z >. (y >= t || f && g + f *. y \\. u % p \\ u))))))));
                        While x != 3.e-3 EndDo.
                    EndIf.
                EndIf.
            EndBody.
        """
        expect = Program([VarDecl(Id("x"),[3],ArrayLiteral([IntLiteral(2578),IntLiteral(4095),IntLiteral(83),IntLiteral(1048575),FloatLiteral(0.0)])),VarDecl(Id("x"),[3,2730,5368],None),VarDecl(Id("f"),[],ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4),BooleanLiteral(True),BooleanLiteral(False),StringLiteral("\\n\\f\\bstring\\b\'\"")])),FuncDecl(Id("func"),[],([],[If([(BinaryOp("==",Id("x"),FloatLiteral(1e+57)),[],[If([(BinaryOp("=/=",Id("y"),StringLiteral("\'\"\\n\\b\\\\")),[],[Dowhile(([],[Assign(Id("x"),BinaryOp("-.",Id("x"),IntLiteral(3))),CallStmt(Id("func"),[]),Return(None),Continue(),Break(),Assign(Id("f"),UnaryOp("!",BinaryOp("<.",Id("a"),BinaryOp("<=",Id("b"),BinaryOp(">=",Id("c"),BinaryOp("=/=",Id("d"),BinaryOp("==",Id("f"),BinaryOp("!=",Id("g"),BinaryOp(">.",Id("z"),BinaryOp(">=",Id("y"),BinaryOp("&&",BinaryOp("||",Id("t"),Id("f")),BinaryOp("+",Id("g"),BinaryOp("\\",BinaryOp("%",BinaryOp("\.",BinaryOp("*.",Id("f"),Id("y")),Id("u")),Id("p")),Id("u"))))))))))))))]),BinaryOp("!=",Id("x"),FloatLiteral(0.003)))])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_381(self):
        input = """
            Function: func
            Body:  
                If x == 10.e+56 Then
                    If y =/= "'\"\\n\\b\\\\" Then
                        Do 
                            
                        While x != 3.e-3 EndDo.
                        While x >=. 0.e-5 Do EndWhile.
                        var = x && f || z + y +. t - a -.p * f *. t \\ k \\. y % z || (!y) ;
                        y = y -. 2;
                    EndIf.
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("func"),[],([],[If([(BinaryOp("==",Id("x"),FloatLiteral(1e+57)),[],[If([(BinaryOp("=/=",Id("y"),StringLiteral("\'\"\\n\\b\\\\")),[],[Dowhile(([],[]),BinaryOp("!=",Id("x"),FloatLiteral(0.003))),While(BinaryOp(">=.",Id("x"),FloatLiteral(0.0)),([],[])),Assign(Id("var"),BinaryOp("||",BinaryOp("||",BinaryOp("&&",Id("x"),Id("f")),BinaryOp("-.",BinaryOp("-",BinaryOp("+.",BinaryOp("+",Id("z"),Id("y")),Id("t")),Id("a")),BinaryOp("%",BinaryOp("\.",BinaryOp("\\",BinaryOp("*.",BinaryOp("*",Id("p"),Id("f")),Id("t")),Id("k")),Id("y")),Id("z")))),UnaryOp("!",Id("y")))),Assign(Id("y"),BinaryOp("-.",Id("y"),IntLiteral(2)))])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))
    def test_382(self):
        input = """
            Function: func
            Body:  
                If x == 0X3FABCABDE Then
                    If y =/= "'\"\\n\\b\\\\" Then
                        Do 
                            
                        While x != 3.e-3 EndDo.
                        While x >=. 0.e-5 Do EndWhile.
                        Continue;
                        Break;
                        func(a[f[z[a[r[t[y[u[i[o[p[l[k[j[h[g[f[d + 0XF12]]]]]]]]]]]]]]]]]);
                    EndIf.
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("func"),[],([],[If([(BinaryOp("==",Id("x"),IntLiteral(17091570654)),[],[If([(BinaryOp("=/=",Id("y"),StringLiteral("\'\"\\n\\b\\\\")),[],[Dowhile(([],[]),BinaryOp("!=",Id("x"),FloatLiteral(0.003))),While(BinaryOp(">=.",Id("x"),FloatLiteral(0.0)),([],[])),Continue(),Break(),CallStmt(Id("func"),[ArrayCell(Id("a"),[ArrayCell(Id("f"),[ArrayCell(Id("z"),[ArrayCell(Id("a"),[ArrayCell(Id("r"),[ArrayCell(Id("t"),[ArrayCell(Id("y"),[ArrayCell(Id("u"),[ArrayCell(Id("i"),[ArrayCell(Id("o"),[ArrayCell(Id("p"),[ArrayCell(Id("l"),[ArrayCell(Id("k"),[ArrayCell(Id("j"),[ArrayCell(Id("h"),[ArrayCell(Id("g"),[ArrayCell(Id("f"),[BinaryOp("+",Id("d"),IntLiteral(3858))])])])])])])])])])])])])])])])])])])])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_383(self):
        input = """
            Function: func
            Body:  
                If x == 0X3FABCABDE Then
                    If y =/= "'\"\\n\\b\\\\" Then
                        Do 
                            func(a[f[z[a[r[t[y[u[i[o[p[l[k[j[h[g[f[d + 0XF12]]]]]]]]]]]]]]]]], 0O120, "\\\\'\"");

                        While x != 3.e+11 EndDo.
                        While x >=. 0.e+5 Do EndWhile.                                                
                    EndIf.
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("func"),[],([],[If([(BinaryOp("==",Id("x"),IntLiteral(17091570654)),[],[If([(BinaryOp("=/=",Id("y"),StringLiteral("\'\"\\n\\b\\\\")),[],[Dowhile(([],[CallStmt(Id("func"),[ArrayCell(Id("a"),[ArrayCell(Id("f"),[ArrayCell(Id("z"),[ArrayCell(Id("a"),[ArrayCell(Id("r"),[ArrayCell(Id("t"),[ArrayCell(Id("y"),[ArrayCell(Id("u"),[ArrayCell(Id("i"),[ArrayCell(Id("o"),[ArrayCell(Id("p"),[ArrayCell(Id("l"),[ArrayCell(Id("k"),[ArrayCell(Id("j"),[ArrayCell(Id("h"),[ArrayCell(Id("g"),[ArrayCell(Id("f"),[BinaryOp("+",Id("d"),IntLiteral(3858))])])])])])])])])])])])])])])])])]),IntLiteral(80),StringLiteral("\\\\\'\"")])]),BinaryOp("!=",Id("x"),FloatLiteral(300000000000.0))),While(BinaryOp(">=.",Id("x"),FloatLiteral(0.0)),([],[]))])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))
    
    def test_384(self):
        input = """
            Var: x = "\\\\'\"\\f\\n";
            Function: func
            Body:  
                If x == 0X3FABCABDE0000000 Then
                    If y =/= "'\"\\n\\b\\\\" Then
                        Do 
                            
                        While x == 0 EndDo.
                        While x >=. 0 Do EndWhile.
                        If x == "\\\\a\\n" Then
                        EndIf.
                    EndIf.
                EndIf.
            EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],StringLiteral("\\\\\'\"\\f\\n")),FuncDecl(Id("func"),[],([],[If([(BinaryOp("==",Id("x"),IntLiteral(4587983562262708224)),[],[If([(BinaryOp("=/=",Id("y"),StringLiteral("\'\"\\n\\b\\\\")),[],[Dowhile(([],[]),BinaryOp("==",Id("x"),IntLiteral(0))),While(BinaryOp(">=.",Id("x"),IntLiteral(0)),([],[])),If([(BinaryOp("==",Id("x"),StringLiteral("\\\\a\\n")),[],[])],([],[]))])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))
    
    def test_385(self):
        input = """
            Function: func
            Body:  
                If x == 0.E+12 Then
                    If y =/= "'\"\\n\\b\\\\" Then
                      
                    EndIf.
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("func"),[],([],[If([(BinaryOp("==",Id("x"),FloatLiteral(0.0)),[],[If([(BinaryOp("=/=",Id("y"),StringLiteral("\'\"\\n\\b\\\\")),[],[])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))
    
    def test_386(self):
        input = """
            Function: func
            Body:  
                If x == 0X3FABCABDE Then
                    If y =/= "'\"\\n\\b\\\\" Then
                        Do 
                            
                        While x != 3.e-3 EndDo.
                        While x >=. 0.e-5 Do
                            hi = ":)";
                            func("'\"\\\\");
                            x = func("hi ;)", "00000213");
                            ** this is a comment :))))))))**
                        EndWhile.                    
                    EndIf.
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("func"),[],([],[If([(BinaryOp("==",Id("x"),IntLiteral(17091570654)),[],[If([(BinaryOp("=/=",Id("y"),StringLiteral("\'\"\\n\\b\\\\")),[],[Dowhile(([],[]),BinaryOp("!=",Id("x"),FloatLiteral(0.003))),While(BinaryOp(">=.",Id("x"),FloatLiteral(0.0)),([],[Assign(Id("hi"),StringLiteral(":)")),CallStmt(Id("func"),[StringLiteral("\'\"\\\\")]),Assign(Id("x"),CallExpr(Id("func"),[StringLiteral("hi ;)"),StringLiteral("00000213")]))]))])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))
    
    def test_387(self):
        input = """
            Function: func
            Body:  
                If x == 0 Then
                    If y =/= "'\"\\n\\b\\\\" Then
                       
                    EndIf.

                EndIf.
                func("'\"\\\\");
                Return x == 3;
            EndBody.
        """
        expect = Program([FuncDecl(Id("func"),[],([],[If([(BinaryOp("==",Id("x"),IntLiteral(0)),[],[If([(BinaryOp("=/=",Id("y"),StringLiteral("\'\"\\n\\b\\\\")),[],[])],([],[]))])],([],[])),CallStmt(Id("func"),[StringLiteral("\'\"\\\\")]),Return(BinaryOp("==",Id("x"),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))
    
    def test_388(self):
        input = """
            Var: f[3] = {{{{{{{{{{{{{{{{{{1}}}}}}}}}}}}}}}}}};
            Function: func
            Body:  
                
            EndBody.
        """
        expect = Program([VarDecl(Id("f"),[3],ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])])])])])])])])])])])])])])])])])])),FuncDecl(Id("func"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))
    
    def test_389(self):
        input = """
            Function: func
            Body:  
                
            EndBody.

            Function: function
            Body:  
                Var: f[3] = {{{{0X1FF0,"\\\\",2,{1,2,3},{{{{{{{{{{{{{{1}}}}}}}}}}}}}}}}}};
            EndBody.
        """
        expect = Program([FuncDecl(Id("func"),[],([],[])),FuncDecl(Id("function"),[],([VarDecl(Id("f"),[3],ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(8176),StringLiteral("\\\\"),IntLiteral(2),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])])])])])])])])])])])])])])])])])]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))
    
    def test_390(self):
        input = """
            Var: x = {{{1,2,3}, 0}, {True, False}, "\\\\"};
            Var: x;
        """
        expect = Program([VarDecl(Id("x"),[],ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),IntLiteral(0)]),ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False)]),StringLiteral("\\\\")])),VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))
    
    def test_391(self):
        input = """
            Var: a[1][0xABC] = {0o7023,{1.25E-36,1.25E+36}};
        """
        expect = Program([VarDecl(Id("a"),[1,2748],ArrayLiteral([IntLiteral(3603),ArrayLiteral([FloatLiteral(1.25e-36),FloatLiteral(1.25e+36)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))
    
    def test_392(self):
        input = """
            Function: func
            Body:  
                If True Then
                    Var: a[1][0xABC] = {0o7023,{1.25E-36,1.25E+36}};
                    For (a = 5, a == "'\"" , a + 3) Do
                        func(x);
                    EndFor.
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("func"),[],([],[If([(BooleanLiteral(True),[VarDecl(Id("a"),[1,2748],ArrayLiteral([IntLiteral(3603),ArrayLiteral([FloatLiteral(1.25e-36),FloatLiteral(1.25e+36)])]))],[For(Id("a"),IntLiteral(5),BinaryOp("==",Id("a"),StringLiteral("\'\"")),BinaryOp("+",Id("a"),IntLiteral(3)),([],[CallStmt(Id("func"),[Id("x")])]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))
    
    def test_393(self):
        input = """
            Function: func
            Body:  
                Var: x = 0O120000000000000000000000000000;
            EndBody.
        """
        expect = Program([FuncDecl(Id("func"),[],([VarDecl(Id("x"),[],IntLiteral(193428131138340667952988160))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))
    
    def test_394(self):
        input = """
            Function: foo
            Body:
                Do 
                    Var: f[3] = {{{{0X1FF0,"\\\\",2,{1,2,3},{{{{{{{{{{{{{{1}}}}}}}}}}}}}}}}}};
                    a = (b + 3);                        
                    t = x[3];
                    c[func(3)+5*op[x[y[z[3]]]]] = 3;
                    c[2][3] = (((5)));
                While x == y EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([VarDecl(Id("f"),[3],ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(8176),StringLiteral("\\\\"),IntLiteral(2),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])])])])])])])])])])])])])])])])])]))],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(Id("t"),ArrayCell(Id("x"),[IntLiteral(3)])),Assign(ArrayCell(Id("c"),[BinaryOp("+",CallExpr(Id("func"),[IntLiteral(3)]),BinaryOp("*",IntLiteral(5),ArrayCell(Id("op"),[ArrayCell(Id("x"),[ArrayCell(Id("y"),[ArrayCell(Id("z"),[IntLiteral(3)])])])])))]),IntLiteral(3)),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),IntLiteral(5))]),BinaryOp("==",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_395(self):
        input = """
            Var: x[3];
            Function: func
            Body:
                Do Do Do Do Do Do Do Do Do Do Do While x == "\\\\"
                EndDo. While x == "\\\\"
                EndDo. While x == "\\\\"
                EndDo. While x == "\\\\"
                EndDo. While x == "\\\\"
                EndDo. While x == "\\\\"
                EndDo. While x == "\\\\"
                EndDo. While x == "\\\\"
                EndDo. While x == "\\\\"
                EndDo. While x == "\\\\"
                EndDo. While x == "\\\\"
                EndDo.
                Return;
            EndBody.
        """
        expect = Program([VarDecl(Id("x"),[3],None),FuncDecl(Id("func"),[],([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[]),BinaryOp("==",Id("x"),StringLiteral("\\\\")))]),BinaryOp("==",Id("x"),StringLiteral("\\\\")))]),BinaryOp("==",Id("x"),StringLiteral("\\\\")))]),BinaryOp("==",Id("x"),StringLiteral("\\\\")))]),BinaryOp("==",Id("x"),StringLiteral("\\\\")))]),BinaryOp("==",Id("x"),StringLiteral("\\\\")))]),BinaryOp("==",Id("x"),StringLiteral("\\\\")))]),BinaryOp("==",Id("x"),StringLiteral("\\\\")))]),BinaryOp("==",Id("x"),StringLiteral("\\\\")))]),BinaryOp("==",Id("x"),StringLiteral("\\\\")))]),BinaryOp("==",Id("x"),StringLiteral("\\\\"))),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    
    def test_396(self):
        input = """
            Var: x = 3;
            Function: func
            Parameter: x
            Body:
                x = func("\\\\'\"", func("\\\\'\"", func("\\\\'\"", func("\\\\'\"", func("\\\\'\"", func("\\\\'\"", func()))))));
                Return;
            EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(3)),FuncDecl(Id("func"),[VarDecl(Id("x"),[],None)],([],[Assign(Id("x"),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[])])])])])])])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))
    
    def test_397(self):
        input = """
            Var: x = 3;
            Function: func
            Parameter: x
            Body:
                x = func("\\\\'\"", func("\\\\'\"", func("\\\\'\"", func("\\\\'\"", func("\\\\'\"", func("\\\\'\"", func()))))));
                Return;
            EndBody.
            Function: func
            Parameter: x[0O170]
            Body:
                x = func("\\\\'\"", func("\\\\'\"", func("\\\\'\"", {1,2,3,4,{1,2,3}, True, False, 0.E+5} ,func("\\\\'\"", func("\\\\'\"", func("\\\\'\"", func()))))));
                Return;
            EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(3)),FuncDecl(Id("func"),[VarDecl(Id("x"),[],None)],([],[Assign(Id("x"),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[])])])])])])])),Return(None)])),FuncDecl(Id("func"),[VarDecl(Id("x"),[120],None)],([],[Assign(Id("x"),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),BooleanLiteral(True),BooleanLiteral(False),FloatLiteral(0.0)]),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[StringLiteral("\\\\\'\""),CallExpr(Id("func"),[])])])])])])])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))
    
    def test_398(self):
        input = """
            Function: func
            Parameter: x[3], b[3]
            Body:
                If x < 3 Then
                    If x < 3 Then
                        If x < 3 Then
                            If x < 3 Then
                                If x < 3 Then
                                    If x < 3 Then
                EndIf.
                EndIf.
                EndIf.
                EndIf.
                EndIf.
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("func"),[VarDecl(Id("x"),[3],None),VarDecl(Id("b"),[3],None)],([],[If([(BinaryOp("<",Id("x"),IntLiteral(3)),[],[If([(BinaryOp("<",Id("x"),IntLiteral(3)),[],[If([(BinaryOp("<",Id("x"),IntLiteral(3)),[],[If([(BinaryOp("<",Id("x"),IntLiteral(3)),[],[If([(BinaryOp("<",Id("x"),IntLiteral(3)),[],[If([(BinaryOp("<",Id("x"),IntLiteral(3)),[],[])],([],[]))])],([],[]))])],([],[]))])],([],[]))])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))
    
    def test_399(self):
        input = """
            Function: func
            Body:
            While a > 4 Do
                While a > 4 Do
                    While a > 4 Do
                        While a > 4 Do
                            While a > 4 Do
                            EndWhile.
                        EndWhile.
                    EndWhile.                    
                EndWhile.
            EndWhile.
            EndBody.
        """
        expect = Program([FuncDecl(Id("func"),[],([],[While(BinaryOp(">",Id("a"),IntLiteral(4)),([],[While(BinaryOp(">",Id("a"),IntLiteral(4)),([],[While(BinaryOp(">",Id("a"),IntLiteral(4)),([],[While(BinaryOp(">",Id("a"),IntLiteral(4)),([],[While(BinaryOp(">",Id("a"),IntLiteral(4)),([],[]))]))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))