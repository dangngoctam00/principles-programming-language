import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    # def test_dump_401(self):
        
    #     input = """                                    
    #                 Function: main
    #                     Parameter: x[1][1]
    #                     Body:                            
    #                         x = {{1.1}};
    #                         x = y;
    #                         Return x;
    #                     EndBody.    
    #             """
    #     expect = str("Undeclared Identifier: y")
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_dump_402(self):        
    #     input = """    
    #                 Function: foo
    #                     Parameter: x[1][1], y
    #                     Body:      
    #                         Var: z;                                                                              
    #                         z = main(z);
    #                     EndBody.   

    #                 Function: main
    #                     Parameter: x
    #                     Body:                            
    #                         Return x;
    #                     EndBody.    
    #             """
    #     expect = str("Type Cannot Be Inferred: Assign(Id(z),CallExpr(Id(main),[Id(z)]))")
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_dump_403(self):
        
    #     input = """    
    #                 Function: foo                        
    #                     Body:      
    #                         Var: z, x, y[1][1];                                                                              
    #                         z = x + y[1][1];
    #                     EndBody.   

    #                 Function: main                        
    #                     Body:           
    #                         Var: x = 1;                 
    #                         Return x;
    #                     EndBody.    
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_dump_404(self):
        
    #     input = """    
    #                 Function: foo                        
    #                     Body:      
    #                         Var: z, x, y[1][1] = {{1}};                                                                              
    #                         z = -.y[1][1];
    #                     EndBody.   

    #                 Function: main                        
    #                     Body:           
    #                         Var: x = 1;                 
    #                         Return x;
    #                     EndBody.    
    #             """
    #     expect = str("Type Mismatch In Expression: UnaryOp(-.,ArrayCell(Id(y),[IntLiteral(1),IntLiteral(1)]))")
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_dump_405(self):
        
    #     input = """    
    #                 Function: foo                        
    #                     Body:      
    #                         Var: z, x, y[1][1] = {{1}};                                                                              
    #                         main();
    #                     EndBody.   

    #                 Function: main                        
    #                     Body:           
    #                         Var: x = 1;                 
    #                         Return;
    #                     EndBody.    
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,405))
    

    # def test_406(self):
        
    #     input = """Function: main
    #                Body: 
    #                     foo();
    #                EndBody."""
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,406))

    # def test_407(self):
    #     """Complex program"""
    #     input = """Function: main  
    #                Body:
    #                     printStrLn();
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,407))
    
    # def test_408(self):
    #     """More complex program"""
    #     input = """Function: main 
    #                 Body:
    #                     printStrLn(read(4));
    #                 EndBody."""
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_409(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"),[],([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,409))

    # def test_410(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[
    #                     CallExpr(Id("read"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_411(self):
    #     """Complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,411))
    
    # def test_dump_412(self):
        
    #     input = """
    #         Function: main
    #         Parameter: a, c, d
    #         Body:                
    #             If a Then d = 10;
    #             ElseIf c == 6 Then d = 12;
    #             EndIf.
    #         EndBody.
    #     """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,412))

    # def test_dump_413(self):
        
    #     input = """
    #         Function: main 
    #             Parameter: n,a[3], b[2][3], c[1]
    #             Body:
    #                 a = {1,2,3}; 
    #                 b[2][3] = 5;
    #                 c[2] = {{1,3, 2},{1,5,7}};
    #                 Return;
    #             EndBody.
    #     """
    #     expect = str("Type Mismatch In Statement: Assign(ArrayCell(Id(c),[IntLiteral(2)]),ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(3),IntLiteral(2)),ArrayLiteral(IntLiteral(1),IntLiteral(5),IntLiteral(7))))")
    #     self.assertTrue(TestChecker.test(input,expect,413))


    # def test_414(self):        
    #     input = """    
    #                 Function: foo
    #                     Parameter: x[1][1], y
    #                     Body:      
    #                         Var: z;                                                                              
    #                         x = main(z);
    #                     EndBody.   

    #                 Function: main
    #                     Parameter: x
    #                     Body:                            
    #                         Return x;
    #                     EndBody.    
    #             """
    #     expect = str("Type Cannot Be Inferred: Assign(Id(x),CallExpr(Id(main),[Id(z)]))")        
    #     self.assertTrue(TestChecker.test(input,expect,414))

    # def test_415(self):        
    #     input = """    
    #                 Function: foo
    #                     Parameter: x[1][1], y
    #                     Body:      
    #                         Var: z = 1;                                                                              
    #                         x = main(z);
    #                     EndBody.   

    #                 Function: main
    #                     Parameter: x
    #                     Body:                            
    #                         Return x;
    #                     EndBody.    
    #             """
    #     expect = str("Type Cannot Be Inferred: Assign(Id(x),CallExpr(Id(main),[Id(z)]))")
    #     self.assertTrue(TestChecker.test(input,expect,415))
    
    # def test_416(self):    
    #     input = """    
    #                 Function: foo
    #                     Parameter: x[1][1], y
    #                     Body:      
    #                         Var: z = 1;                                                                              
    #                         x = main(z);
    #                     EndBody.   

    #                 Function: main
    #                     Parameter: x
    #                     Body:        
    #                         Var: z[1][1] = {{1}};                   
    #                         Return z;
    #                     EndBody.    
    #             """
    #     expect = str("Type Cannot Be Inferred: Assign(Id(x),CallExpr(Id(main),[Id(z)]))")
    #     self.assertTrue(TestChecker.test(input,expect,416))

    # def test_417(self):
    #     input = """    
    #                 Function: foo
    #                     Parameter: x[1][1], y
    #                     Body:      
    #                         Var: x = 1.2;
    #                         Var: z = 1;                                                                              
    #                         x = main(z);
    #                     EndBody.   

    #                 Function: main
    #                     Parameter: x
    #                     Body:        
    #                         Var: z[1][1] = {{1}};                   
    #                         Return z;
    #                     EndBody.    
    #             """
    #     expect = str("Redeclared Variable: x")
    #     self.assertTrue(TestChecker.test(input,expect,417))

    # def test_418(self):
    #     input = """    
    #                 Function: foo
    #                     Parameter: x[1][1], y
    #                     Body:                                 
    #                         x = {{1}};
    #                         Return x;
    #                     EndBody.   

    #                 Function: main
    #                     Parameter: x, z
    #                     Body:        
    #                         Var: t[1][1] = {{1}};                 
    #                         Return t;
    #                     EndBody.    
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,418))

    # #**
    # def test_419(self):
    #     input = """    
    #                 Function: foo
    #                     Parameter: x[1][1], y
    #                     Body:     
    #                         y = 1;                            
    #                         main(y)[1][1] = 2;
    #                         Return x;
    #                     EndBody.   

    #                 Function: main
    #                     Parameter: x
    #                     Body:        
    #                         Var: t[1][1] = {{1}};                 
    #                         Return t;
    #                     EndBody.    
    #             """
    #     expect = str("Type Cannot Be Inferred: Assign(ArrayCell(CallExpr(Id(main),[Id(y)]),[IntLiteral(1),IntLiteral(1)]),IntLiteral(2))")
    #     self.assertTrue(TestChecker.test(input,expect,419))



    # def test_420(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x
    #                     Body:        
    #                         If x Then
    #                             Var: y = 1;
    #                         ElseIf y Then
    #                         EndIf.
    #                         Return t;
    #                     EndBody.    
    #             """
    #     expect = str("Undeclared Identifier: y")
    #     self.assertTrue(TestChecker.test(input,expect,420))

    # def test_421(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x
    #                     Body:        
    #                         If x Then
    #                             Var: y = 1, x = "\\n\\tHello";
    #                         ElseIf x > 1 Then
    #                         EndIf.
    #                         Return x;
    #                     EndBody.    
    #             """
    #     expect = str("Type Mismatch In Expression: BinaryOp(>,Id(x),IntLiteral(1))")
    #     self.assertTrue(TestChecker.test(input,expect,421))
    
    # def test_422(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x
    #                     Body:        
    #                         If x == 1 Then
    #                             Var: y = 1, x = "\\n\\tHello";
    #                             Var: z = True;
    #                         ElseIf x > 1 Then
    #                             Var: x = 5;
    #                             z = False;
    #                         EndIf.
    #                         Return x;
    #                     EndBody.    
    #             """
    #     expect = str("Undeclared Identifier: z")
    #     self.assertTrue(TestChecker.test(input,expect,422))

    # def test_423(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x
    #                     Body:        
    #                         Return 1;  
    #                     EndBody.   

    #                 Function: foo
    #                     Parameter: z[2][2]
    #                     Body:
    #                         Var: r_type = 1;
    #                         main(r_type);
    #                         Return;
    #                     EndBody. 
    #             """
    #     expect = str("Type Mismatch In Statement: CallStmt(Id(main),[Id(r_type)])")
    #     self.assertTrue(TestChecker.test(input,expect,423))

    # def test_424(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x
    #                     Body:        
    #                         Return 1;  
    #                     EndBody.   

    #                 Function: foo
    #                     Parameter: z[2][2]
    #                     Body:
    #                         Var: r_type = 1, y;
    #                         r_type = main(r_type);
    #                         y = r_type + main(r_type) + 1;
    #                         Return;
    #                     EndBody. 
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,424))        
    
    # def test_425(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z                        
    #                     Body:        
    #                         y = x || (x > z);
    #                         Return x;
    #                     EndBody.                       
    #             """
    #     expect = str("Type Mismatch In Expression: BinaryOp(>,Id(x),Id(z))")
    #     self.assertTrue(TestChecker.test(input,expect,425))

    # def test_426(self):
    #     input = """                        
    #                 Var: a = 5, f;
    #                 Function: main
    #                 Body:
    #                     Var: r = 10, v = "45", d;
    #                     d = float_of_string(v);
    #                     f = (r != !d) ;
    #                     d = string_of_bool(f);
    #                 EndBody.                    
    #             """
    #     expect = str("Type Mismatch In Expression: UnaryOp(!,Id(d))")
    #     self.assertTrue(TestChecker.test(input,expect,426))


    # def test_427(self):
    #     input = """                        
    #                 Var: a = 5, f;
    #                 Function: main
    #                 Body:
    #                     Var: r = 10., v = "45", d;
    #                     d = printLn();                                            
    #                     d = string_of_bool(f);
    #                 EndBody.                    
    #             """
    #     expect = str("Type Mismatch In Statement: Assign(Id(d),CallExpr(Id(printLn),[]))")
    #     self.assertTrue(TestChecker.test(input,expect,427))

    # def test_428(self):
    #     input = """                        
    #                 Var: a = 5, f;
    #                 Function: main
    #                 Body:
    #                     Var: r = 10., v = "45", d;
    #                     printLn();
    #                     v = read();                                            
    #                     d = string_of_bool(f);
    #                 EndBody.                    
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,428))

    # def test_429(self):
    #     input = """                        
    #                 Var: a = 5, f;
    #                 Function: main
    #                 Body:
    #                     Var: r = 10., v = "45", d;
    #                     printLn();
    #                     v = read(); 
    #                     printStr(5);                                           
    #                     d = string_of_bool(f);
    #                 EndBody.                    
    #             """
    #     expect = str("Type Mismatch In Statement: CallStmt(Id(printStr),[IntLiteral(5)])")
    #     self.assertTrue(TestChecker.test(input,expect,429))

    # def test_430(self):
    #     input = """                        
    #                 Var: a = 5, f;
    #                 Function: main
    #                 Body:
    #                     Var: r = 10., v = "45", d;
    #                     printLn();
    #                     v = read(); 
    #                     printStr("\\b\\f");
    #                     printStrLn();
    #                     f = float_of_string("\\n\\f**hello");                                   
    #                     d = string_of_bool(f);
    #                 EndBody.                    
    #             """
    #     expect = str("Type Mismatch In Statement: CallStmt(Id(printStrLn),[])")
    #     self.assertTrue(TestChecker.test(input,expect,430))  
    
                        

    # def test_431(self):
    #     input = """                        
    #                 Var: a = 5, f;
    #                 Function: main
    #                 Body:
    #                     Var: r = 10., v = "45", d;
    #                     printLn();
    #                     v = read(); 
    #                     printStr("\\b\\f");
    #                     printStrLn("\\n\\f\\b132");  
    #                     f = bool_of_string("\\n\\f**hello");                                   
    #                     d = string_of_bool(f);
    #                 EndBody.                    
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,431))    
    


    # def test_432(self):
    #     input = """                        
    #                 Var: a = 5, f;
    #                 Function: main
    #                 Body:
    #                     Var: r = 10., v = "45", d, g, h;
    #                     printLn();
    #                     v = read(); 
    #                     printStr("\\b\\f");
    #                     printStrLn("\\n\\f\\b132");  
    #                     f = bool_of_string("\\n\\f**hello");                                   
    #                     d = string_of_bool(f);
    #                     g = int_of_string(d);
    #                     h = float_to_int(g);
    #                 EndBody.                    
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,432))    


    # def test_433(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x
    #                     Body:        
    #                         Var: t[1][1] = {{1}};                 
    #                         Return t;
    #                     EndBody.    

    #                 Function: foo
    #                     Parameter: x[1][1], y
    #                     Body:     
    #                         y = 1;                            
    #                         main(y)[1][1] = 1.2;
    #                         Return x;
    #                     EndBody.   
    #             """
    #     expect = str("Type Mismatch In Statement: Assign(ArrayCell(CallExpr(Id(main),[Id(y)]),[IntLiteral(1),IntLiteral(1)]),FloatLiteral(1.2))")
    #     self.assertTrue(TestChecker.test(input,expect,433))
    

    # def test_434(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x
    #                     Body:        
    #                         Var: t[1][1] = {{1}}, y;                            
    #                         y = printStrLn("\\f\\'\\r\\b\\n\\\\");
    #                         Return t;
    #                     EndBody.    
    #             """
    #     expect = str("Type Mismatch In Statement: Assign(Id(y),CallExpr(Id(printStrLn),[StringLiteral(\\f\\'\\r\\b\\n\\\\)]))")
    #     self.assertTrue(TestChecker.test(input,expect,434))

    
    # def test_435(self):
    #     input = """                        
    #                 Var: x;
    #                 Function: main
    #                 Body:
    #                     Var: a, b, c;
    #                     x  = 3;
    #                     If bool_of_string("True") Then
    #                         a = int_of_string (b);
    #                         c = float_to_int (a) +. 2.0;
    #                     EndIf.
    #                     c = doo(a);
    #                 EndBody.

    #                 Function: doo
    #                 Parameter: a
    #                 Body:
    #                     a = "\\n\\'";
    #                     Return 2;
    #                 EndBody.   
    #             """
    #     expect = str("Type Mismatch In Statement: Assign(Id(a),StringLiteral(\\n\\'))")
    #     self.assertTrue(TestChecker.test(input,expect,435))

    # def test_436(self):
    #     input = """                        
    #                 Var: x, y, g;
    #                 Function: main
    #                 Body:
    #                     Var: a, b, c;
    #                     x  = True;
    #                     y = 1;
    #                     If bool_of_string("True") Then
    #                         a = int_of_string(b);
    #                         c = float_to_int(a) +. 2.0 -. 1.2;
    #                     ElseIf x Then
    #                         printLn();
    #                     ElseIf y > 2 Then
    #                         Var: g;
    #                         g = string_of_int(2);
    #                     ElseIf y Then
    #                     Else
    #                     EndIf.                    
    #                 EndBody.

    #                 Function: doo
    #                 Parameter: a
    #                 Body:
    #                     a = "\\n\\'";
    #                     Return 2;
    #                 EndBody.   
    #             """
    #     expect = str("Type Mismatch In Statement: If(CallExpr(Id(bool_of_string),[StringLiteral(True)]),[],[Assign(Id(a),CallExpr(Id(int_of_string),[Id(b)])),Assign(Id(c),BinaryOp(-.,BinaryOp(+.,CallExpr(Id(float_to_int),[Id(a)]),FloatLiteral(2.0)),FloatLiteral(1.2)))])ElseIf(Id(x),[],[CallStmt(Id(printLn),[])])ElseIf(BinaryOp(>,Id(y),IntLiteral(2)),[VarDecl(Id(g))],[Assign(Id(g),CallExpr(Id(string_of_int),[IntLiteral(2)]))])ElseIf(Id(y),[],[])Else([],[])")
    #     self.assertTrue(TestChecker.test(input,expect,436))

    # def test_437(self):
    #     input = """                        
    #                 Var: x, y, g;
    #                 Function: main
    #                 Body:
    #                     Var: a, b, c;
    #                     x  = True;
    #                     y = 1;
    #                     If bool_of_string("True") Then
    #                         Var: y[5];
    #                         y = {1.2, 1.1, 2.1, 1.2, 1.1};                           
    #                     ElseIf x Then
    #                         Var: y[5];
    #                         y = {1.2, 1.1, 2.1, 1.2, 1.1};   
    #                     ElseIf y > 2 Then
    #                         Var: y[5];
    #                         y = {1.2, 1.1, 2.1, 1.2, 1.1};   
    #                     ElseIf y > int_of_string("\\n") Then
    #                     Else
    #                     EndIf.                    
    #                 EndBody.                    
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,437))

    # def test_438(self):
    #     input = """                        
    #                 Var: x, y, g;
    #                 Function: main
    #                 Body:
    #                     Var: a, b, c;
    #                     x  = True;
    #                     y = 1;
    #                     If bool_of_string("True") || (y > 0) && (float_to_int(y) <. float_of_string("")) Then
    #                         Var: y[5];
    #                         y = {1.2, 1.1, 2.1, 1.2, 1.1};                           
    #                     ElseIf x Then
    #                         Var: y[5];
    #                         y = {1.2, 1.1, 2.1, 1.2, 1.1};   
    #                     ElseIf y > 2 Then
    #                         Var: y[5];
    #                         y = {1.2, 1.1, 2.1, 1.2, 1.1};   
    #                     ElseIf y > int_of_string("\\n") Then
    #                     Else
    #                     EndIf.                    
    #                 EndBody.                    
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,438))

    # def test_439(self):
    #     input = """                        
    #                 Var: x, y, g, k;
    #                 Function: main
    #                 Body:
    #                     Var: a, b, c;
    #                     x  = True;
    #                     y = 1;
    #                     If bool_of_string("True") || (y > 0) && (float_to_int(y) <. float_of_string("")) Then
    #                         Var: y;
    #                         y = 1.2;
    #                         g = string_of_bool(x);
    #                         k = int_of_float(float_to_int(int_of_float(y)) *. 1.2 -. 3.0);
    #                     Else
    #                     EndIf.                    
    #                 EndBody.                    
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,439))


    # def test_440(self):        
    #     input = """    
    #                 Function: foo
    #                     Parameter: x[1][1]
    #                     Body:      
    #                         Var: z = 1, y = 1.2;                                                                              
    #                         z = main(z, True, {{"\\n"}});
    #                         z = main(12, False, {{"\\f\\'"}});
    #                     EndBody.   

    #                 Function: main
    #                     Parameter: x, y, z[1][1]
    #                     Body:                            
    #                         Return x;
    #                     EndBody.    
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,440))

    # def test_441(self):        
    #     input = """    
    #                 Function: foo
    #                     Parameter: x[1][1]
    #                     Body:      
    #                         Var: z = 1, y = 1.2;                                                                              
    #                         z = main(z, True, {{"\\n"}});
    #                         y = main(12, False, {{"\\f\\'"}});
    #                     EndBody.   

    #                 Function: main
    #                     Parameter: x, y, z[1][1]
    #                     Body:                            
    #                         Return x;
    #                     EndBody.    
    #             """
    #     expect = str("Type Mismatch In Statement: Assign(Id(y),CallExpr(Id(main),[IntLiteral(12),BooleanLiteral(false),ArrayLiteral(ArrayLiteral(StringLiteral(\\f\\')))]))")
    #     self.assertTrue(TestChecker.test(input,expect,441))

    # def test_442(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: foo
    #                     Parameter: x[1][1]
    #                     Body:      
    #                         For (a = 3 + int_of_string("\\'"), False , 1) Do
    #                         EndFor.
    #                         Return;
    #                     EndBody.   

    #                 Function: main
    #                     Parameter: x, y, z[1][1]
    #                     Body:                            
    #                         Return;
    #                     EndBody.    
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,442))

    
    # def test_443(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x[1][1]
    #                     Body:      
    #                         For (a = int_of_float(float_to_int(int_of_string("2"))) + int_of_string("\\'"), False , 3 + 5 * 2 - 4) Do
    #                         EndFor.
    #                         Return;
    #                     EndBody.   
                   
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,443))

    # def test_444(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x[1][1], z
    #                     Body:      
    #                         z = 1;
    #                         For (a = int_of_float(float_to_int(int_of_string("2"))) + int_of_string("\\'"), z , 3 + 5 * 2 - 4) Do
    #                         EndFor.
    #                         Return;
    #                     EndBody.   
                   
    #             """
    #     expect = str("Type Mismatch In Statement: For(Id(a),BinaryOp(+,CallExpr(Id(int_of_float),[CallExpr(Id(float_to_int),[CallExpr(Id(int_of_string),[StringLiteral(2)])])]),CallExpr(Id(int_of_string),[StringLiteral(\\')])),Id(z),BinaryOp(-,BinaryOp(+,IntLiteral(3),BinaryOp(*,IntLiteral(5),IntLiteral(2))),IntLiteral(4)),[],[])")
    #     self.assertTrue(TestChecker.test(input,expect,444))

    # def test_445(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x[1][1], z
    #                     Body:      
    #                         z = 1;
    #                         For (a = int_of_float(float_to_int(int_of_string("2"))) + int_of_string("\\'"), True , 3 + 5 * 2 - 4 \\3) Do
    #                             Var: z[1][2], x;
    #                             z = {{True, False}};
    #                             x = z[0][0];
    #                         EndFor.
    #                         Return;
    #                     EndBody.   
                   
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,445))

    # def test_446(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x, z
    #                     Body:
    #                         Var: y;      
    #                         z = 1;
    #                         For (a = int_of_float(float_to_int(int_of_string("2"))) + int_of_string("\\'"), True , 3 + 5 * 2 - 4 \\3) Do
    #                             Var: z[1][2], x;
    #                             z = {{True, False}};
    #                             x = z[0][0];
    #                             Break;
    #                             Continue;
    #                         EndFor.
                            
    #                         If x == 0xAF Then
    #                             If y == "'\"\\n\\b\\\\" Then
    #                                 Do 
    #                                     x = x + 3;
    #                                 While x >= 0o17 EndDo.
    #                             EndIf.
    #                         EndIf.
    #                         Return;
    #                     EndBody.   
                   
    #             """
    #     expect = str("Type Mismatch In Expression: BinaryOp(==,Id(y),StringLiteral('\"\\n\\b\\\\))")
    #     self.assertTrue(TestChecker.test(input,expect,446))

    # def test_447(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x, z
    #                     Body:
    #                         Var: y;      
    #                         z = 1;
    #                         For (a = int_of_float(float_to_int(int_of_string("2"))) + int_of_string("\\'"), True , 3 + 5 * 2 - 4 \\3) Do
    #                             Var: z[1][2], x;
    #                             z = {{True, False}};
    #                             x = z[0][0];
    #                             Break;
    #                             Continue;
    #                         EndFor.
                            
    #                         If x == 0xAF Then
    #                             If y == 1 Then
    #                                 Do 
    #                                     Var: x;
    #                                     x = x +. 3.2;
    #                                 While x >= 0o17 EndDo.
    #                             EndIf.
    #                         EndIf.
    #                         Return;
    #                     EndBody.   
                   
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,447))

    # def test_448(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x, z
    #                     Body:
    #                         Var: y;      
    #                         z = 1;
    #                         For (a = int_of_float(float_to_int(int_of_string("2"))) + int_of_string("\\'"), True , 3 + 5 * 2 - 4 \\3) Do
    #                             Var: z[1][2], x;
    #                             z = {{True, False}};
    #                             x = z[0][0];
    #                             Break;
    #                             Continue;
    #                         EndFor.
                            
    #                         If x == 0xAF Then
    #                             If y == 1 Then
    #                                 Do 
    #                                     Var: x;
    #                                     x = x +. 3.2;
    #                                 While x + 0o17 EndDo.
    #                             EndIf.
    #                         EndIf.
    #                         Return;
    #                     EndBody.   
                   
    #             """
    #     expect = str("Type Mismatch In Statement: Dowhile([VarDecl(Id(x))],[Assign(Id(x),BinaryOp(+.,Id(x),FloatLiteral(3.2)))],BinaryOp(+,Id(x),IntLiteral(15)))")
    #     self.assertTrue(TestChecker.test(input,expect,448))

    # def test_dump_449(self):
    #     input = """                                    
    #                 Function: main
    #                     Parameter: x[1][1]
    #                     Body:                            
    #                         func();
    #                         Return;
    #                     EndBody.    
                    
    #                 Function: func                        
    #                     Body:         
    #                         Var: x[1][1];          
    #                         x = {{True}};                        
    #                         Return printStr("");
    #                     EndBody.    
    #             """
    #     expect = str("Type Mismatch In Statement: Return(CallExpr(Id(printStr),[StringLiteral()]))")
    #     self.assertTrue(TestChecker.test(input,expect,449))

    
    # def test_450(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x, z
    #                     Body:                                                                                   
    #                         Do 

    #                         While foo() EndDo.                                                    
    #                         Return;
    #                     EndBody.

    #                 Function: foo
    #                     Body:
    #                         Var: x;
    #                         Return x;                        
    #                     EndBody.   
                   
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,450))

    # def test_451(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x, z
    #                     Body:                                                                                   
    #                         Do 

    #                         While foo() EndDo.                                                    
    #                         Return;
    #                     EndBody.

    #                 Function: foo
    #                     Body:
    #                         Var: x[1][1];
    #                         Return x;                        
    #                     EndBody.   
                   
    #             """
    #     expect = str("Type Mismatch In Statement: Return(Id(x))")
    #     self.assertTrue(TestChecker.test(input,expect,451))

    # def test_452(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x, z
    #                     Body:    
    #                         x = True;                                                                               
    #                         Do 
    #                             Var: x, z;
    #                             x = 2;                            
    #                             printLn();
    #                             printStr(string_of_float(0.1E+4));
    #                         While foo() > int_of_string("hi ;)")  EndDo.                                                    
    #                         Return x;
    #                     EndBody.

    #                 Function: foo
    #                     Body:
    #                         Var: x = "1.2";
    #                         x = string_of_bool(main(True, 1));
    #                         Return int_of_string(x);                        
    #                     EndBody.   
                   
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,452))

    # def test_453(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x, z
    #                     Body:    
    #                         x = True;                                                                               
    #                         Do 
    #                             Var: x, z;
    #                             x = 2;                            
    #                             printLn();
    #                             printStr(string_of_float(0.1E+4));
    #                         While foo() > int_of_string("hi ;)")  EndDo.                                                    
    #                         Return x;
    #                     EndBody.

    #                 Function: foo
    #                     Body:
    #                         Var: x = "1.2";
    #                         x = string_of_bool(main(True, 1));
    #                         Return float_of_string(x);                        
    #                     EndBody.   
                   
    #             """
    #     expect = str("Type Mismatch In Statement: Return(CallExpr(Id(float_of_string),[Id(x)]))")
    #     self.assertTrue(TestChecker.test(input,expect,453))
    
    # def test_454(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x, z, y
    #                     Body:    
    #                         If x == 0X3FABCABDE Then
    #                             If y =/= float_of_string("12.2") Then
    #                                 Do                             
                                    
    #                                 While x != 0o10 EndDo.
    #                                 While z >=. 0.e-5 Do 
                                    
    #                                 EndWhile.                                    
                                    
    #                                 func();
    #                                 EndIf.
    #                         EndIf.
    #                     EndBody. 
    #                 Function: func                        
    #                     Body:

    #                     EndBody.                                      
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,454))

    # def test_455(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x, z, y
    #                     Body:    
    #                         If x == 0X3FABCABDE Then
    #                             If y =/= float_of_string("12.2") Then
    #                                 Do                             
                                    
    #                                 While x != 0o10 EndDo.
    #                                 While x + 12 Do 
                                    
    #                                 EndWhile.                                    
                                    
    #                                 func();
    #                                 EndIf.
    #                         EndIf.
    #                     EndBody. 
    #                 Function: func                        
    #                     Body:

    #                     EndBody.                                      
    #             """
    #     expect = str("Type Mismatch In Statement: While(BinaryOp(+,Id(x),IntLiteral(12)),[],[])")
    #     self.assertTrue(TestChecker.test(input,expect,455))

    # def test_456(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x, z, y
    #                     Body:    
    #                         If x == 0X3FABCABDE Then
    #                             If y =/= float_of_string("12.2") Then
    #                                 Do                             
                                    
    #                                 While x != 0o10 EndDo.
    #                                 While x > float_of_string("") Do 
                                    
    #                                 EndWhile.                                    
                                    
    #                                 func();
    #                                 EndIf.
    #                         EndIf.
    #                     EndBody. 
    #                 Function: func                        
    #                     Body:

    #                     EndBody.                                      
    #             """
    #     expect = str("Type Mismatch In Expression: BinaryOp(>,Id(x),CallExpr(Id(float_of_string),[StringLiteral()]))")
    #     self.assertTrue(TestChecker.test(input,expect,456))

    # def test_457(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x, z, y
    #                     Body:    
    #                         If x == 0X3FABCABDE Then
    #                             If y =/= float_of_string("12.2") Then
    #                                 Do                             
                                    
    #                                 While x != 0o10 EndDo.
    #                                 While x > int_of_string("") Do 
    #                                     While False Do
    #                                         Var: x;
    #                                         x = 0.1;
    #                                         While x =/= 1.2 Do
    #                                         EndWhile.
    #                                     EndWhile.
    #                                 EndWhile.                                                                                                            
    #                                 EndIf.
    #                         EndIf.
    #                     EndBody.                                                       
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,457))

    # def test_458(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x, z, y
    #                     Body:    
    #                         If x == 0X3FABCABDE Then
    #                             If y =/= float_of_string("12.2") Then
    #                                 Do                             
                                    
    #                                 While x != 0o10 EndDo.
    #                                 While x > int_of_string("") Do 
    #                                     While False Do
    #                                         Var: x;
    #                                         x = 0.1;
    #                                         While x =/= 1.2 Do
    #                                         EndWhile.
    #                                     EndWhile.
    #                                     x = float_of_string("");
    #                                 EndWhile.                                                                                                            
    #                                 EndIf.
    #                         EndIf.
    #                     EndBody.                                                       
    #             """
    #     expect = str("Type Mismatch In Statement: Assign(Id(x),CallExpr(Id(float_of_string),[StringLiteral()]))")
    #     self.assertTrue(TestChecker.test(input,expect,458))
    
    # def test_459(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: main
    #                     Parameter: x, z, y
    #                     Body:    
    #                         Do Do Do Do Do Do Do Do Do Do Do While x == int_of_string("")
    #                         EndDo. While x == int_of_string("")
    #                         EndDo. While x == int_of_string("")
    #                         EndDo. While x == int_of_string("")
    #                         EndDo. While x == int_of_string("")
    #                         EndDo. While x == int_of_string("")
    #                         EndDo. While x == int_of_string("")
    #                         EndDo. While x == int_of_string("")
    #                         EndDo. While x == int_of_string("")
    #                         EndDo. While x == int_of_string("")
    #                         EndDo. While x == int_of_string("")
    #                         EndDo.
    #                         Return;
    #                     EndBody.                                                       
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,459))

    # def test_460(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z                        
    #                     Body:        
    #                         y = x && (z || (int_of_float(1.2) > z));
    #                         Return x;
    #                     EndBody.                       
    #             """
    #     expect = str("Type Mismatch In Expression: BinaryOp(>,CallExpr(Id(int_of_float),[FloatLiteral(1.2)]),Id(z))")
    #     self.assertTrue(TestChecker.test(input,expect,460))
    
    # def test_461(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z                        
    #                     Body:        
    #                         y = x == (x + (x * int_of_float(1.2)));
    #                         Return x;
    #                     EndBody.                       
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,461))
    
    # def test_462(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z                        
    #                     Body:        
    #                         y = x == (y - ( x + (x * (int_of_float(1.2) + y))));
    #                         Return x;
    #                     EndBody.                       
    #             """
    #     expect = str("Type Mismatch In Statement: Assign(Id(y),BinaryOp(==,Id(x),BinaryOp(-,Id(y),BinaryOp(+,Id(x),BinaryOp(*,Id(x),BinaryOp(+,CallExpr(Id(int_of_float),[FloatLiteral(1.2)]),Id(y)))))))")
    #     self.assertTrue(TestChecker.test(input,expect,462))
    
    # def test_463(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z                        
    #                     Body:        
    #                         y = x \\ (y - ( x + (x * (int_of_float(1.2) + y))));
    #                         Return x;
    #                     EndBody.                       
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,463))
    
    # def test_464(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z                        
    #                     Body:        
    #                         x = x > y;
    #                         Return;
    #                     EndBody.                       
    #             """
    #     expect = str("Type Mismatch In Statement: Assign(Id(x),BinaryOp(>,Id(x),Id(y)))")
    #     self.assertTrue(TestChecker.test(input,expect,464))

    # def test_465(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z                        
    #                     Body:        
    #                         x = x > y;
    #                         Return;
    #                     EndBody.                       
    #             """
    #     expect = str("Type Mismatch In Statement: Assign(Id(x),BinaryOp(>,Id(x),Id(y)))")
    #     self.assertTrue(TestChecker.test(input,expect,465))

    # def test_466(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z, t                    
    #                     Body:        
    #                         z = x > y;
    #                         t = !bool_of_string("True");
    #                         t = !t; 
    #                         Return;
    #                     EndBody.                       
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,466))
    
    # def test_467(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z, t                    
    #                     Body:
    #                         Var: k[1][1][1][1][1];        
    #                         z = x > y;
    #                         t = !bool_of_string("True");
    #                         t = !t; 
    #                         z = t;
    #                         t = z;
    #                         k[1][1][1][1][1] = t;
    #                         Return;
    #                     EndBody.                       
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,467))

    
    # def test_468(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z, t                    
    #                     Body:
    #                         Var: k[1][1][1][1][1];        
    #                         z = x > y;
    #                         t = !bool_of_string("True");
    #                         t = !t; 
    #                         z = t;
    #                         t = z;
    #                         foo(1 != 2,1 == 1,z || False,z && !bool_of_string("False"));
    #                         Return;
    #                     EndBody. 
    #                 Function: foo
    #                     Parameter: x, y, z, t
    #                     Body:
    #                         Return;
    #                     EndBody.                      
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,468))

    # def test_469(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z, t                    
    #                     Body:
    #                         Var: k[1][1][1][1][1];        
    #                         z = x > y;
    #                         t = !bool_of_string("True");
    #                         t = !t; 
    #                         z = t;
    #                         t = z;
    #                         foo(1 != 2,z == 1,z || False,z && !bool_of_string("False"));
    #                         Return;
    #                     EndBody. 
    #                 Function: foo
    #                     Parameter: x, y, z, t
    #                     Body:
    #                         Return;
    #                     EndBody.                      
    #             """
    #     expect = str("Type Mismatch In Expression: BinaryOp(==,Id(z),IntLiteral(1))")
    #     self.assertTrue(TestChecker.test(input,expect,469))

    # def test_470(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z, t                    
    #                     Body:
    #                         Var: k[1][1][1][1][1], g;        
    #                         z = x > y;
    #                         t = !bool_of_string("True");
    #                         t = !t; 
    #                         z = t;
    #                         t = z;
    #                         foo(g,int_of_float(float_to_int(1)) == 1,z || False,z && !bool_of_string("False"));
    #                         Return;
    #                     EndBody. 
    #                 Function: foo
    #                     Parameter: x, y, z, t
    #                     Body:
    #                         Return;
    #                     EndBody.                      
    #             """
    #     expect = str("Type Cannot Be Inferred: CallStmt(Id(foo),[Id(g),BinaryOp(==,CallExpr(Id(int_of_float),[CallExpr(Id(float_to_int),[IntLiteral(1)])]),IntLiteral(1)),BinaryOp(||,Id(z),BooleanLiteral(false)),BinaryOp(&&,Id(z),UnaryOp(!,CallExpr(Id(bool_of_string),[StringLiteral(False)])))])")
    #     self.assertTrue(TestChecker.test(input,expect,470))

    # def test_471(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z, t                    
    #                     Body:
    #                         x = float_to_int(1);
    #                         y = float_of_string("1");
    #                         z = x <=. (y -. 1.2) *. 1.3 \. t; 
    #                         z = foo(True, 1, 1, 1);
    #                         Return;
    #                     EndBody. 
    #                 Function: foo
    #                     Parameter: x, y, z, t
    #                     Body:
    #                         Return x;
    #                     EndBody.                      
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,471))
    
    # def test_472(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z, t                    
    #                     Body:
    #                         x = float_to_int(1);
    #                         y = float_of_string("1");
    #                         z = False || (x <=. (y -. 1.2) *. 1.3 \. t * float_to_int(1 % 2)); 
    #                         z = foo(True, 1, 1, 1);
    #                         Return;
    #                     EndBody. 
    #                 Function: foo
    #                     Parameter: x, y, z, t
    #                     Body:
    #                         Return x;
    #                     EndBody.                      
    #             """
    #     expect = str("Type Mismatch In Expression: BinaryOp(*,BinaryOp(\.,BinaryOp(*.,BinaryOp(-.,Id(y),FloatLiteral(1.2)),FloatLiteral(1.3)),Id(t)),CallExpr(Id(float_to_int),[BinaryOp(%,IntLiteral(1),IntLiteral(2))]))")
    #     self.assertTrue(TestChecker.test(input,expect,472))
    
    # def test_473(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z, t                    
    #                     Body:
    #                         x = float_to_int(1);
    #                         y = float_of_string("1");
    #                         z = False || (x <=. (y -. 1.2) *. 1.3 \. t *. float_to_int(1 % 2)); 
    #                         z = foo(True, 1, 1, 1);
    #                         Return;
    #                     EndBody. 
    #                 Function: foo
    #                     Parameter: x, y, z, t
    #                     Body:
    #                         Return x;
    #                     EndBody.                      
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,473))
    
    # def test_474(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z, t                    
    #                     Body:
    #                         Var: a[1];
    #                         x = -12;
    #                         a[0] = -12;
    #                         a[0] = -0.12E+5;
    #                         Return;
    #                     EndBody. 
    #                 Function: foo
    #                     Parameter: x, y, z, t
    #                     Body:
    #                         Return;
    #                     EndBody.       

    #                 Function: foo1
    #                     Parameter: x, y, z, t
    #                     Body:
    #                         Return;
    #                     EndBody.                      
    #             """
    #     expect = str("Type Mismatch In Expression: UnaryOp(-,FloatLiteral(12000.0))")
    #     self.assertTrue(TestChecker.test(input,expect,474))
    
    # def test_475(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z, t                    
    #                     Body:
    #                         Var: a[1]; 
    #                         x = -1;                           
    #                         a[0] = -12;
    #                         foo(x, a[2], int_of_float(1.2), -1);
    #                         Return;
    #                     EndBody. 
    #                 Function: foo
    #                     Parameter: x, y, z, t
    #                     Body:
    #                         foo1(t, y, int_of_float(1.2), -1);
    #                         Return;
    #                     EndBody.       

    #                 Function: foo1
    #                     Parameter: x, y, z, t
    #                     Body:
    #                         Return;
    #                     EndBody.                      
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,475))

    # def test_476(self):
    #     input = """
    #                 Function: main
    #                     Parameter: x[1][1], y
    #                     Body:
    #                         x = {{1},{1}};
    #                         Return;
    #                     EndBody.
    #             """
    #     expect = str("Type Mismatch In Statement: Assign(Id(x),ArrayLiteral(ArrayLiteral(IntLiteral(1)),ArrayLiteral(IntLiteral(1))))")
    #     self.assertTrue(TestChecker.test(input, expect, 476))

    # def test_477(self):
    #     input = r"""Var: x[1];
    #                 Var: main;
    #                 Function: foo
    #                 Parameter: x[1][1]
    #                 Body:
    #                     x = {{1.1}};                        
    #                     Return x;
    #                 EndBody.
    #             """
    #     expect = str("No Entry Point")
    #     self.assertTrue(TestChecker.test(input, expect, 477))
    
    # def test_478(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z, t                    
    #                     Body:
    #                         Var: a[1]; 
    #                         x = -1;                           
    #                         a[0] = -12;
    #                         foo(x, a[2], int_of_float(1.2), -1);
    #                         foo1(x, 1, int_of_float(0.5), -1);
    #                         Return;
    #                     EndBody. 
    #                 Function: foo
    #                     Parameter: x, y, z, t
    #                     Body:
    #                         foo1(t, y, int_of_float(0.1), -1);
    #                         Return;
    #                     EndBody.       

    #                 Function: foo1
    #                     Parameter: x, y, z, t
    #                     Body:
    #                         Return;
    #                     EndBody.                      
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,478))

    # def test_479(self):
    #     input = r"""Var: x[1];
    #                 Var: y[1] = {{1,2}};
    #                 Function: main
    #                 Parameter: x, y
    #                 Body:
    #                     x = {{1.1}};
    #                     Return x;
    #                 EndBody.
    #             """
    #     expect = str("Type Mismatch In Statement: VarDecl(Id(y),[1],ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2))))")
    #     self.assertTrue(TestChecker.test(input, expect, 479))

    # def test_480(self):
    #     input = """                        
    #                 Function: main
    #                     Parameter: x, y, z, t                    
    #                     Body:
    #                         Var: a[1]; 
    #                         x = -1;                           
    #                         a[0] = -12;
    #                         foo(x, a[2], int_of_float(1.2), -1);
    #                         foo1(x, 1, int_of_float(0.5), -1);
    #                         Return;
    #                     EndBody. 
    #                 Function: foo
    #                     Parameter: x, y, z, t
    #                     Body:
    #                         foo1(-.1.2, y, int_of_float(0.1), -1);
    #                         Return;
    #                     EndBody.       

    #                 Function: foo1
    #                     Parameter: x, y, z, t
    #                     Body:
    #                         Return;
    #                     EndBody.                      
    #             """
    #     expect = str("Type Mismatch In Statement: CallStmt(Id(foo1),[UnaryOp(-.,FloatLiteral(1.2)),Id(y),CallExpr(Id(int_of_float),[FloatLiteral(0.1)]),UnaryOp(-,IntLiteral(1))])")
    #     self.assertTrue(TestChecker.test(input,expect,480))

    # def test_481(self):
    #     input = """Var: x[1];                    
    #                 Function: foo
    #                 Parameter: x[1][1]
    #                 Body:
    #                     x = {{1.1}};                        
    #                     Return x;
    #                 EndBody.
    #             """
    #     expect = str("No Entry Point")
    #     self.assertTrue(TestChecker.test(input, expect, 481))

    # def test_482(self):
    #     input = """
    #                 Var: main;
    #                 Var: x[1];                    
    #                 Function: main
    #                 Parameter: x[1][1]
    #                 Body:
    #                     x = {{1.1}};                        
    #                     Return x;
    #                 EndBody.
    #             """
    #     expect = str("Redeclared Function: main")
    #     self.assertTrue(TestChecker.test(input, expect, 482))
    
    # def test_483(self):
    #     input = """
    #                 Var: x[1];
    #                 Var: y[1][3] = {{1,2}};
    #                 Function: main
    #                 Parameter: x, y, t, e, f, g
    #                 Body:
    #                     x = 1;
    #                     Return x;
    #                 EndBody.
    #             """
    #     expect = str(
    #         "Type Mismatch In Statement: VarDecl(Id(y),[1,3],ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2))))")
    #     self.assertTrue(TestChecker.test(input, expect, 483))

    # def test_484(self):
    #     input = """
    #                 Var: x[1];                    
    #                 Function: main
    #                 Parameter: x, y, t, e, f, g
    #                 Body:
    #                     x = 1;
    #                     x = printStr(string_of_int(12));
    #                     Return x;
    #                 EndBody.
    #             """
    #     expect = str(
    #         "Type Mismatch In Statement: Assign(Id(x),CallExpr(Id(printStr),[CallExpr(Id(string_of_int),[IntLiteral(12)])]))")
    #     self.assertTrue(TestChecker.test(input, expect, 484))

    # def test_485(self):
    #     input = """
    #                 Var: x[1];                    
    #                 Function: main
    #                 Parameter: x, y, t, e, f, g, z
    #                 Body:                    
    #                     printStr(string_of_int(y));
    #                     printStrLn(z);
    #                     y = z;
    #                     Return;
    #                 EndBody.
    #             """
    #     expect = str(
    #         "Type Mismatch In Statement: Assign(Id(y),Id(z))")
    #     self.assertTrue(TestChecker.test(input, expect, 485))

    # def test_486(self):
    #     input = r"""
    #                 Var: a;
    #                 Function: main                    
    #                 Body:
    #                     Var: z,c;
    #                     z = 1;
    #                     a = 1.1;
    #                     c = z + foo(a +. foo(a));
    #                 EndBody.

    #                 Function: foo
    #                 Parameter: x
    #                 Body:
    #                     Return x;
    #                 EndBody.
    #             """
    #     expect = str(
    #         "Type Mismatch In Expression: BinaryOp(+,Id(z),CallExpr(Id(foo),[BinaryOp(+.,Id(a),CallExpr(Id(foo),[Id(a)]))]))")
    #     self.assertTrue(TestChecker.test(input, expect, 486))

    # def test_487(self):
    #     input = r"""
    #                 Var: a;
    #                 Function: main                    
    #                 Body:
    #                     Var: z,c;
    #                     z = 1;
    #                     a = 1.1;
    #                     c = z + foo(c);
    #                 EndBody.

    #                 Function: foo
    #                 Parameter: x
    #                 Body:
    #                     Return x;
    #                 EndBody.
    #             """
    #     expect = str(
    #         "Type Cannot Be Inferred: Assign(Id(c),BinaryOp(+,Id(z),CallExpr(Id(foo),[Id(c)])))")
    #     self.assertTrue(TestChecker.test(input, expect, 487))

    # def test_488(self):
    #     input = r"""
    #                 Var: a;
    #                 Function: main                    
    #                 Body:
    #                     Var: z,c, arr[1];
    #                     z = 1;
    #                     a = 1.1;
    #                     c = z + foo(arr[0]);
    #                 EndBody.

    #                 Function: foo
    #                 Parameter: x
    #                 Body:
    #                     Return x;
    #                 EndBody.
    #             """
    #     expect = str(
    #         "Type Cannot Be Inferred: Assign(Id(c),BinaryOp(+,Id(z),CallExpr(Id(foo),[ArrayCell(Id(arr),[IntLiteral(0)])])))")
    #     self.assertTrue(TestChecker.test(input, expect, 488))

    # def test_489(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: foo
    #                     Parameter: x[1][1]
    #                     Body:      
    #                         For (a = 3 + int_of_string("\\'"), False , 1) Do
    #                             Var: a[1][1] = {{1}};
    #                             For (a = 1, True, 1) Do
    #                             EndFor.
    #                         EndFor.
    #                         Return;
    #                     EndBody.   

    #                 Function: main
    #                     Parameter: x, y, z[1][1]
    #                     Body:  
    #                         foo();                          
    #                         Return;
    #                     EndBody.    
    #             """
    #     expect = str("Type Mismatch In Statement: For(Id(a),IntLiteral(1),BooleanLiteral(true),IntLiteral(1),[],[])")
    #     self.assertTrue(TestChecker.test(input,expect,489))

    # def test_489(self):        
    #     input = """    
    #                 Var: a;
    #                 Function: foo
    #                     Parameter: x[1][1]
    #                     Body:      
    #                         For (a = 3 + int_of_string("\\'"), False , 1) Do
    #                             Var: a[1][1] = {{1}};
    #                             For (a = 1, True, 1) Do
    #                             EndFor.
    #                         EndFor.
    #                         Return;
    #                     EndBody.   

    #                 Function: main
    #                     Parameter: x, y, z[1][1]
    #                     Body:  
    #                         foo();                          
    #                         Return;
    #                     EndBody.    
    #             """
    #     expect = str("Type Mismatch In Statement: For(Id(a),IntLiteral(1),BooleanLiteral(true),IntLiteral(1),[],[])")
    #     self.assertTrue(TestChecker.test(input,expect,489))
    
    # def test_490(self):        
    #     input = """                        
    #                 Var: x, y, z[1][1];
    #                 Function: main
    #                     Parameter: x, y, z[1][1]
    #                     Body:  
    #                         Var: t[1], k[1];
    #                         k[1] = t[1] + y;
    #                         foo();                          
    #                         Return;
    #                     EndBody.    
    #             """
    #     expect = str("Undeclared Function: foo")
    #     self.assertTrue(TestChecker.test(input,expect,490))

    # def test_491(self):        
    #     input = """                        
    #                 Var: x, y, z[1][1];
    #                 Function: main
    #                     Parameter: x, y, z[1][1]
    #                     Body:  
    #                         Var: t[1], k[1];
    #                         k[1] = t[1] + y;                            
    #                         Return;
    #                     EndBody.    
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input,expect,491))

    # def test_492(self):
    #     input = r"""
    #                 Var: a;
    #                 Function: main
    #                 Body:
    #                     Var: z,c,d[1];
    #                     z = 1;
    #                     a = 1.1;
    #                     c = z + foo(2)[1][1];
    #                 EndBody.

    #                 Function: foo
    #                 Parameter: x
    #                 Body:
    #                     Return {{1}};
    #                 EndBody.
    #             """
    #     expect = str("Type Cannot Be Inferred: Assign(Id(c),BinaryOp(+,Id(z),ArrayCell(CallExpr(Id(foo),[IntLiteral(2)]),[IntLiteral(1),IntLiteral(1)])))")
    #     self.assertTrue(TestChecker.test(input, expect, 492))

    # def test_493(self):
    #     input = r"""
    #                 Var: a;
    #                 Function: main
    #                 Body:
    #                     Var: z,c,d[1];                        
    #                     c = z + foo(foo(2));
    #                 EndBody.

    #                 Function: foo
    #                 Parameter: x
    #                 Body:
    #                     Return 1;
    #                 EndBody.
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input, expect, 493))

    # def test_494(self):
    #     input = """
    #                 Var: a;
    #                 Function: main
    #                 Body:
    #                     Var: z,c,b,x,d[1];
    #                     z = 1;
    #                     a = 1;
    #                     c = z + c * (a \\ 1) % b;
    #                     x = c < z;
    #                 EndBody.
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input, expect, 494))

    # def test_495(self):
    #     input = """
    #                 Var: a;
    #                 Function: main
    #                 Body:
    #                     Var: x;
    #                     x = string_of_float(float_to_int(int_of_float(1.2)));
    #                     Return;
    #                 EndBody.
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input, expect, 495))

    # def test_496(self):
    #     input = """
    #                 Var: a;
    #                 Function: foo
    #                 Body:
    #                     a = 1.2;
    #                     Return;
    #                 EndBody.

    #                 Function: main
    #                 Body:
    #                     a = True;                        
    #                     Return;
    #                 EndBody.
    #             """
    #     expect = str("Type Mismatch In Statement: Assign(Id(a),BooleanLiteral(true))")
    #     self.assertTrue(TestChecker.test(input, expect, 496))

    # def test_497(self):
    #     input = """
    #                 Var: a;
    #                 Function: foo
    #                 Body:
    #                     a = 1.2;
    #                     Return;
    #                 EndBody.

    #                 Function: main
    #                 Body:
    #                     Var: a;
    #                     a = True;                        
    #                     Return;
    #                 EndBody.

    #                 Function: foo1
    #                 Body:   
    #                     Var: z;
    #                     z = a || False;                                                               
    #                     Return;
    #                 EndBody.

    #             """
    #     expect = str("Type Mismatch In Expression: BinaryOp(||,Id(a),BooleanLiteral(false))")
    #     self.assertTrue(TestChecker.test(input, expect, 497))

    
    # def test_498(self):
    #     input = """
    #                 Var: a;
    #                 Function: foo
    #                 Body:
    #                     a = 1.2;
    #                     Return;
    #                 EndBody.

    #                 Function: main
    #                 Body:
    #                     Var: a;
    #                     a = True;                        
    #                     Return False;
    #                 EndBody.

    #                 Function: foo1
    #                 Body:   
    #                     Var: z;
    #                     z =  main() || False;                                                               
    #                     Return;
    #                 EndBody.
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input, expect, 498))   

    # def test_499(self):
    #     input = """                    
    #                 Function: main
    #                 Body:                        
    #                     Return;
    #                 EndBody.
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input, expect, 499))
    
    # def test_500(self):
    #     input = """
    #                 Var: a;
    #                 Function: main
    #                 Body:
    #                     Var: x, y;
    #                     x = float_of_string(string_of_float(float_to_int(int_of_float(1.2))));
    #                     x = float_of_string(string_of_bool(x >. 2.0));
    #                     y = read();
    #                     Return;
    #                 EndBody.
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input, expect, 500))

    # def test_501(self):
    #     input = """
    #                 Var: a;
    #                 Function: main
    #                 Body:
    #                     Var: x[1][1];
    #                     foo(foo1());
    #                     Return;
    #                 EndBody.

    #                 Function: foo
    #                     Parameter: x[1][1]
    #                 Body: 
    #                     Return;
    #                 EndBody.

    #                 Function: foo1                        
    #                 Body: 
    #                     Var: x[1][1];
    #                     Return x;
    #                 EndBody.
    #             """
    #     expect = str("Type Cannot Be Inferred: CallStmt(Id(foo),[CallExpr(Id(foo1),[])])")
    #     self.assertTrue(TestChecker.test(input, expect, 501))

    # def test_502(self):
    #     """Simple program: main"""
    #     input = """
    #     Function: foo
    #         Parameter: x, y, z
    #         Body:
    #             Return False;
    #         EndBody.
    #     Function: main
    #         Body:
    #             Var: x, y;
    #             x = foo(True, 1, foo(x, y, False));
    #             x = y;
    #             Return;
    #         EndBody."""
    #     expect = str(TypeMismatchInStatement(Assign(Id("x"), Id("y"))))
    #     self.assertTrue(TestChecker.test(input,expect,502))

    # def test_503(self):
    #     input = r"""
    #                 Var: a;
    #                 Function: foo
    #                 Parameter: x[1][1]
    #                 Body:
    #                     x[1][1] = 1;
    #                     Return x;
    #                 EndBody.
    #                 Function: foo1
    #                 Body:
    #                     Var: x[1][1] = {{1}};
    #                     Return foo(x);
    #                 EndBody.
    #                 Function: main
    #                 Body:
    #                     Var: z,c,d[1], y[1][1];
    #                     y = {{10}};
    #                     y = foo1();
    #                     Return;
    #                 EndBody.
    #             """
    #     expect = str("")
    #     self.assertTrue(TestChecker.test(input, expect, 503))