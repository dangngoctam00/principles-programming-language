from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):
    # pass
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        # print("abc")
        declare = []
        if ctx.glo_variable_dec():
            declare = [i for glo_var in ctx.glo_variable_dec()
                       for i in glo_var.accept(self)]
        if ctx.function_dec():
            declare = declare + \
                [func_dec.accept(self) for func_dec in ctx.function_dec()]
        # print("declare" , declare)
        return Program(declare)

    def visitFunction_dec(self, ctx: BKITParser.Function_decContext):
        # print("visitFunction_dec")
        identifer = ctx.IDENTIFIER().getText()
        param = []
        if ctx.parameter_dec():
            param = ctx.parameter_dec().accept(self)
        list_sta = ([], [])
        if ctx.list_sta():
            list_sta = ctx.list_sta().accept(self)
        return FuncDecl(Id(identifer), param, list_sta)  # not complete

    def visitList_sta(self, ctx: BKITParser.List_staContext):
        var_decs = []
        list_sta = []
        # print("visitList_sta")
        if ctx.variable_dec():
            var_decs = [i for var_dec in ctx.variable_dec()
                        for i in var_dec.accept(self)]
        if ctx.statement():
            list_sta = [sta.accept(self) for sta in ctx.statement()]
        return (var_decs, list_sta)

    def visitStatement(self, ctx: BKITParser.StatementContext):

        if ctx.assignment_sta():
            # print("helakfjlaskfj")
            return ctx.assignment_sta().accept(self)
        elif ctx.if_sta():
            return ctx.if_sta().accept(self)
        elif ctx.for_sta():
            return ctx.for_sta().accept(self)
        elif ctx.while_sta():
            return ctx.while_sta().accept(self)
        elif ctx.do_while_sta():
            return ctx.do_while_sta().accept(self)
        elif ctx.break_sta():
            return ctx.break_sta().accept(self)
        elif ctx.continue_sta():
            return ctx.continue_sta().accept(self)
        elif ctx.call_sta():
            return ctx.call_sta().accept(self)
        elif ctx.return_sta():
            return ctx.return_sta().accept(self)

    def visitAssignment_sta(self, ctx: BKITParser.Assignment_staContext):
        left_operand = ctx.left_operand().accept(self)
        exp = ctx.exp().accept(self)
        return Assign(left_operand, exp)

    def visitIf_sta(self, ctx: BKITParser.If_staContext):
        lst_exp = [e.accept(self) for e in ctx.exp()]
        list_sta_body = [sta.accept(self) for sta in ctx.list_sta()]
        ifthenStmt = list(
            map(lambda e, s: (e, s[0], s[1]), lst_exp, list_sta_body))
        elseStmt = ([], [])
        if ctx.list_else_sta():
            elseStmt = ctx.list_else_sta().accept(self)
        return If(ifthenStmt, elseStmt)

    def visitFor_sta(self, ctx: BKITParser.For_staContext):
        idx = Id(ctx.IDENTIFIER().getText())
        exp1 = ctx.exp(0).accept(self)
        exp2 = ctx.exp(1).accept(self)
        exp3 = ctx.exp(2).accept(self)
        loop = ctx.list_sta().accept(self)
        return For(idx, exp1, exp2, exp3, loop)

    def visitWhile_sta(self, ctx: BKITParser.While_staContext):
        expr = ctx.exp().accept(self)
        sl = ctx.list_sta().accept(self)
        return While(expr, sl)

    def visitDo_while_sta(self, ctx: BKITParser.Do_while_staContext):
        expr = ctx.exp().accept(self)
        sl = ctx.list_sta().accept(self)
        return Dowhile(sl, expr)

    def visitBreak_sta(self, ctx: BKITParser.Break_staContext):
        return Break()

    def visitContinue_sta(self, ctx: BKITParser.Continue_staContext):
        return Continue()

    def visitReturn_sta(self, ctx: BKITParser.Return_staContext):
        expr = None
        if ctx.exp():
            expr = ctx.exp().accept(self)
        return Return(expr)

    def visitCall_sta(self, ctx: BKITParser.Call_staContext):
        id = Id(ctx.IDENTIFIER().getText())
        param = []
        if ctx.list_exp():
            param = ctx.list_exp().accept(self)
        return CallStmt(id, param)

    def visitList_else_sta(self, ctx: BKITParser.List_else_staContext):
        return ctx.list_sta().accept(self)

    def visitExp(self, ctx: BKITParser.ExpContext):
        if ctx.EQUAL_OP_INT():
            return BinaryOp(ctx.EQUAL_OP_INT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.NOT_EQUAL_OP_INT():
            return BinaryOp(ctx.NOT_EQUAL_OP_INT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.LESS_OP_INT():
            return BinaryOp(ctx.LESS_OP_INT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.GREATER_OP_INT():
            return BinaryOp(ctx.GREATER_OP_INT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.LESS_EQUAL_OP_INT():
            return BinaryOp(ctx.LESS_EQUAL_OP_INT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.GREATER_EQUAL_OP_INT():
            return BinaryOp(ctx.GREATER_EQUAL_OP_INT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.NOT_EQUAL_OP_FLOAT():
            return BinaryOp(ctx.NOT_EQUAL_OP_FLOAT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.LESS_OP_FLOAT():
            return BinaryOp(ctx.LESS_OP_FLOAT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.GREATER_OP_FLOAT():
            return BinaryOp(ctx.GREATER_OP_FLOAT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.LESS_EQUAL_OP_FLOAT():
            return BinaryOp(ctx.LESS_EQUAL_OP_FLOAT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.GREATER_EQUAL_OP_FLOAT():
            return BinaryOp(ctx.GREATER_EQUAL_OP_FLOAT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        else:
            return ctx.exp1(0).accept(self)

    def visitExp1(self, ctx: BKITParser.Exp1Context):
        if ctx.AND_OP():
            return BinaryOp(ctx.AND_OP().getText(), ctx.exp1().accept(self), ctx.exp2().accept(self))
        elif ctx.OR_OP():
            return BinaryOp(ctx.OR_OP().getText(), ctx.exp1().accept(self), ctx.exp2().accept(self))
        else:
            return ctx.exp2().accept(self)

    def visitExp2(self, ctx: BKITParser.Exp2Context):
        if ctx.ADD_OP_INT():
            return BinaryOp(ctx.ADD_OP_INT().getText(), ctx.exp2().accept(self), ctx.exp3().accept(self))
        elif ctx.SUB_OP_INT():
            return BinaryOp(ctx.SUB_OP_INT().getText(), ctx.exp2().accept(self), ctx.exp3().accept(self))
        elif ctx.ADD_OP_FLOAT():
            return BinaryOp(ctx.ADD_OP_FLOAT().getText(), ctx.exp2().accept(self), ctx.exp3().accept(self))
        elif ctx.SUB_OP_FLOAT():
            return BinaryOp(ctx.SUB_OP_FLOAT().getText(), ctx.exp2().accept(self), ctx.exp3().accept(self))
        else:
            return ctx.exp3().accept(self)

    def visitExp3(self, ctx: BKITParser.Exp3Context):
        if ctx.MUL_OP_INT():
            return BinaryOp(ctx.MUL_OP_INT().getText(), ctx.exp3().accept(self), ctx.exp4().accept(self))
        elif ctx.DIV_OP_INT():
            return BinaryOp(ctx.DIV_OP_INT().getText(), ctx.exp3().accept(self), ctx.exp4().accept(self))
        elif ctx.MOD_OP_INT():
            return BinaryOp(ctx.MOD_OP_INT().getText(), ctx.exp3().accept(self), ctx.exp4().accept(self))
        elif ctx.MUL_OP_FLOAT():
            return BinaryOp(ctx.MUL_OP_FLOAT().getText(), ctx.exp3().accept(self), ctx.exp4().accept(self))
        elif ctx.DIV_OP_FLOAT():
            return BinaryOp(ctx.DIV_OP_FLOAT().getText(), ctx.exp3().accept(self), ctx.exp4().accept(self))
        else:
            return ctx.exp4().accept(self)

    def visitExp4(self, ctx: BKITParser.Exp4Context):
        if ctx.NOT_OP():
            return UnaryOp(ctx.NOT_OP().getText(), ctx.exp4().accept(self))
        else:
            return ctx.exp5().accept(self)

    def visitExp5(self, ctx: BKITParser.Exp5Context):
        if ctx.SUB_OP_INT():
            return UnaryOp(ctx.SUB_OP_INT().getText(), ctx.exp5().accept(self))
        elif ctx.SUB_OP_FLOAT():
            return UnaryOp(ctx.SUB_OP_FLOAT().getText(), ctx.exp5().accept(self))
        else:
            return ctx.exp6().accept(self)

    def visitExp6(self, ctx: BKITParser.Exp6Context):
        if ctx.name_index_op():
            return ArrayCell(ctx.name_index_op().accept(self), ctx.index_operators().accept(self))
        elif ctx.function_call():
            return ctx.function_call().accept(self)

    def visitName_index_op(self, ctx: BKITParser.Name_index_opContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.function_call():
            return ctx.function_call().accept(self)

    def visitFunction_call(self, ctx: BKITParser.Function_callContext):
        if ctx.IDENTIFIER():
            identifier = ctx.IDENTIFIER().getText()
            exprs = ctx.list_exp().accept(self) if ctx.list_exp() else []
            return CallExpr(Id(identifier), exprs)
        elif ctx.exp8():
            return ctx.exp8().accept(self)

    def visitList_exp(self, ctx: BKITParser.List_expContext):
        return [expr.accept(self) for expr in ctx.exp()]

    def visitExp8(self, ctx: BKITParser.Exp8Context):
        if ctx.literal():
            return ctx.literal().accept(self)
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.exp():
            return ctx.exp().accept(self)

    def visitLeft_operand(self, ctx: BKITParser.Left_operandContext):
        if ctx.index_operators():
            identifier = Id(ctx.IDENTIFIER().getText())
            index_op = ctx.index_operators().accept(self)
            return ArrayCell(identifier, index_op)
        else:
            return Id(ctx.IDENTIFIER().getText())

    def visitIndex_operators(self, ctx: BKITParser.Index_operatorsContext):
        if ctx.index_operators():
            return ctx.index_operators().accept(self) + [ctx.exp().accept(self)]
        else:
            return [ctx.exp().accept(self)]
        # return [exp.accept(self) for exp in ctx.exp()]

    def visitVariable_dec(self, ctx: BKITParser.Variable_decContext):
        # print("visitVariable_dec")
        return ctx.list_var().accept(self)

    def visitParameter_dec(self, ctx: BKITParser.Parameter_decContext):
        return ctx.list_param().accept(self)

    def visitList_param(self, ctx: BKITParser.List_paramContext):
        # print("visitList_param")
        list_param = ctx.variable_id()
        lst = [var.accept(self) for var in list_param]
        #print("lst: ", lst)
        return [VarDecl(Id(var[0]), [], None) if len(var) == 1 else VarDecl(Id(var[0]), var[1:], None) for var in lst]

    def visitGlo_variable_dec(self, ctx: BKITParser.Glo_variable_decContext):
        return [i for var in ctx.list_var() for i in var.accept(self)]

    def visitList_var(self, ctx: BKITParser.List_varContext):
        return [elem.accept(self) for elem in ctx.var_elem()]

    def visitVar_elem(self, ctx: BKITParser.Var_elemContext):
        if ctx.var():
            return ctx.var().accept(self)
        else:
            return ctx.var_init().accept(self)

    def visitVar(self, ctx: BKITParser.VarContext):
        identifier = ctx.variable_id().accept(self)
        if len(identifier) == 1:
            return VarDecl(Id(identifier[0]), [], None)
        else:
            return VarDecl(Id(identifier[0]), identifier[1:], None)

    def visitVar_init(self, ctx: BKITParser.Var_initContext):
        identifier = ctx.variable_id().accept(self)
        value = ctx.value().accept(self)
        # print("visitVar_init")
        if len(identifier) == 1:
            return VarDecl(Id(identifier[0]), [], value)
        else:
            return VarDecl(Id(identifier[0]), identifier[1:], value)

    def visitValue(self, ctx: BKITParser.ValueContext):
        return ctx.literal().accept(self)

    def visitArray(self, ctx: BKITParser.ArrayContext):
        lst_content = [i for elem in ctx.array_elem()
                       for i in elem.accept(self)]
        # print("visitArray")
        #print (lst_content)
        return ArrayLiteral(lst_content)

    def visitArray_elem(self, ctx: BKITParser.Array_elemContext):
        if len(ctx.array()) == 0:
            return [i.accept(self) for i in ctx.value()]
        elif len(ctx.array()) == 1:
            return [ctx.array(0).accept(self)]
        else:
            return [ctx.array(0).accept(self)] + [ctx.array(1).accept(self)]

    def visitLiteral(self, ctx: BKITParser.LiteralContext):
        if ctx.INTEGER():
            return IntLiteral(eval(ctx.INTEGER().getText()))
        elif ctx.FLOAT():
            return FloatLiteral(eval(ctx.FLOAT().getText()))
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        elif ctx.boolean():
            return ctx.boolean().accept(self)
        elif ctx.array():
            #print("visit array of primary_type", ctx.array().accept(self))
            return ctx.array().accept(self)


    def visitBoolean(self, ctx: BKITParser.BooleanContext):
        if ctx.TRUE():
            return BooleanLiteral(True)
        else:
            return BooleanLiteral(False)

    def visitVariable_id(self, ctx: BKITParser.Variable_idContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFIER().getText()]
        else:
            identifier = [ctx.IDENTIFIER().getText()]
            dimen = list(map(lambda i: eval(i.getText()), ctx.INTEGER()))
            res = identifier + dimen
            return res
