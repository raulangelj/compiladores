# Generated from ./grammar/yapl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .yaplParser import yaplParser
else:
    from yaplParser import yaplParser

# This class defines a complete listener for a parse tree produced by yaplParser.
class yaplListener(ParseTreeListener):

    # Enter a parse tree produced by yaplParser#program.
    def enterProgram(self, ctx:yaplParser.ProgramContext):
        pass

    # Exit a parse tree produced by yaplParser#program.
    def exitProgram(self, ctx:yaplParser.ProgramContext):
        pass


    # Enter a parse tree produced by yaplParser#classs.
    def enterClasss(self, ctx:yaplParser.ClasssContext):
        pass

    # Exit a parse tree produced by yaplParser#classs.
    def exitClasss(self, ctx:yaplParser.ClasssContext):
        pass


    # Enter a parse tree produced by yaplParser#attributesDeclaration.
    def enterAttributesDeclaration(self, ctx:yaplParser.AttributesDeclarationContext):
        pass

    # Exit a parse tree produced by yaplParser#attributesDeclaration.
    def exitAttributesDeclaration(self, ctx:yaplParser.AttributesDeclarationContext):
        pass


    # Enter a parse tree produced by yaplParser#methodDef.
    def enterMethodDef(self, ctx:yaplParser.MethodDefContext):
        pass

    # Exit a parse tree produced by yaplParser#methodDef.
    def exitMethodDef(self, ctx:yaplParser.MethodDefContext):
        pass


    # Enter a parse tree produced by yaplParser#attr.
    def enterAttr(self, ctx:yaplParser.AttrContext):
        pass

    # Exit a parse tree produced by yaplParser#attr.
    def exitAttr(self, ctx:yaplParser.AttrContext):
        pass


    # Enter a parse tree produced by yaplParser#formal.
    def enterFormal(self, ctx:yaplParser.FormalContext):
        pass

    # Exit a parse tree produced by yaplParser#formal.
    def exitFormal(self, ctx:yaplParser.FormalContext):
        pass


    # Enter a parse tree produced by yaplParser#new.
    def enterNew(self, ctx:yaplParser.NewContext):
        pass

    # Exit a parse tree produced by yaplParser#new.
    def exitNew(self, ctx:yaplParser.NewContext):
        pass


    # Enter a parse tree produced by yaplParser#minus.
    def enterMinus(self, ctx:yaplParser.MinusContext):
        pass

    # Exit a parse tree produced by yaplParser#minus.
    def exitMinus(self, ctx:yaplParser.MinusContext):
        pass


    # Enter a parse tree produced by yaplParser#mult.
    def enterMult(self, ctx:yaplParser.MultContext):
        pass

    # Exit a parse tree produced by yaplParser#mult.
    def exitMult(self, ctx:yaplParser.MultContext):
        pass


    # Enter a parse tree produced by yaplParser#string.
    def enterString(self, ctx:yaplParser.StringContext):
        pass

    # Exit a parse tree produced by yaplParser#string.
    def exitString(self, ctx:yaplParser.StringContext):
        pass


    # Enter a parse tree produced by yaplParser#isvoid.
    def enterIsvoid(self, ctx:yaplParser.IsvoidContext):
        pass

    # Exit a parse tree produced by yaplParser#isvoid.
    def exitIsvoid(self, ctx:yaplParser.IsvoidContext):
        pass


    # Enter a parse tree produced by yaplParser#false.
    def enterFalse(self, ctx:yaplParser.FalseContext):
        pass

    # Exit a parse tree produced by yaplParser#false.
    def exitFalse(self, ctx:yaplParser.FalseContext):
        pass


    # Enter a parse tree produced by yaplParser#integer.
    def enterInteger(self, ctx:yaplParser.IntegerContext):
        pass

    # Exit a parse tree produced by yaplParser#integer.
    def exitInteger(self, ctx:yaplParser.IntegerContext):
        pass


    # Enter a parse tree produced by yaplParser#less.
    def enterLess(self, ctx:yaplParser.LessContext):
        pass

    # Exit a parse tree produced by yaplParser#less.
    def exitLess(self, ctx:yaplParser.LessContext):
        pass


    # Enter a parse tree produced by yaplParser#while.
    def enterWhile(self, ctx:yaplParser.WhileContext):
        pass

    # Exit a parse tree produced by yaplParser#while.
    def exitWhile(self, ctx:yaplParser.WhileContext):
        pass


    # Enter a parse tree produced by yaplParser#plus.
    def enterPlus(self, ctx:yaplParser.PlusContext):
        pass

    # Exit a parse tree produced by yaplParser#plus.
    def exitPlus(self, ctx:yaplParser.PlusContext):
        pass


    # Enter a parse tree produced by yaplParser#div.
    def enterDiv(self, ctx:yaplParser.DivContext):
        pass

    # Exit a parse tree produced by yaplParser#div.
    def exitDiv(self, ctx:yaplParser.DivContext):
        pass


    # Enter a parse tree produced by yaplParser#equal.
    def enterEqual(self, ctx:yaplParser.EqualContext):
        pass

    # Exit a parse tree produced by yaplParser#equal.
    def exitEqual(self, ctx:yaplParser.EqualContext):
        pass


    # Enter a parse tree produced by yaplParser#negative.
    def enterNegative(self, ctx:yaplParser.NegativeContext):
        pass

    # Exit a parse tree produced by yaplParser#negative.
    def exitNegative(self, ctx:yaplParser.NegativeContext):
        pass


    # Enter a parse tree produced by yaplParser#not.
    def enterNot(self, ctx:yaplParser.NotContext):
        pass

    # Exit a parse tree produced by yaplParser#not.
    def exitNot(self, ctx:yaplParser.NotContext):
        pass


    # Enter a parse tree produced by yaplParser#paren.
    def enterParen(self, ctx:yaplParser.ParenContext):
        pass

    # Exit a parse tree produced by yaplParser#paren.
    def exitParen(self, ctx:yaplParser.ParenContext):
        pass


    # Enter a parse tree produced by yaplParser#true.
    def enterTrue(self, ctx:yaplParser.TrueContext):
        pass

    # Exit a parse tree produced by yaplParser#true.
    def exitTrue(self, ctx:yaplParser.TrueContext):
        pass


    # Enter a parse tree produced by yaplParser#block.
    def enterBlock(self, ctx:yaplParser.BlockContext):
        pass

    # Exit a parse tree produced by yaplParser#block.
    def exitBlock(self, ctx:yaplParser.BlockContext):
        pass


    # Enter a parse tree produced by yaplParser#let.
    def enterLet(self, ctx:yaplParser.LetContext):
        pass

    # Exit a parse tree produced by yaplParser#let.
    def exitLet(self, ctx:yaplParser.LetContext):
        pass


    # Enter a parse tree produced by yaplParser#FunctionCall.
    def enterFunctionCall(self, ctx:yaplParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by yaplParser#FunctionCall.
    def exitFunctionCall(self, ctx:yaplParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by yaplParser#id.
    def enterId(self, ctx:yaplParser.IdContext):
        pass

    # Exit a parse tree produced by yaplParser#id.
    def exitId(self, ctx:yaplParser.IdContext):
        pass


    # Enter a parse tree produced by yaplParser#if.
    def enterIf(self, ctx:yaplParser.IfContext):
        pass

    # Exit a parse tree produced by yaplParser#if.
    def exitIf(self, ctx:yaplParser.IfContext):
        pass


    # Enter a parse tree produced by yaplParser#less_equal.
    def enterLess_equal(self, ctx:yaplParser.Less_equalContext):
        pass

    # Exit a parse tree produced by yaplParser#less_equal.
    def exitLess_equal(self, ctx:yaplParser.Less_equalContext):
        pass


    # Enter a parse tree produced by yaplParser#assign.
    def enterAssign(self, ctx:yaplParser.AssignContext):
        pass

    # Exit a parse tree produced by yaplParser#assign.
    def exitAssign(self, ctx:yaplParser.AssignContext):
        pass


    # Enter a parse tree produced by yaplParser#methodCall.
    def enterMethodCall(self, ctx:yaplParser.MethodCallContext):
        pass

    # Exit a parse tree produced by yaplParser#methodCall.
    def exitMethodCall(self, ctx:yaplParser.MethodCallContext):
        pass



del yaplParser