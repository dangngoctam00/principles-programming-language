import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_315(self):
        input = """
            Function: foo
            Body:
                Do a = b + 3; c[2][3] = 5; While x == y EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(Id("c"),[IntLiteral(2),IntLiteral(3)]),IntLiteral(5))]),BinaryOp("==",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))






# class StaticCheck(Visitor):
#     def visitProgram(self, ctx: Program, o: object):
#         o = [None,[]]
#         for decl in ctx.decl:
#             self.visit(decl, o)

#     def visitVarDecl(self, ctx: VarDecl, o: object):
#         if ctx.name in o[1]:
#             raise RedeclaredVariable(ctx.name)
#         o[1] += [ctx.name]

#     def visitConstDecl(self, ctx: ConstDecl, o: object):
#         if ctx.name in o[1]:
#             raise RedeclaredConstant(ctx.name)
#         o[1] += [ctx.name]

#     def visitFuncDecl(self, ctx: FuncDecl, o: object):
#         if ctx.name in o[1]:
#             raise RedeclaredFunction(ctx.name)
#         o[1] += [ctx.name]
#         fscope = [o, []]
#         for p in ctx.param:
#             self.visit(p, fscope)
#         bdecl = ctx.body[0]
#         for b in bdecl:
#             self.visit(b, fscope)
#         bexp = ctx.body[1]
#         for b in bexp:
#             self.visit(b, fscope)

#     def visitIntType(self, ctx: IntType, o: object): pass

#     def visitFloatType(self, ctx: FloatType, o: object): pass

#     def visitIntLit(self, ctx: IntLit, o: object): pass

#     def visitId(self, ctx: Id, o: object):
#         if not self.checkScope(ctx.name, o):
#             raise UndeclaredIdentifier(ctx.name)

#     def checkScope(self, name, scope):
#         if name in scope[1]:
#             return True
#         else:
#             if scope[0] == None:
#                 return False
#             else:
#                 return self.checkScope(name, scope[0])




# class StaticCheck(Visitor):
#     def visitProgram(self,ctx:Program,o:object):
#         o = [None, []]
#         [exp.accept(self, o) for exp in ctx.decl]
#     def visitVarDecl(self,ctx:VarDecl,o:object):
#         if ctx.name in o[1]:
#             raise RedeclaredVariable(ctx.name)
#         o[1] += [ctx.name]
#     def visitConstDecl(self,ctx:ConstDecl,o:object):
#         if ctx.name in o[1]:
#             raise RedeclaredConstant(ctx.name)
#         o[1] += [ctx.name]
#     def visitFuncDecl(self,ctx:FuncDecl,o:object):
#         if ctx.name in o[1]:
#             raise RedeclaredFunction(ctx.name)
#         o[1] += [ctx.name]
#         evn = [o, []]
#         [i.accept(self, evn) for i in ctx.param]
#         [i.accept(self, evn) for i in ctx.body[0]]
#         for x in ctx.body[1]:
#             if not self.checkUndeclare(x, evn):
#                 raise UndeclaredIdentifier(x.name)
        
#     def checkUndeclare(self, ctx: Id, o: object):
#         if ctx.name in o[1]:
#             return True
#         elif o[0] == None:
#             return False
#         else:
#             return self.checkUndeclare(ctx, o[0])
            
#     def visitIntType(self,ctx:IntType,o:object):pass

#     def visitFloatType(self,ctx:FloatType,o:object):pass

#     def visitIntLit(self,ctx:IntLit,o:object):pass

#     def visitId(self,ctx:Id,o:object):pass