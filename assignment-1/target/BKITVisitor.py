# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#glo_variable_dec.
    def visitGlo_variable_dec(self, ctx:BKITParser.Glo_variable_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_var.
    def visitList_var(self, ctx:BKITParser.List_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_id.
    def visitVariable_id(self, ctx:BKITParser.Variable_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#value.
    def visitValue(self, ctx:BKITParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array.
    def visitArray(self, ctx:BKITParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#primary_type.
    def visitPrimary_type(self, ctx:BKITParser.Primary_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_dec.
    def visitFunction_dec(self, ctx:BKITParser.Function_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_sta.
    def visitList_sta(self, ctx:BKITParser.List_staContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter_dec.
    def visitParameter_dec(self, ctx:BKITParser.Parameter_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_param.
    def visitList_param(self, ctx:BKITParser.List_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_sta.
    def visitIf_sta(self, ctx:BKITParser.If_staContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_sta.
    def visitFor_sta(self, ctx:BKITParser.For_staContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_sta.
    def visitWhile_sta(self, ctx:BKITParser.While_staContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_sta.
    def visitDo_while_sta(self, ctx:BKITParser.Do_while_staContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_sta.
    def visitBreak_sta(self, ctx:BKITParser.Break_staContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_sta.
    def visitContinue_sta(self, ctx:BKITParser.Continue_staContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_sta.
    def visitCall_sta(self, ctx:BKITParser.Call_staContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_exp.
    def visitList_exp(self, ctx:BKITParser.List_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_sta.
    def visitReturn_sta(self, ctx:BKITParser.Return_staContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_dec.
    def visitVariable_dec(self, ctx:BKITParser.Variable_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignment_exp.
    def visitAssignment_exp(self, ctx:BKITParser.Assignment_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignment_sta.
    def visitAssignment_sta(self, ctx:BKITParser.Assignment_staContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#left_operand.
    def visitLeft_operand(self, ctx:BKITParser.Left_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#name_var.
    def visitName_var(self, ctx:BKITParser.Name_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operators.
    def visitIndex_operators(self, ctx:BKITParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#fuction_call.
    def visitFuction_call(self, ctx:BKITParser.Fuction_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp8.
    def visitExp8(self, ctx:BKITParser.Exp8Context):
        return self.visitChildren(ctx)



del BKITParser