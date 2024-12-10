# Generated from ./grammar/yapl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .yaplParser import yaplParser
else:
    from yaplParser import yaplParser

# This class defines a complete generic visitor for a parse tree produced by yaplParser.

class yaplVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by yaplParser#program.
    def visitProgram(self, ctx:yaplParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#classs.
    def visitClasss(self, ctx:yaplParser.ClasssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#attributesDeclaration.
    def visitAttributesDeclaration(self, ctx:yaplParser.AttributesDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#methodDef.
    def visitMethodDef(self, ctx:yaplParser.MethodDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#attr.
    def visitAttr(self, ctx:yaplParser.AttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#formal.
    def visitFormal(self, ctx:yaplParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#new.
    def visitNew(self, ctx:yaplParser.NewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#minus.
    def visitMinus(self, ctx:yaplParser.MinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#mult.
    def visitMult(self, ctx:yaplParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#string.
    def visitString(self, ctx:yaplParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#isvoid.
    def visitIsvoid(self, ctx:yaplParser.IsvoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#false.
    def visitFalse(self, ctx:yaplParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#integer.
    def visitInteger(self, ctx:yaplParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#less.
    def visitLess(self, ctx:yaplParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#while.
    def visitWhile(self, ctx:yaplParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#plus.
    def visitPlus(self, ctx:yaplParser.PlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#div.
    def visitDiv(self, ctx:yaplParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#equal.
    def visitEqual(self, ctx:yaplParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#negative.
    def visitNegative(self, ctx:yaplParser.NegativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#not.
    def visitNot(self, ctx:yaplParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#paren.
    def visitParen(self, ctx:yaplParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#true.
    def visitTrue(self, ctx:yaplParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#block.
    def visitBlock(self, ctx:yaplParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#let.
    def visitLet(self, ctx:yaplParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#FunctionCall.
    def visitFunctionCall(self, ctx:yaplParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#id.
    def visitId(self, ctx:yaplParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#if.
    def visitIf(self, ctx:yaplParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#less_equal.
    def visitLess_equal(self, ctx:yaplParser.Less_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#assign.
    def visitAssign(self, ctx:yaplParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#methodCall.
    def visitMethodCall(self, ctx:yaplParser.MethodCallContext):
        return self.visitChildren(ctx)



del yaplParser