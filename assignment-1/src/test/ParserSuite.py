import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_declaration_variable_0(self):
        input = """Var: x = {{1,2,3}, {2,3,4}, {1,2}"""
        expect = "Error on line 1 col 33: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_declaration_variable_1(self):
        input = """Var: a = + 3, b = +5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_declaration_variable_2(self):
        input = """Var: a, b = 5,     c    = 10, d, e,f,g,    h;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_declaration_variable_3(self):
        input = """Var:"""
        expect = "Error on line 1 col 4: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_declaration_variable_4(self):
        input = """Var: a[2] = {1, 2, 3}, b = 4, c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_declaration_variable_5(self):
        input = """Varr x;"""
        expect = "Error on line 1 col 3: r"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_declaration_variable_6(self):
        input = """Var: m[10], a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_declaration_variable_7(self):
        input = """Var: x;;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_declaration_variable_8(self):
        input = """Var: x = 3, {1, 2};"""
        expect = "Error on line 1 col 12: {"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_declaration_variable_9(self):
        input = """Var: x[3 = {2}"""
        expect = "Error on line 1 col 9: ="
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_declaration_variable_10(self):
        input = """Var: x[3] = {2, 3, 5}, b = """
        expect = "Error on line 1 col 27: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_declaration_variable_11(self):
        input = """Var: x[3] = {2, 3, 5}, b = 03"""
        expect = "Error on line 1 col 28: 3"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_function_1(self):
        input = """
            Function: foo
            Parameter: a[5], b
            Body:
            EndBody.
            .
        """
        expect = "Error on line 6 col 12: ."
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_function_2(self):
        input = """
            Function: foo
            Body:
                Var: a = 5;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    # def test_function_3(self):
        # input = """
            # Function: foo
            # Parameter: a , b[2]
            # Body:
                # Var: a = 5;
                # x = 2;
            # EndBody.
        # """
        # expect = "successful"
        # self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_function_4(self):
        input = """
            Function: foo
            Parameter: a, b[2]
            Body:
                Var: a = 5
                x = 2;
            EndBody.
        """
        expect = "Error on line 6 col 16: x"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_function_5(self):
        input = """
            Function: foo
            Parameter: a , b[2]
            Body:
                Var: a = 5;
                x = (4. \. 3.) *. 3.14 *. r *. r *. r;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_function_6(self):
        input = """
            Function: foo
            Parameter: a , b[2]
            Body:
                Var: r = 10., abc[25][16] = {{1,2,3}, {5,6,7}};
                x = (4. \. 3.) *. 3.14 *. r *. r *. r;
                a[3 + foo(2)] = a[b[2][3]] + 4;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_function_7(self):
        input = """
            Function: foo
            Parameter: a
            Body:
                Var: r = 10., abc[25][16] = {{1,2,3}, {5,6,7}};
                x = (4. \. 3.) *. 3.14 *. r *. r *. r;
                a[3 + foo(2] = a[b[2][3]] + 4;
            EndBody.
        """
        expect = "Error on line 7 col 27: ]"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_function_8(self):
        input = """
            Function: foo
            Parameter: a, b[2] , b[]
            Body:
                Var: r = 10., abc[25][16] = {{1,2,3}, {5,6,7}};
                x = (4. \. 3.) *. 3.14 *. r *. r *. r;
                a[3 + foo(ii)] = a[b[2][3]] + 4;
            EndBody.
        """
        expect = "Error on line 3 col 35: ]"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_function_9(self):
        input = """
            Function: foo
            Parameter: a, b[3]
            Body:
                x = (4. \. 3.) *. 3.14 *. r *. r *. r;
                Var: r = 10., abc[25][16] = {{1,2,3}, {5,6,7}};
                a[3 + foo(ii)] = a[b[2][3]] + 4;
            EndBody.
        """
        expect = "Error on line 6 col 16: Var"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_function_10(self):
        input = """
            Function: foo
            Parameter: a , b[2] , b[3]
            Body:
                Var: r = 10., abc[25][16] = {{1,2,3}, {5,6,7}};
                x = (4. \. 3.) *. 3.14 *. r *. r *. r;
                a[3 + foo(ii)] = a[b[2][3]] + 4;;
            EndBody.
        """
        expect = "Error on line 7 col 48: ;"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_if_statement_1(self):
        input = """
            Function: foo
            Parameter: a , b[2], b[3]
            Body:
                Var: r = 10., abc[25][16] = {{1,2,3}, {5,6,7}};
                If a + b Then c = 10;
                ElseIf c == 6 Then d = 12;
                Else
                EndIf
            EndBody.
        """
        expect = "Error on line 10 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_if_statement_2(self):
        input = """
            Function: foo
            Parameter: a ,  b[3]
            Body:
                Var: r = 10., abc[25][16] = {{1,2,3}, {5,6,7}};
                If a + b Then c = 10;
                ElseIf c = 6 Then d = 12;
                EndIf.
            EndBody.
        """
        expect = "Error on line 7 col 25: ="
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_if_statement_3(self):
        input = """
            Function: foo
            Body:
                Var: r = 10., abc[25][16] = {{1,2,3}, {5,6,7}};
                If a + b Then c = 10;
                ElseIf c == (((2 + 5)\ 2)* 6) Then d = 12;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_if_statement_4(self):
        input = """
            Function: foo
            Parameter: a
            Body:
                Var: r = 10., abc[25][16] = {{1,2,3}, {5,6,7}};
                If a + b c = 10 Then;
                ElseIf c == (((2 + 5)\ 2)* 6) Then d = 12;
                EndIf.
            EndBody.
        """
        expect = "Error on line 6 col 25: c"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_if_statement_5(self):
        input = """
            Function: foo
            Parameter: a
            Body:
                If c = 10 Then
                EndIf.
            EndBody.
        """
        expect = "Error on line 5 col 21: ="
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_if_statement_6(self):
        input = """
            Function: foo
            Parameter: a
            Body:
                If c == 10 Then
                EndIf
                EndIf.
            EndBody.
        """
        expect = "Error on line 7 col 16: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_if_statement_7(self):
        input = """
            Function: foo
            Parameter: a
            Body:
                If c == 10 Then
                ElseIf ** comment ** Then
                EndIf.
            EndBody.
        """
        expect = "Error on line 6 col 37: Then"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_if_statement_8(self):
        input = """
            Function: foo
            Parameter: a
            Body:
                If c == 10 Then
                ElseIf a -   ** comment ** 3 Then
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_if_statement_9(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_if_statement_10(self):
        input = """
            Function: foo
            Parameter: a
            Body:
                If c == 10 Then
                ElseIf a -   ** comment ** 3 Then
                ElseIf a -   ** comment ** 3 Then
                ElseIf a -   ** comment ** 3 Then
                Else
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_for_statement_1(self):
        input = """
            Function: foo
            Parameter: a
            Body:
                For (a = 3 + 5, a != 3, a = a + 1) Do
                    c = c + 3;
                EndFor.
            EndBody.
        """
        expect = "Error on line 5 col 42: ="
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_for_statement_2(self):
        input = """
            Function: foo
            Parameter: a, b[2], b[3]
            Body:
                For (a = 3 + 5; a != 3, a = a + 1) Do
                    c = c + 3;
                EndFor.
            EndBody.
        """
        expect = "Error on line 5 col 30: ;"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_for_statement_3(self):
        input = """
            Function: foo
            Parameter: a, b[2], b[3]
            Body:
                For (a = 3 + 5, , a = a + 1) Do
                EndFor.
            EndBody.
        """
        expect = "Error on line 5 col 32: ,"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_for_statement_4(self):
        input = """
            Function: foo
            Parameter: a  , b[3]
            Body:
                For (a = 3 + 5, a ,1) Do
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_for_statement_5(self):
        input = """
            Function: foo
            Body:
                For (a = 3 + 5, a , a) Do EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_while_statement_1(self):
        input = """
            Var: a = 12, d[2] = {1,2,4};
            Var: a = 5;
            Function: foo
            Body:
                While (bc == 5) Do a = c; x = y; EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_while_statement_2(self):
        input = """
            Function: foo
            Body:
                While a = 1 Do a= 5 EndWhile.
            EndBody.
        """
        expect = "Error on line 4 col 24: ="
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_while_statement_3(self):
        input = """
            Function: foo
            Body:
                While a ==1 o a= 5 EndWhile.
            EndBody.
        """
        expect = "Error on line 4 col 28: o"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_while_statement_7(self):
        input = """
            Function: foo
            Body:
                Var: x = 2;
                While a == 1 Do
                    a = 5;
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_do_while_statement_1(self):
        input = """
            Function: foo
            Body:
                Do a = b + 3; c[2][3] = 5; While x == y EndDo.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_do_while_statement_2(self):
        input = """
            Function: foo
            Body:
                Do a = b + 3; c[2][3] = 5; While x = y EndDo.
            EndBody.
        """
        expect = "Error on line 4 col 51: ="
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_do_while_statement_3(self):
        input = """
            Function: foo
            Body:
                Do a = b + 3; c[2][3] = 5; While x == y EndDo
            EndBody.
        """
        expect = "Error on line 5 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_do_while_statement_4(self):
        input = """
            Function: foo
            Body:
                o a = b + 3; c[2][3] = 5; While x == y EndDo.
            EndBody.
        """
        expect = "Error on line 4 col 18: a"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_do_while_statement_5(self):
        input = """
            Function: foo
            Body:
                Do a == b + 3; c[2][3] = 5; While x == y EndDo.
            EndBody.
        """
        expect = "Error on line 4 col 21: =="
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_do_while_statement_6(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3); c[2][3] = (((5))); While x == y EndDo.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_do_while_statement_7(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3);
                c[2][3] = (((5)));
                While
                While x == y EndDo.
            EndBody.
        """
        expect = "Error on line 7 col 16: While"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_do_while_statement_8(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3);
                c[2][3] = (((5)));
                If a = 3;
                While x == y EndDo.
            EndBody.
        """
        expect = "Error on line 6 col 21: ="
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_do_while_statement_9(self):
        input = """
            Function: foo
            Body:
                Do a == (b + 3);
                c[2][3] = (((5)));
                While x == y EndDo.
            EndBody.
        """
        expect = "Error on line 4 col 21: =="
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_do_while_statement_10(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3);
                                            xyz = x[3];
                c[2][3] = (((5)));
                While x == y EndDo.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_do_while_statement_11(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_do_while_statement_12(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_do_while_statement_13(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3);
                                            xyz = x[3];
                                c[func(3)+5*op[x[y[z[3]]]]] = 3;
                c[2][3] = (((5)));
                While x - y. EndDo.
            EndBody.
        """
        expect = "Error on line 8 col 27: ."
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_do_while_statement_14(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3);
                x(y) = 5;
                c[2][3] = (((5)));
                While x - y. EndDo.
            EndBody.
        """
        expect = "Error on line 5 col 21: ="
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_do_while_statement_15(self):
        input = """
            Function: foo
            Body:
                Do a = (b + 3);
                x(y)              ; ** hello **
                c[2][3] = (((5)));
                While x - y EndDo.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_call_statement_1(self):
        input = """
            Function: foo
            Body:
                foo( );
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_call_statement_2(self):
        input = """
            Function: foo
            Body:
                foo(x + 2, 4. \. y);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_call_statement_3(self):
        input = """
            Function: foo
            Body:
                foo(x + 2 4. \. y);
            EndBody.
        """
        expect = "Error on line 4 col 26: 4."
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_call_statement_4(self):
        input = """
            Function: foo
            Body:
                foo(func(a + 2, b \ 3) + 3 * 6, zz);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_call_statement_5(self):
        input = """
            Function: foo
            Body:
                foo(func(a + 2, b \ 3) + 3 * 6 zz);
            EndBody.
        """
        expect = "Error on line 4 col 47: zz"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_function_call_1(self):
        input = """
            Function: foo
            Body:
                x = foo(2 + 4, another_foo(2,3 \ 5));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_function_call_2(self):
        input = """
            Function: foo
            Body:
                x = foo(2 + 4, another_foo(2,3 \ 5););
            EndBody.
        """
        expect = "Error on line 4 col 51: ;"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_while_statement_4(self):
        input = """
            Function: foo
            Body:
                While a == 3 Do x = x + 1; Break EndWhile.
            EndBody.
        """
        expect = "Error on line 4 col 49: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_while_statement_5(self):
        input = """
            Function: foo
            Body:
                While a == 3 Do x = x + 1; Break;
                Continue;
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_while_statement_6(self): #think
        input = """
            Function: foo
            Body:
                While a == 3 Do x = x + 1; break; EndWhile.
            EndBody.
        """
        expect = "Error on line 4 col 48: ;"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_comment_1(self): #think
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
        """
        expect = "Error on line 11 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_comment_2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_comment_3(self):
        input = """
            Var: x = 3;
            **This is single line comment**
            Function: function
            Parameter: x, y
            ** abc_xyz***
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
                For (a = 3, b && c || d && e, i = i \ 3)
                **////abc_xyz**
                Do x = x + 2; y = y + 3;
                EndFor.
            EndBody.
        """
        expect = "Error on line 6 col 24: *"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_comment_4(self):
        input = """
            Var: x = 3;
            **This is single line comment**
            ****************Var: abc = 5;****
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_comment_5(self):
        input = """
            Var: x = 3;
            **This is single line comment**
            ****************************************************
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_comment_6(self):
        input = """
            Var: x = 3;
            **This is single line comment**
            *****************************************************
        """
        expect = "Error on line 4 col 64: *"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_comment_7(self):
        input = """
            Var: x = 3;
            **This is single line comment**
            ****************************************************
            **
            Var !@#$%^&*()_+)
            **
            Var: x = 2,    b, c ,   d, e = 55;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_comment_8(self):
        input = """
            **This is single line comment**
            ****************************************************
            **
            Var !@#$%^&*()_+)
            **
            Var: x = 2,   , b, c ,   d, e = 55;
        """
        expect = "Error on line 7 col 26: ,"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_while_statement_9(self):
        input = """
    Function: main
        Body:
            While (n<10) && (m>0) && (check!= False) Do
                write(n);
                m = 1.2 +. n \\. i *. a[b[1][3]];
                If m*n!=0 Then
                    While (m>10000) && (m<=foo(z))
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
        expect = "Error on line 9 col 20: m"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_while_statement_8(self):
        input = """
            Var: x,a= + 6,arr[3][4] = {-1,a,b,c,d};
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_while_statement_(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3, "string"};
            Function: add
            Parameter: a, b
            Body:
                While (b < 2.12) Do
                    i = i + 1;
                    Var: x = 3;
                EndWhile.
                Return a+b;
            EndBody.
            """
        expect = "Error on line 8 col 20: Var"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_while_statement_10(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3};
            Function: add
            Parameter: a, b
            Body:
                While (a + b < 2.12) Do
                    i = i + 1;
                EndWhile.
                Return a+b;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_while_statement_11(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3};
            Function: add
            Parameter: a, b
            Body:
                While (a + b < 2.12) Do
                    i = i + 1;
                EndWhile.
                Var: x;
                Return a+b;
            EndBody.
            """
        expect = "Error on line 9 col 16: Var"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_while_statement_12(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3};
            Function: add
            Parameter: a, b
            Body:
                While (a == 0012) Do
                    i = i + 1;
                EndWhile.
                Return a+b;
            EndBody.
            """
        expect = "Error on line 6 col 29: 0"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_while_statement_13(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3};
            Function: add
            Parameter: a, b
            Body:
                While (a =. 12) Do
                    i = i + 1;
                EndWhile.
                Return a+b;
            EndBody.
            """
        expect = "Error on line 6 col 25: ="
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_while_statement_14(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_while_statement_15(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3};
            Function: add
            Parameter: a, b
            Body:
                While (a != 12) Do
                    Break;
                    Continue
                    i = i + 1;
                EndWhile.
                Return a+b;
            EndBody.
            """
        expect = "Error on line 9 col 20: i"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_while_statement_16(self):
        input = """
            Function: add
            Body:
                While (a != 12) Do
                    x[a[a[3]]] = "hello";
                EndWhile.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_while_statement_17(self):
        input = """
            Var: x,a=6,arr[3][4] = {1,2,3};
            Function: add
            Parameter: a, b
            Body:
                While (a != 12) Do
                    Break;
                    Continue
                    i = i + 1;
                EndWhile.
                Return a+b;
            EndBody.
            """
        expect = "Error on line 9 col 20: i"
        self.assertTrue(TestParser.checkParser(input,expect,200))

    def test_while_statement_18(self):
        input = """
            Function: add
            Body:
                While (a != 12) Do
                    x[a[a[3]] = "hello";
                EndWhile.
            EndBody.
            """
        expect = "Error on line 5 col 30: ="
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_while_statement_19(self):
        input = """
            Function: add
            Body:
                While (a != 12) Do
                    x[a[a[3]]] = {1,2,3,4};
                EndWhile.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_while_statement_20(self):
        input = """
            Function: add
            Body:
                While (a != 12) Do
                    x[a[a[3]]] = {1,a,3,4};
                EndWhile.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_while_statement_21(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_while_statement_22(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Body:
            While (a < 5) && (j>6) || (k==7) d
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = "Error on line 5 col 45: d"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_while_statement_23(self):
        input = """
        Function: func
        Body:
            While (a < 5) && (j>6) || (k==7) Do
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_while_statement_24(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Body:
            While (a < 5) && (j>6) || (k==7) d
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = "Error on line 5 col 45: d"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_while_statement_25(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Body:
            While (a < 5) && (j>6) |||| (k==7) Do
            EndWhile.
        EndBody."""
        expect = "Error on line 5 col 37: ||"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_program_0(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a{2}
        Body:
            While (a <  - 5) && (j>6) |||| (k==7) Do
            EndWhile.
        EndBody."""
        expect = "Error on line 4 col 20: {"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_program_1(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a = 2;
        Body:
            While (a < 5) && (j>6) |||| (k==7) Do
            EndWhile.
        EndBody."""
        expect = "Error on line 4 col 21: ="
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_program_2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_program_3(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, x[3]
        Body:
            While (a < 5) && (j>6) || (k==7) Do
            EndWhile.

            While (a < 5) && (j>6) || k==7 Do
            EndWhile.

            If(((((((x == 3))))))) Then
                    x = y + z;
                    func(3) ;
                    x[y[z[y[t[a[z[a[e[f[q[a[s[a[3]]]]]]]]]]]]]];
            EndIf.
        EndBody."""
        expect = "Error on line 15 col 63: ;"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_program_4(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, x[3]
        Body:
            While (a < 5) && (j>6) || (k==7) Do
            EndWhile.

            While (a < 5) && j>6 || k==7 Do
            EndWhile.

            If(((((((x == 3))))))) Then
                    x = y + z;
                    func(3) ;
                    x[y[z[y[t[a[z[a[e[f[q[a[s[a[3]]]]]]]]]]]]]] = 3;
            EndIf.
        EndBody."""
        expect = "Error on line 9 col 37: =="
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_program_5(self):
        input = """
        Var: a[3] = {True,-2,- 3};
        Function: func
        Parameter: a, x[3]
        Body:
            While a < 5 && j>=6 || k==7 Do
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
        expect = "Error on line 6 col 28: >="
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_program_6(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, x[3]
        Body:
            While (True) && (False) || (True >= False) Do
            EndWhile.
            **
                    !@#$%^&*()_)
            **
            *
            If(((((((x == 3))))))) Then
                    x = y + z;
                    func(3) ;
            x[func(3) + 3] = 5;
            EndIf.
        EndBody."""
        expect = "Error on line 11 col 12: *"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_program_7(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    # def test_wrong_while_loop1(self):
        # """ Missing 'Do' word """
        # input = """
# Function: main
                    # Body:
                        # Var: a[5] = {1,2,3,4,5},i,j,done;
                        # done = False;
                        # i = -1;
                        # Do
                            # printLn(a[i]);
                            # While False Do
                                # doNothing();
                                # For (i = 0, i < 10, 1) Do
                                    # doNothing();
                                # EndFor.
                                # Do
                                    # doNothing();
                                # While False
                                # EndDo.
                            # EndWhile.
                            # i = i + 1;
                        # While ((i < 5) || !done)
                        # EndDo.
                    # EndBody.
            # """
        # expect = "Error on line 9 col 32: m"
        # self.assertTrue(TestParser.checkParser(input, expect, 10))
