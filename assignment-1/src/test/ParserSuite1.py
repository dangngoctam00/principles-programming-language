import unittest
from TestUtils import TestParser

class ParserSuite1(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_function(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_decl(self):
        """function"""
        input = """Var: a,b,c=func(r),abc[1][2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_decl_lack_of_semi(self):
        """function"""
        input = """Var: a,b,c=func(r),abc[1][2]"""
        expect = "Error on line 1 col 28: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_commnent_unclosed(self):
        """function"""
        input = """**this is unclosed comment"""
        expect = ""
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_assign_with_array(self):
        input = """Var: a = b[123];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_decl_comment_func(self):
        input = """
        **this is comment**
        Var: a = b[123];
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
                EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_while_nested(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) Do
                Var: j = 0;
                While (j % 5 == 2) Do
                    a[i] = b +. 1.0;
                    j = j + 1;
                EndWhile.
            EndWhile.
        EndBody."""
        expect = "Error on line 7 col 16: Var"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_if(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            If a > 10 Then
                a = 2;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_if_cond(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            If !(a > 10) Then
                a = 2;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_if_else(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            If a > 10 Then
                a = 2;
            Else 
                a = 3;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    
    def test_if_elseif_else(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            If a > 10 Then
                a = 2;
            ElseIf b < 10 Then
                a = 15;
            Else 
                a = 3;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_if_elseifs_else(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            If a > 10 Then
                a = 2;
            ElseIf b < 10 Then
                a = 15;
            ElseIf b < 10 Then
                a = 15;
            ElseIf b < 10 Then
                a = 15;
            Else 
                a = 3;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    
    def test_if_nested(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            If a > 10 Then
                If a > 10 Then
                    a = 2;
                ElseIf b < 10 Then
                    a = 15;
                ElseIf b < 10 Then
                    a = 15;
                ElseIf b < 10 Then
                    a = 15;
                Else 
                    a = 3;
                EndIf.
            ElseIf b < 10 Then
                If a > 10 Then
                    a = 2;
                Else 
                    a = 3;
                EndIf.
            ElseIf b < 10 Then
                If a > 10 Then
                    a = 2;
                ElseIf b < 10 Then
                    a = 15;
                ElseIf b < 10 Then
                    a = 15;
                ElseIf b < 10 Then
                    a = 15;
                EndIf.
            ElseIf abc > 345 Then
                If (foo(a[a_A[456]],b) == 3) Then a = a - e; EndIf.
            ElseIf b < 10 Then
                a = 15;
            Else 
                a = 3;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_for(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            For (i = 10, i >= 0, -1) Do
                a = a + b;
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    
    def test_for_nested(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0,j, a[3] = {1,2,3};
            For (i = 10, i >= 0, -1) Do
                For (j = 0, j < 3, 1) Do
                    a[j] = j*i;
                EndFor.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    
    
    
    def test_for_nested_while_wrong(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0,j, a[3] = {1,2,3};
            For (i = 10, i >= 0, -1) Do
                While (j % 5 == 2) Do
                    a[i] = b +. 1.0;
                    j = j + 1;
            EndFor.EndWhile.
        EndBody."""
        expect = "Error on line 10 col 12: EndFor"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    
    def test_invalid_decl_arr(self):
        input = """Var: a[]"""
        expect = "Error on line 1 col 7: ]"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    
    def test_assign(self):
        input = """
        Function: foo
        Body:
            5 = 6;
        EndBody."""
        expect = "Error on line 4 col 12: 5"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    

    def test_assign_1(self):
        input = """
        Function: foo
        Body:
            a = 6
        EndBody."""
        expect = "Error on line 5 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_assign_2(self):
        input = """
        Function: foo
        Body:
            a = 6;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_assign_3(self):
        input = """
        Function: foo
        Body:
            a + 3 = 5;
        EndBody."""
        expect = "Error on line 4 col 14: +"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    
    def test_while_break(self):
        input = """
        Function: foo
        Body:
            While (x+y > x-y) Do
                If (x*y % 2) Then
                    Break;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_wrong_decl_pos(self):
        input = """
        Function: foo
        Body:
            While (x+y > x-y) Do
                If (x*y % 2) Then
                    Break;
                EndIf.
            EndWhile.
            Var: abc = 13;
        EndBody."""
        expect = "Error on line 9 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_for_break(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0,j, a[3] = {1,2,3};
            For (i = 10, i >= 0, -1) Do
                For (j = 0, j < 3, 1) Do
                    If (i==j) Then Break; EndIf.
                    a[j] = j*i;
                EndFor.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_while_continue(self):
        input = """
        Function: foo
        Body:
            While (x+y > x-y) Do
                If (x*y % 2) Then
                    Continue;
                EndIf.
                x = x+1;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))


    def test_for_continue(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0,j, a[3] = {1,2,3};
            For (i = 10, i >= 0, -1) Do
                For (j = 0, j < 3, 1) Do
                    If (i==j) Then Continue; EndIf.
                    a[j] = j*i;
                EndFor.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_do_while(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0,j, a[3] = {1,2,3};
            Do
                For (j = 0, j < 3, 1) Do
                    If (i==j) Then Continue; EndIf.
                    a[j] = j*i;
                EndFor.
                i= i+1;
            While i<10 EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    
    def test_do_nested_while(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0,j, a[3] = {1,2,3};
            Do
                While (x+y > x-y) Do
                    If (x*y % 2) Then
                        Continue;
                    EndIf.
                    x = x+1;
                EndWhile.
                i= i+1;
            While i<10 EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_program_1(self):
        input = """
        Var: x,a=6,arr[3][4] = {1,2,3,4};
        Function: add
        Parameter: a, b
        Body:
            Return a+b;
        EndBody.
        Function: checkNeg
        Parameter: a
        Body:
            Return a<0 || a<.0;
        EndBody."""
        expect = "Error on line 11 col 27: <."
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_program_2(self):
        input = """
        Var: x,a=6,arr[3][4] = {1,2,3,4};
        Function: add
        Parameter: a, b
        Body:
            Return a+b;
        EndBody.
        Function: checkNeg
        Parameter: a
        Body:
            Return (a<0) || (a<.0);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    
    def test_func_one_decl(self):
        input = """
        Var: x,a=6,arr[3][4] = {1,2,3,4};
        Function: add
        Parameter: a, b
        Body:
            Var: a = 1;
        EndBody.
        Function: checkNeg
        Parameter: a
        Body:
            Return (a<0) || (a<.0);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    
    def test_func_no_stmt(self):
        input = """
        Var: x,a=6,arr[3][4] = {1,2,3,4};
        Function: add
        Parameter: a, b
        Body:
        EndBody.
        Function: checkNeg
        Parameter: a
        Body:
            Return (a<0) || (a<.0);
        EndBody."""
        expect = "Error on line 6 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    
    def test_235(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_for_nested_while(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0,j, a[3] = {1,2,3};
            For (i = 10, i >= 0, -1) Do
                While (j % 5 == 2) Do
                    a[i] = b +. 1.0;
                    j = j + 1;
                EndWhile.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_237(self):
        """ test while """
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
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_238(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
                EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    
    def test_239(self):
        input = """
        Var: a = {1,2,3};
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
                EndWhile.
        EndBody."""
        expect = "Error on line 2 col 17: {"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    
    def test_240(self):
        input = """
        Var: a[3] = {1,2,3};
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While i < 5 && j>6 || k==7 Do
                a[i] = b +. 1.0;
                i = i + 1;
                EndWhile.
        EndBody."""
        expect = "Error on line 7 col 28: >"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    
    def test_241(self):
        input = """
        Var: a[3] = {a,2,3};
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While i < 5 && j>6 || k==7 Do
                a[i] = b +. 1.0;
                i = i + 1;
                EndWhile.
        EndBody."""
        expect = "Error on line 2 col 21: a"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_242(self):
        input = """
        Var: a[3] = {2+3,2,3};
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While i < 5 && j>6 || k==7 Do
                a[i] = b +. 1.0;
                i = i + 1;
                EndWhile.
        EndBody."""
        expect = "Error on line 2 col 22: +"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_243(self):
        input = """
        Var: a[3] = {a[4],2,3};
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While i < 5 && j>6 || k==7 Do
                a[i] = b +. 1.0;
                i = i + 1;
                EndWhile.
        EndBody."""
        expect = "Error on line 2 col 21: a"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_244(self):
        input = """
        Var: a[3] = {func(abc),2,3};
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While i < 5 && j>6 || k==7 Do
                a[i] = b +. 1.0;
                i = i + 1;
                EndWhile.
        EndBody."""
        expect = "Error on line 2 col 21: func"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_245(self):
        input = """
        Var: a[3] = {{1,2},{2,3}};
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i + 1;
                EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_246(self):
        input = """
        Var: a[3] = {23,2,3};
        Function: 123
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = "Error on line 3 col 18: 123"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_247(self):
        input = """
        Var: a[3] = {23,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i + 1 + a + b + c + d;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_248(self):
        input = """
        Var: a[3] = {23,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - 1 + a -. b - c - -.d;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_249(self):
        input = """
        Var: a[3] = {23,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_250(self):
        input = """
        Var: a[3] = {23,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))


    def test_251(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_252(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return 1;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    

    def test_253(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return 1+3;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_254(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return !( True && abc || func(a) ) || !!!((a>b) || (a<c));
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_255(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return a[1];
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_256(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return {"abc","123"};
        EndBody."""
        expect = "Error on line 11 col 19: {"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_257(self):
        input = """
        Var: a[3] = {{"abc","123"},2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_258(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return 1;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_259(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_260(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    # def test_function(self):
    #     """function"""
    #     input = """
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #             EndWhile.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    
    
    
