
"""
 * @author dntam
 * ID: 1813910
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type


@dataclass
class Symbol:
    name: str
    mtype:Type

@dataclass
class MType:
    # [params type] , return type?
    intype:List[Symbol]
    restype:Type


class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([Symbol('x', FloatType())],IntType())),
Symbol("float_to_int",MType([Symbol('x',IntType())],FloatType())),
Symbol("int_of_string",MType([Symbol('x',StringType())],IntType())),
Symbol("string_of_int",MType([Symbol('x',IntType())],StringType())),
Symbol("float_of_string",MType([Symbol('x',StringType())],FloatType())),
Symbol("string_of_float",MType([Symbol('x',FloatType())],StringType())),
Symbol("bool_of_string",MType([Symbol('x',StringType())],BoolType())),
Symbol("string_of_bool",MType([Symbol('x',BoolType())],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([Symbol('x',StringType())],VoidType())),
Symbol("printStrLn",MType([Symbol('x',StringType())],VoidType()))]    
#         self.builtInFunction = [
# "int_of_float", "float_of_int", "int_of_string",
# "string_of_int", "float_of_string", "string_of_float", "bool_of_string",
# "string_of_bool", "read", "printLn", "printStr", "printStrLn"]                       
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    @staticmethod
    def visitParamDecl(ast, c):
        # variable : Id
        # varDimen : List[int] # empty list for scalar variable
        # varInit  : Literal   # always None
        
        paramName = ast.variable.name
        if paramName in list(map(lambda par: par.name, c)):
            raise Redeclared(Parameter(), paramName)
        if len(ast.varDimen) == 0:
            c += [Symbol(paramName, Unknown())]
        else:
            c += [Symbol(paramName, ArrayType(ast.varDimen, Unknown()))]
        #print("c: ", c)
        


    @staticmethod
    def visitFuncInitial(ast, c):
        # name: Id
        # param: List[VarDecl]
        # body: Tuple[List[VarDecl],List[Stmt]]]

        #check redelcare

        functionName = ast.name.name
        if functionName in list(map(lambda var: var.name, c)):
            raise Redeclared(Function(), functionName)

        params = [Symbol(functionName, Unknown())]
        [StaticChecker.visitParamDecl(par, params) for par in ast.param]
        params.pop(0)

        #func_record = [function_name, params, return_type]
        #func_record = Symbol(functionName, MType(list(map(lambda p: p.mtype ,params)), Unknown()))
        #print("params: ", params)
        func_record = Symbol(functionName, MType(params, Unknown()))
        c += [func_record]
        #print("c: ", c)

        

    def visitProgram(self,ast, c):
        #decl : List[Decl]
        #c = []
        for declare in ast.decl:
            if isinstance(declare, VarDecl):
                self.visit(declare, self.global_envi)
            elif isinstance(declare, FuncDecl):
                StaticChecker.visitFuncInitial(declare, self.global_envi)

        main_function = list(filter(lambda func: func.name == "main", self.global_envi))
        if len(main_function) == 0:
            raise NoEntryPoint()
        elif not isinstance(main_function[0].mtype, MType):
            raise NoEntryPoint()
        for declare in ast.decl:
            if isinstance(declare, FuncDecl):
                self.visit(declare, self.global_envi)
                
        #[self.visit(x,c) for x in ast.decl]

    def visitVarDecl(self, ast, c):
        # variable : Id
        # varDimen : List[int] # empty list for scalar variable
        # varInit  : Literal   # null if no initial
        typeOfElement = None
        if len(ast.varDimen) == 0:
            typeOfElement = self.visit(ast.varInit, c) if ast.varInit else Unknown()
        else:
            if ast.varInit:
                arr_type = self.visit(ast.varInit, c)
                if arr_type.dimen == ast.varDimen:
                    typeOfElement = arr_type
                else:
                    raise TypeMismatchInStatement(ast)
            else:
                typeOfElement = ArrayType(ast.varDimen, Unknown())
                          
        variableName = ast.variable.name

        if variableName in list(map(lambda var: var.name, c)):
            raise Redeclared(Variable(), variableName)
        
        c += [Symbol(variableName, typeOfElement)]
        
        #print('c: ', c)

    def visitFuncDecl(self, ast, c):
        # name: Id
        # param: List[VarDecl]
        # body: Tuple[List[VarDecl],List[Stmt]]
        func_record = list(filter(lambda func: func.name == ast.name.name, c))[0]
        local_env = [Symbol(ast.name.name, Unknown())] + [func_record] + func_record.mtype.intype
        #[local_env += [Symbol(par.variable.name, )] for par in ast.param]
        [self.visit(var, local_env) for var in ast.body[0]]
        local_env.pop(0)
        local_env_name = list(map(lambda local: local.name, local_env))
        for global_var in c:
            if global_var.name not in local_env_name:
                local_env.append(global_var)
        #func_record.mtype.intype = list(map(lambda p: p.mtype , func_record.mtype.intype))
        #print("local: ", local_env)
        #Stmt: Assign, If, For, Break, Continue, Return, DoWhile, While, CallStmt
        try:
            # [self.visit(stmt, local_env) for stmt in ast.body[1]]
            for stmt in ast.body[1]:
                self.visit(stmt, local_env)
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(stmt)

    @staticmethod
    def checkArrayType(ast, arr):
        if isinstance(arr.eletype, Unknown):
            raise TypeCannotBeInferred(arr)
    
    def visitAssign(self, ast, c):
        # lhs: LHS : Id / ArrayCell
        # rhs: Expr        
        #Expr: Literal, CallExpr, BinaryOp, UnaryOp, Id
        rhs_type = self.visit(ast.rhs, c)
        lhs_type = self.visit(ast.lhs, c)
        if isinstance(lhs_type, VoidType) or isinstance(rhs_type, VoidType):
            raise TypeMismatchInStatement(ast)
        #print("abcakjsdkasd: ", lhs_type, rhs_type)
        if isinstance(lhs_type, Unknown) and isinstance(rhs_type, Unknown):            
            raise TypeCannotBeInferred(ast)

        if isinstance(lhs_type, ArrayType): #lhs: id           
            ####error
            if isinstance(rhs_type, Unknown):
                
                if isinstance(ast.rhs, Id):
                    rhs_object = list(filter(lambda x: x.name == ast.rhs.name, c))[0]
                    rhs_object.mtype = lhs_type
                else: #callexpr
                    rhs_object = list(filter(lambda x: x.name == ast.rhs.method.name, c))[0]
                    rhs_object.mtype.restype = lhs_type
                            
                StaticChecker.checkArrayType(ast, lhs_type)
                
            elif not isinstance(rhs_type, ArrayType):
                
                raise TypeMismatchInStatement(ast)
            else:
                if len(lhs_type.dimen) != len(rhs_type.dimen):                    
                    raise TypeMismatchInStatement(ast)
                for i in range(len(lhs_type.dimen)):
                    if lhs_type.dimen[i] != rhs_type.dimen[i]:                        
                        raise TypeMismatchInStatement(ast)
                lhs_object = list(filter(lambda x: x.name == ast.lhs.name, c))[0]
                if isinstance(ast.rhs, Id): 
                    # print("check point")
                    rhs_name = ast.rhs.name                 
                    rhs_object = list(filter(lambda x: x.name == rhs_name, c))[0]
                    if isinstance(lhs_object.mtype.eletype, Unknown) and isinstance(rhs_object.mtype.eletype, Unknown):
                        raise TypeCannotBeInferred(ast)
                    elif isinstance(lhs_object.mtype.eletype, Unknown):
                        lhs_object.mtype.eletype = rhs_type.eletype        
                    elif isinstance(rhs_object.mtype.eletype, Unknown):
                        rhs_object.mtype.eletype = lhs_type.eletype
                    elif not isinstance(lhs_type.eletype, type(rhs_type.eletype)):
                        #print("check: " +  str(lhs_type) +  "\\\\" + str(rhs_type))
                        raise TypeMismatchInStatement(ast)
                elif isinstance(ast.rhs, CallExpr):
                    rhs_name = ast.rhs.method.name                   
                    rhs_object = list(filter(lambda x: x.name == rhs_name, c))[0]
                    if isinstance(lhs_object.mtype.eletype, Unknown) and isinstance(rhs_object.mtype.restype.eletype, Unknown):
                        raise TypeCannotBeInferred(ast)
                    elif isinstance(lhs_object.mtype.eletype, Unknown):
                        lhs_object.mtype.eletype = rhs_type.eletype        
                    elif isinstance(rhs_object.mtype.restype.eletype, Unknown):
                        rhs_object.mtype.restype.eletype = lhs_type.eletype
                    elif not isinstance(lhs_type.eletype, type(rhs_type.eletype)):
                        #print("check: " +  str(lhs_type) +  "\\\\" + str(rhs_type))
                        raise TypeMismatchInStatement(ast)
                else:
                    if isinstance(lhs_object.mtype.eletype, Unknown):
                        lhs_object.mtype.eletype = rhs_type.eletype
                    else:
                        raise TypeMismatchInStatement(ast)
        else:            
            if isinstance(lhs_type, Unknown):
                # lhs_object = list(filter(lambda x: x.name == ast.lhs.name, c))[0]
                # if isinstance(ast.lhs, Id):
                #     lhs_object.mtype = rhs_type
                # else:
                #     lhs_object.mtype.restype = rhs_type
                if isinstance(rhs_type, ArrayType):
                    raise TypeMismatchInStatement(ast)
                self.setVariableUnknowType(ast.lhs, rhs_type, c)

                #print("lhs_type: ", rhs_type)
            elif isinstance(rhs_type, Unknown):
                if isinstance(ast.rhs, ArrayCell):
                    StaticChecker.setTypeArrayCell(ast.rhs, lhs_type, c)
                elif isinstance(ast.rhs, CallExpr):
                    StaticChecker.setTypeCallExpr(ast.rhs, lhs_type, c)
                else:                       
                    rhs_object = list(filter(lambda x: x.name == ast.rhs.name, c))[0]
                    rhs_object.mtype = lhs_type
            elif not isinstance(lhs_type, type(rhs_type)):               
                raise TypeMismatchInStatement(ast)



    @staticmethod
    def setTypeArrayCell(ast, type_obj, c):
        obj = list(filter(lambda x: x.name == ast.arr.name, c))[0]
        if isinstance(ast.arr, Id):
            obj.mtype = type_obj
        else:
            obj.mtype.restype = type_obj    


    @staticmethod
    def setTypeCallExpr(ast, type_obj ,c):
        obj = list(filter(lambda x: x.name == ast.method.name, c))[0]
        obj.mtype.restype = type_obj
    

    def visitArrayCell(self, ast, c):
        # arr:Expr
        # idx:List[Expr]
        idx_type = list(map(lambda i: self.visit(i, c), ast.idx))
        notIntType = list(filter(lambda i: not isinstance(i, IntType), idx_type))
        if len(notIntType) > 0:
            raise TypeMismatchInExpression(ast)
        arr_type = self.visit(ast.arr, c)
        #print("arr_type: ", arr_type, ast.arr)
        
        if isinstance(arr_type, Unknown):
            raise TypeCannotBeInferred(ast)

        if not isinstance(arr_type, ArrayType):            
            raise TypeMismatchInExpression(ast)
        if len(idx_type) != len(arr_type.dimen):
            raise TypeMismatchInExpression(ast)        
        return arr_type.eletype

    def visitCallExpr(self, ast, c):
        #method:Id
        #param:List[Expr]
        # if ast.method.name in self.builtInFunction:
        #     return self.checkBuiltInFunction(ast, c)
        
        func = list(filter(lambda f : f.name == ast.method.name, c))
        if len(func) == 0:
            raise Undeclared(Function(), ast.method.name)
        func = func[0]
        params = func.mtype.intype
        #print("params: ", params)
        # args = list(map(lambda arg: self.visit(arg, c), ast.param))
        args_len = len(ast.param)
        
        if len(params) != args_len:
            raise TypeMismatchInExpression(ast)
        for i in range(len(params)):
            arg = self.visit(ast.param[i], c)
            if isinstance(params[i].mtype, Unknown) and isinstance(arg, Unknown):
                raise TypeCannotBeInferred(ast)
            if isinstance(params[i].mtype, ArrayType) and isinstance(arg, ArrayType):                
                if isinstance(params[i].mtype.eletype, Unknown) and isinstance(arg.eletype, Unknown):                    
                    raise TypeCannotBeInferred(ast)
                if len(params[i].mtype.dimen) != len(arg.dimen):
                    raise TypeMismatchInExpression(ast)
                for j in range(len(arg.dimen)):                    
                    if params[i].mtype.dimen[j] != arg.dimen[j]:                       
                        raise TypeMismatchInExpression(ast)
                if isinstance(params[i].mtype.eletype, Unknown):
                    params[i].mtype.eletype = arg.eletype
                elif isinstance(arg.eletype, Unknown):
                    arg.eletype = params[i].mtype.eletype
                elif not isinstance(arg.eletype, type(params[i].mtype.eletype)):
                    raise TypeMismatchInExpression(ast)
            else:
                #print("args: ", args)
                if isinstance(params[i].mtype, Unknown):
                    params[i].mtype = arg
                elif isinstance(arg, Unknown):
                    if isinstance(ast.param[i], Id):
                        arg_object = list(filter(lambda x: x.name == ast.param[i].name, c))[0]
                        arg_object.mtype = params[i].mtype
                    elif isinstance(ast.param[i], CallExpr):
                        func = list(filter(lambda x: x.name == ast.param[i].method.name, c))[0]
                        func.mtype.restype = params[i].mtype
                    elif isinstance(ast.param[i], ArrayCell):
                        if isinstance(ast.param[i].arr, CallExpr):
                            func = list(filter(lambda x: x.name == ast.param[i].arr.method.name, c))[0]
                            func.mtype.restype = params[i].mtype
                        else:
                            var = list(filter(lambda x: x.name == ast.param[i].arr.name, c))
                            var.mtype = params[i].mtype                                            
                elif not isinstance(params[i].mtype, type(arg)):
                    raise TypeMismatchInExpression(ast)


        return func.mtype.restype



    def setVariableUnknowType(self, ast, mtype, c):        
        if isinstance(ast, Id):
            arg_object = list(filter(lambda x: x.name == ast.name, c))[0]
            arg_object.mtype = mtype
        elif isinstance(ast, CallExpr):
            func = list(filter(lambda x: x.name == ast.method.name, c))[0]
            func.mtype.restype = mtype
        elif isinstance(ast, ArrayCell):
            #print("chack")
            if isinstance(ast.arr, CallExpr):
                func = list(filter(lambda x: x.name == ast.arr.method.name, c))[0]
                func.mtype.restype = mtype
            else:
                var = list(filter(lambda x: x.name == ast.arr.name, c))[0]
                var.mtype.eletype = mtype             


    def visitBinaryOp(self, ast, c):
        # op:str
        # left:Expr
        # right:Expr
        left_type = self.visit(ast.left, c)
        if ast.op in ['+', '-', '*', '\\', '%', '==', '!=', '<', '>', '<=', '>=']:            
            if type(left_type) not in [IntType, Unknown]:
                raise TypeMismatchInExpression(ast)
            if isinstance(left_type, Unknown):
                self.setVariableUnknowType(ast.left, IntType(), c)            
             
        elif ast.op in ['+.', '-.', '*.', '\.', '=/=', '<.', '>.', '<=.', '>=.']:
            if type(left_type) not in [FloatType, Unknown]:
                raise TypeMismatchInExpression(ast)
            if isinstance(left_type, Unknown):
                self.setVariableUnknowType(ast.left, FloatType(), c)            
            
        elif ast.op in ['&&', '||']:
            if type(left_type) not in [BoolType, Unknown]:
                raise TypeMismatchInExpression(ast)
            if isinstance(left_type, Unknown):
                self.setVariableUnknowType(ast.left, BoolType(), c)            

        right_type = self.visit(ast.right, c)
                
        if ast.op in ['+', '-', '*', '\\', '%', '==', '!=', '<', '>', '<=', '>=']:            
            if type(right_type) not in [IntType, Unknown]:                
                raise TypeMismatchInExpression(ast)            
            if isinstance(right_type, Unknown):
                self.setVariableUnknowType(ast.right, IntType(), c)              
        elif ast.op in ['+.', '-.', '*.', '\.', '=/=', '<.', '>.', '<=.', '>=.']:
            if type(right_type) not in [FloatType, Unknown]:
                raise TypeMismatchInExpression(ast)            
            if isinstance(right_type, Unknown):
                self.setVariableUnknowType(ast.right, FloatType(), c)                        
        elif ast.op in ['&&', '||']:
            if type(right_type) not in [BoolType, Unknown]:
                raise TypeMismatchInExpression(ast)        
            if isinstance(right_type, Unknown):
                self.setVariableUnknowType(ast.right, BoolType(),c)            

        if ast.op in ['+', '-', '*', '\\', '%', '==', '!=', '<', '>', '<=', '>=']:
            if ast.op in ['==', '!=', '<', '>', '<=', '>=']:
                return BoolType()
            return IntType()  
        if ast.op in ['+.', '-.', '*.', '\.', '=/=', '<.', '>.', '<=.', '>=.']:   
            if ast.op in ['=/=', '<.', '>.', '<=.', '>=.']:
                return BoolType()
            return FloatType()
        return BoolType()
        
        


    def visitUnaryOp(self, ast, c):
        #op:str
        #body:Expr
        expr_type = self.visit(ast.body, c)
        if ast.op == '-':
            if type(expr_type) not in [IntType, Unknown]:
                raise TypeMismatchInExpression(ast)
            if isinstance(expr_type, Unknown):
                self.setVariableUnknowType(ast.body, IntType(), c)
            return IntType()
        elif ast.op == '-.':
            if type(expr_type) not in [FloatType, Unknown]:
                raise TypeMismatchInExpression(ast)
            if isinstance(expr_type, Unknown):
                self.setVariableUnknowType(ast.body, FloatType(), c)
            return FloatType()
        elif ast.op == '!':
            if type(expr_type) not in [BoolType, Unknown]:
                raise TypeMismatchInExpression(ast)
            if isinstance(expr_type, Unknown):
                self.setVariableUnknowType(ast.body, BoolType(), c)
            return BoolType()
    
    def visitIf(self,ast,c):
        # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
        # elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
        # print("c: ", c)
        for i in range(len(ast.ifthenStmt)):
            
            type_expr = self.visit(ast.ifthenStmt[i][0], c)
            #print(ast.ifthenStmt[i][0])
            if type(type_expr) not in [BoolType, Unknown]:
                raise TypeMismatchInStatement(ast)
            if isinstance(type_expr, Unknown):
                self.setVariableUnknowType(ast.ifthenStmt[i][0], BoolType(), c)
            local_env = [] 
                      
            #[local_env += [Symbol(par.variable.name, )] for par in ast.param]
            [self.visit(var, local_env) for var in ast.ifthenStmt[i][1]]        
            local_env_name = list(map(lambda local: local.name, local_env))
            for global_var in c:
                if global_var.name not in local_env_name:
                    local_env.append(global_var)
            [self.visit(stmt, local_env) for stmt in ast.ifthenStmt[i][2]]
        
        if ast.elseStmt != None:
            local_env = []            
            #[local_env += [Symbol(par.variable.name, )] for par in ast.param]
            [self.visit(var, local_env) for var in ast.elseStmt[0]]        
            local_env_name = list(map(lambda local: local.name, local_env))
            for global_var in c:
                if global_var.name not in local_env_name:
                    local_env.append(global_var)
            [self.visit(stmt, local_env) for stmt in ast.elseStmt[1]]

    def visitFor(self, ast, c):
        # idx1: Id
        # expr1:Expr
        # expr2:Expr
        # expr3:Expr
        # loop: Tuple[List[VarDecl],List[Stmt]]
        id_type = self.visit(ast.idx1, c)
        expr1_type = self.visit(ast.expr1, c)
        expr2_type = self.visit(ast.expr2, c)
        expr3_type = self.visit(ast.expr3, c)
        if type(expr1_type) not in [IntType, Unknown] and type(expr3_type) not in [IntType, Unknown]:
            raise TypeMismatchInStatement(ast)
        if type(expr2_type) not in [BoolType, Unknown]:
            raise TypeMismatchInStatement(ast)
        if type(id_type) not in [IntType, Unknown]:
            raise TypeMismatchInStatement(ast)
        if isinstance(expr1_type, Unknown):
            self.setVariableUnknowType(ast.expr1, IntType(), c)
        if isinstance(expr3_type, Unknown):
            self.setVariableUnknowType(ast.expr3, IntType(), c)
        if isinstance(expr2_type, Unknown):
            self.setVariableUnknowType(ast.expr2, BoolType(), c)
        if isinstance(id_type, Unknown):
            id_obj = list(filter(lambda id: id.name == ast.idx1.name, c))[0]
            id_obj.mtype = IntType()
        local_env = []
        [self.visit(var, local_env) for var in ast.loop[0]]        
        local_env_name = list(map(lambda local: local.name, local_env))
        for global_var in c:
            if global_var.name not in local_env_name:
                local_env.append(global_var)
        [self.visit(stmt, local_env) for stmt in ast.loop[1]]



    def visitBreak(self, ast, c):
        pass

    def visitContinue(self, ast, c):
        pass

    def visitDowhile(self, ast, c):
        # sl:Tuple[List[VarDecl],List[Stmt]]
        # exp: Expr
        exp_type = self.visit(ast.exp, c)
        if type(exp_type) not in [BoolType, Unknown]:
            raise TypeMismatchInStatement(ast)
        if isinstance(exp_type, Unknown):
            self.setVariableUnknowType(ast.exp, BoolType(), c)
        local_env = []
        [self.visit(var, local_env) for var in ast.sl[0]]        
        local_env_name = list(map(lambda local: local.name, local_env))
        for global_var in c:
            if global_var.name not in local_env_name:
                local_env.append(global_var)
        [self.visit(stmt, local_env) for stmt in ast.sl[1]]
        
    def visitWhile(self, ast, c):
        # exp: Expr
        # sl:Tuple[List[VarDecl],List[Stmt]]     
        exp_type = self.visit(ast.exp, c)
        if type(exp_type) not in [BoolType, Unknown]:
            raise TypeMismatchInStatement(ast)
        if isinstance(exp_type, Unknown):
            self.setVariableUnknowType(ast.exp, BoolType(), c)
        local_env = []
        [self.visit(var, local_env) for var in ast.sl[0]]        
        local_env_name = list(map(lambda local: local.name, local_env))
        for global_var in c:
            if global_var.name not in local_env_name:
                local_env.append(global_var)
        [self.visit(stmt, local_env) for stmt in ast.sl[1]]   

    def visitCallStmt(self, ast, c):
        # method:Id
        # param:List[Expr]
        # if ast.method.name in self.builtInFunction:
        #     return self.checkBuiltInFunction(ast, c)
        func = list(filter(lambda f : f.name == ast.method.name, c))
        if len(func) == 0:
            raise Undeclared(Function(), ast.method.name)
        func = func[0]
        if isinstance(func.mtype.restype, Unknown):
            func.mtype.restype = VoidType()
        elif not isinstance(func.mtype.restype, VoidType):
            raise TypeMismatchInStatement(ast)
        params = func.mtype.intype
        #print("params: ", params)
        args = list(map(lambda arg: self.visit(arg, c), ast.param))
        #print("args: ", args)
        if len(params) != len(args):
            raise TypeMismatchInStatement(ast)

        for i in range(len(params)):
            if isinstance(params[i].mtype, Unknown) and isinstance(args[i], Unknown):
                raise TypeCannotBeInferred(ast)
            if isinstance(params[i].mtype, ArrayType) and isinstance(args[i], ArrayType):                
                if isinstance(params[i].mtype.eletype, Unknown) and isinstance(args[i].eletype, Unknown):                    
                    raise TypeCannotBeInferred(ast)
                if len(params[i].mtype.dimen) != len(args[i].dimen):
                    
                    raise TypeMismatchInStatement(ast)
                for j in range(len(args[i].dimen)):                    
                    if params[i].mtype.dimen[j] != args[i].dimen[j]:                       
                        raise TypeMismatchInStatement(ast)
                if isinstance(params[i].mtype.eletype, Unknown):
                    params[i].mtype.eletype = args[i].eletype
                elif isinstance(args[i].eletype, Unknown):
                    args[i].eletype = params[i].mtype.eletype
                else:
                    raise TypeMismatchInStatement(ast)
            else:
                if isinstance(params[i].mtype, Unknown):
                    params[i].mtype = args[i]                
                elif isinstance(args[i], Unknown):
                    if isinstance(ast.param[i], Id):
                        arg_object = list(filter(lambda x: x.name == ast.param[i].name, c))[0]
                        arg_object.mtype = params[i].mtype
                    elif isinstance(ast.param[i], CallExpr):
                        func = list(filter(lambda x: x.name == ast.param[i].method.name, c))[0]
                        func.mtype.restype = params[i].mtype
                        if isinstance(func.mtype.restype, ArrayType):
                            if isinstance(func.mtype.restype.eletype, Unknown):
                                raise TypeCannotBeInferred(ast)
                    elif isinstance(ast.param[i], ArrayCell):
                        if isinstance(ast.param[i].arr, CallExpr):
                            func = list(filter(lambda x: x.name == ast.param[i].arr.method.name, c))[0]
                            func.mtype.restype = params[i].mtype
                        else:
                            var = list(filter(lambda x: x.name == ast.param[i].arr.name, c))
                            var.mtype = params[i].mtype                                            

                elif not isinstance(params[i].mtype, type(args[i])):
                    raise TypeMismatchInStatement(ast)
                        
        return func.mtype.restype


    def visitReturn(self, ast, c):
        
        #expr:Expr # None if no expression
        #func_record = [name, [param], return_type]
        func_record = c[0]
        return_type = func_record.mtype.restype
        if ast.expr == None:
            
            if isinstance(return_type, Unknown):
                func_record.mtype.restype = VoidType()
            elif not isinstance(return_type, VoidType):
               
                raise TypeMismatchInStatement(ast)
        elif isinstance(return_type, VoidType):
            
            raise TypeMismatchInStatement(ast)
        else:
            #print("check")
            type_expr = self.visit(ast.expr, c)
            if isinstance(return_type, Unknown):
                
                if isinstance(type_expr, Unknown):
                    raise TypeCannotBeInferred(ast)
                else:
                    func_record.mtype.restype = type_expr 
                    #print("check1: ", func_record.mtype.restype)
            elif isinstance(type_expr, Unknown):
                self.setVariableUnknowType(ast.expr, return_type, c)
            elif not isinstance(return_type, type(type_expr)):
                #print("check")
                raise TypeMismatchInStatement(ast)


    def visitId(self, ast, c):
        #name : str
        id = list(filter(lambda x: x.name == ast.name, c))
        # if ast.name == 'y':
        #     print("id: ", id)
        if len(id) == 0:
            raise Undeclared(Identifier(), ast.name)
        return id[0].mtype

    def visitIntLiteral(self,ast,c):
        return IntType()

    def visitFloatLiteral(self,ast,c):
        return FloatType()

    def visitStringLiteral(self,ast,c):
        return StringType()

    def visitBooleanLiteral(self,ast,c):
        return BoolType()

    def visitArrayLiteral(self,ast,c):
        #value:List[Literal]
        #return one in four type of literal except array        
        eletype = self.visit(ast.value[0], c)
        
        if not isinstance(eletype, ArrayType):   
            #print("eletype: ", eletype)         
            return ArrayType([len(ast.value)], eletype)
        else:
            #print("11111", [len(ast.value)] + eletype.dimen)
            return ArrayType([len(ast.value)] + eletype.dimen, eletype.eletype)
               



        
