# Generated from ./grammar/yapl.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,202,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,3,1,24,8,1,1,1,1,1,
        1,1,1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        3,2,42,8,2,1,3,1,3,1,3,1,3,1,3,5,3,49,8,3,10,3,12,3,52,9,3,5,3,54,
        8,3,10,3,12,3,57,9,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,71,8,3,3,3,73,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,
        5,5,5,85,8,5,10,5,12,5,88,9,5,5,5,90,8,5,10,5,12,5,93,9,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,4,5,114,8,5,11,5,12,5,115,1,5,1,5,1,5,1,5,1,5,1,5,5,5,124,
        8,5,10,5,12,5,127,9,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,152,8,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,178,8,5,1,5,1,5,1,5,1,5,1,5,1,
        5,5,5,186,8,5,10,5,12,5,189,9,5,5,5,191,8,5,10,5,12,5,194,9,5,1,
        5,5,5,197,8,5,10,5,12,5,200,9,5,1,5,0,1,10,6,0,2,4,6,8,10,0,0,233,
        0,15,1,0,0,0,2,19,1,0,0,0,4,36,1,0,0,0,6,72,1,0,0,0,8,74,1,0,0,0,
        10,151,1,0,0,0,12,13,3,2,1,0,13,14,5,24,0,0,14,16,1,0,0,0,15,12,
        1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,
        20,5,1,0,0,20,23,5,45,0,0,21,22,5,6,0,0,22,24,5,45,0,0,23,21,1,0,
        0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,31,5,21,0,0,26,27,3,6,3,0,27,
        28,5,24,0,0,28,30,1,0,0,0,29,26,1,0,0,0,30,33,1,0,0,0,31,29,1,0,
        0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,0,0,0,34,35,5,22,0,0,35,
        3,1,0,0,0,36,37,5,44,0,0,37,38,5,23,0,0,38,41,5,45,0,0,39,40,5,39,
        0,0,40,42,3,10,5,0,41,39,1,0,0,0,41,42,1,0,0,0,42,5,1,0,0,0,43,44,
        5,44,0,0,44,55,5,19,0,0,45,50,3,8,4,0,46,47,5,25,0,0,47,49,3,8,4,
        0,48,46,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,54,
        1,0,0,0,52,50,1,0,0,0,53,45,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,
        55,56,1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,59,5,20,0,0,59,60,5,
        23,0,0,60,61,5,45,0,0,61,62,5,21,0,0,62,63,3,10,5,0,63,64,5,22,0,
        0,64,73,1,0,0,0,65,66,5,44,0,0,66,67,5,23,0,0,67,70,5,45,0,0,68,
        69,5,39,0,0,69,71,3,10,5,0,70,68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,
        0,0,72,43,1,0,0,0,72,65,1,0,0,0,73,7,1,0,0,0,74,75,5,44,0,0,75,76,
        5,23,0,0,76,77,5,45,0,0,77,9,1,0,0,0,78,79,6,5,-1,0,79,80,5,44,0,
        0,80,91,5,19,0,0,81,86,3,10,5,0,82,83,5,25,0,0,83,85,3,10,5,0,84,
        82,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,90,1,0,0,
        0,88,86,1,0,0,0,89,81,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,
        1,0,0,0,92,94,1,0,0,0,93,91,1,0,0,0,94,152,5,20,0,0,95,96,5,4,0,
        0,96,97,3,10,5,0,97,98,5,10,0,0,98,99,3,10,5,0,99,100,5,2,0,0,100,
        101,3,10,5,0,101,102,5,3,0,0,102,152,1,0,0,0,103,104,5,11,0,0,104,
        105,3,10,5,0,105,106,5,8,0,0,106,107,3,10,5,0,107,108,5,9,0,0,108,
        152,1,0,0,0,109,113,5,21,0,0,110,111,3,10,5,0,111,112,5,24,0,0,112,
        114,1,0,0,0,113,110,1,0,0,0,114,115,1,0,0,0,115,113,1,0,0,0,115,
        116,1,0,0,0,116,117,1,0,0,0,117,118,5,22,0,0,118,152,1,0,0,0,119,
        120,5,14,0,0,120,125,3,4,2,0,121,122,5,25,0,0,122,124,3,4,2,0,123,
        121,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,
        128,1,0,0,0,127,125,1,0,0,0,128,129,5,5,0,0,129,130,3,10,5,19,130,
        152,1,0,0,0,131,132,5,12,0,0,132,152,5,45,0,0,133,134,5,27,0,0,134,
        152,3,10,5,17,135,136,5,7,0,0,136,152,3,10,5,16,137,138,5,13,0,0,
        138,152,3,10,5,8,139,140,5,19,0,0,140,141,3,10,5,0,141,142,5,20,
        0,0,142,152,1,0,0,0,143,152,5,44,0,0,144,152,5,43,0,0,145,152,5,
        46,0,0,146,152,5,15,0,0,147,152,5,16,0,0,148,149,5,44,0,0,149,150,
        5,39,0,0,150,152,3,10,5,1,151,78,1,0,0,0,151,95,1,0,0,0,151,103,
        1,0,0,0,151,109,1,0,0,0,151,119,1,0,0,0,151,131,1,0,0,0,151,133,
        1,0,0,0,151,135,1,0,0,0,151,137,1,0,0,0,151,139,1,0,0,0,151,143,
        1,0,0,0,151,144,1,0,0,0,151,145,1,0,0,0,151,146,1,0,0,0,151,147,
        1,0,0,0,151,148,1,0,0,0,152,198,1,0,0,0,153,154,10,15,0,0,154,155,
        5,31,0,0,155,197,3,10,5,16,156,157,10,14,0,0,157,158,5,32,0,0,158,
        197,3,10,5,15,159,160,10,13,0,0,160,161,5,29,0,0,161,197,3,10,5,
        14,162,163,10,12,0,0,163,164,5,30,0,0,164,197,3,10,5,13,165,166,
        10,11,0,0,166,167,5,34,0,0,167,197,3,10,5,12,168,169,10,10,0,0,169,
        170,5,33,0,0,170,197,3,10,5,11,171,172,10,9,0,0,172,173,5,37,0,0,
        173,197,3,10,5,10,174,177,10,23,0,0,175,176,5,28,0,0,176,178,5,45,
        0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,179,1,0,0,0,179,180,5,26,
        0,0,180,181,5,44,0,0,181,192,5,19,0,0,182,187,3,10,5,0,183,184,5,
        25,0,0,184,186,3,10,5,0,185,183,1,0,0,0,186,189,1,0,0,0,187,185,
        1,0,0,0,187,188,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,190,182,
        1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,195,
        1,0,0,0,194,192,1,0,0,0,195,197,5,20,0,0,196,153,1,0,0,0,196,156,
        1,0,0,0,196,159,1,0,0,0,196,162,1,0,0,0,196,165,1,0,0,0,196,168,
        1,0,0,0,196,171,1,0,0,0,196,174,1,0,0,0,197,200,1,0,0,0,198,196,
        1,0,0,0,198,199,1,0,0,0,199,11,1,0,0,0,200,198,1,0,0,0,18,17,23,
        31,41,50,55,70,72,86,91,115,125,151,177,187,192,196,198
    ]

class yaplParser ( Parser ):

    grammarFileName = "yapl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'true'", "'false'", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "':'", "';'", "','", "'.'", "'~'", "'@'", "'+'", "'-'", 
                     "'*'", "'/'", "'<'", "'<='", "'>'", "'>='", "'='", 
                     "'=>'", "'<-'", "'ERROR'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "ELSE", "FI", "IF", "IN", "INHERITS", 
                      "ISVOID", "LOOP", "POOL", "THEN", "WHILE", "NEW", 
                      "NOT", "LET", "TRUE", "FALSE", "WS", "NEWLINE", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "COLON", "SEMICOLON", 
                      "COMMA", "PERIOD", "NEGATIVE", "AT", "PLUS", "MINUS", 
                      "MULT", "DIV", "LESS_THAN", "LESS_EQUAL", "GREATER_THAN", 
                      "GREATER_EQUAL", "EQUAL", "FAT_ARROW", "ASSIGN", "ERROR", 
                      "COMMENT_BLOCK", "COMMENT_LINE", "INT_VAR", "ID_VAR", 
                      "TYPE_IDENTIFIER", "STR_VAR" ]

    RULE_program = 0
    RULE_classs = 1
    RULE_var_typescript = 2
    RULE_feature = 3
    RULE_formal = 4
    RULE_expr = 5

    ruleNames =  [ "program", "classs", "var_typescript", "feature", "formal", 
                   "expr" ]

    EOF = Token.EOF
    CLASS=1
    ELSE=2
    FI=3
    IF=4
    IN=5
    INHERITS=6
    ISVOID=7
    LOOP=8
    POOL=9
    THEN=10
    WHILE=11
    NEW=12
    NOT=13
    LET=14
    TRUE=15
    FALSE=16
    WS=17
    NEWLINE=18
    LPAREN=19
    RPAREN=20
    LBRACE=21
    RBRACE=22
    COLON=23
    SEMICOLON=24
    COMMA=25
    PERIOD=26
    NEGATIVE=27
    AT=28
    PLUS=29
    MINUS=30
    MULT=31
    DIV=32
    LESS_THAN=33
    LESS_EQUAL=34
    GREATER_THAN=35
    GREATER_EQUAL=36
    EQUAL=37
    FAT_ARROW=38
    ASSIGN=39
    ERROR=40
    COMMENT_BLOCK=41
    COMMENT_LINE=42
    INT_VAR=43
    ID_VAR=44
    TYPE_IDENTIFIER=45
    STR_VAR=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ClasssContext)
            else:
                return self.getTypedRuleContext(yaplParser.ClasssContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.SEMICOLON)
            else:
                return self.getToken(yaplParser.SEMICOLON, i)

        def getRuleIndex(self):
            return yaplParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = yaplParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.classs()
                self.state = 13
                self.match(yaplParser.SEMICOLON)
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClasssContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(yaplParser.CLASS, 0)

        def TYPE_IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.TYPE_IDENTIFIER)
            else:
                return self.getToken(yaplParser.TYPE_IDENTIFIER, i)

        def LBRACE(self):
            return self.getToken(yaplParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(yaplParser.RBRACE, 0)

        def INHERITS(self):
            return self.getToken(yaplParser.INHERITS, 0)

        def feature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.FeatureContext)
            else:
                return self.getTypedRuleContext(yaplParser.FeatureContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.SEMICOLON)
            else:
                return self.getToken(yaplParser.SEMICOLON, i)

        def getRuleIndex(self):
            return yaplParser.RULE_classs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClasss" ):
                listener.enterClasss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClasss" ):
                listener.exitClasss(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasss" ):
                return visitor.visitClasss(self)
            else:
                return visitor.visitChildren(self)




    def classs(self):

        localctx = yaplParser.ClasssContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(yaplParser.CLASS)
            self.state = 20
            self.match(yaplParser.TYPE_IDENTIFIER)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 21
                self.match(yaplParser.INHERITS)
                self.state = 22
                self.match(yaplParser.TYPE_IDENTIFIER)


            self.state = 25
            self.match(yaplParser.LBRACE)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 26
                self.feature()
                self.state = 27
                self.match(yaplParser.SEMICOLON)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(yaplParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typescriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return yaplParser.RULE_var_typescript

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AttributesDeclarationContext(Var_typescriptContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.Var_typescriptContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)
        def COLON(self):
            return self.getToken(yaplParser.COLON, 0)
        def TYPE_IDENTIFIER(self):
            return self.getToken(yaplParser.TYPE_IDENTIFIER, 0)
        def ASSIGN(self):
            return self.getToken(yaplParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributesDeclaration" ):
                listener.enterAttributesDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributesDeclaration" ):
                listener.exitAttributesDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributesDeclaration" ):
                return visitor.visitAttributesDeclaration(self)
            else:
                return visitor.visitChildren(self)



    def var_typescript(self):

        localctx = yaplParser.Var_typescriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_typescript)
        self._la = 0 # Token type
        try:
            localctx = yaplParser.AttributesDeclarationContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(yaplParser.ID_VAR)
            self.state = 37
            self.match(yaplParser.COLON)
            self.state = 38
            self.match(yaplParser.TYPE_IDENTIFIER)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 39
                self.match(yaplParser.ASSIGN)
                self.state = 40
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return yaplParser.RULE_feature

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MethodDefContext(FeatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.FeatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)
        def LPAREN(self):
            return self.getToken(yaplParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(yaplParser.RPAREN, 0)
        def COLON(self):
            return self.getToken(yaplParser.COLON, 0)
        def TYPE_IDENTIFIER(self):
            return self.getToken(yaplParser.TYPE_IDENTIFIER, 0)
        def LBRACE(self):
            return self.getToken(yaplParser.LBRACE, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)

        def RBRACE(self):
            return self.getToken(yaplParser.RBRACE, 0)
        def formal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.FormalContext)
            else:
                return self.getTypedRuleContext(yaplParser.FormalContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.COMMA)
            else:
                return self.getToken(yaplParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDef" ):
                listener.enterMethodDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDef" ):
                listener.exitMethodDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDef" ):
                return visitor.visitMethodDef(self)
            else:
                return visitor.visitChildren(self)


    class AttrContext(FeatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.FeatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)
        def COLON(self):
            return self.getToken(yaplParser.COLON, 0)
        def TYPE_IDENTIFIER(self):
            return self.getToken(yaplParser.TYPE_IDENTIFIER, 0)
        def ASSIGN(self):
            return self.getToken(yaplParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr" ):
                listener.enterAttr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr" ):
                listener.exitAttr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr" ):
                return visitor.visitAttr(self)
            else:
                return visitor.visitChildren(self)



    def feature(self):

        localctx = yaplParser.FeatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_feature)
        self._la = 0 # Token type
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = yaplParser.MethodDefContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(yaplParser.ID_VAR)
                self.state = 44
                self.match(yaplParser.LPAREN)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 45
                    self.formal()
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==25:
                        self.state = 46
                        self.match(yaplParser.COMMA)
                        self.state = 47
                        self.formal()
                        self.state = 52
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 58
                self.match(yaplParser.RPAREN)
                self.state = 59
                self.match(yaplParser.COLON)
                self.state = 60
                self.match(yaplParser.TYPE_IDENTIFIER)
                self.state = 61
                self.match(yaplParser.LBRACE)
                self.state = 62
                self.expr(0)
                self.state = 63
                self.match(yaplParser.RBRACE)
                pass

            elif la_ == 2:
                localctx = yaplParser.AttrContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(yaplParser.ID_VAR)
                self.state = 66
                self.match(yaplParser.COLON)
                self.state = 67
                self.match(yaplParser.TYPE_IDENTIFIER)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 68
                    self.match(yaplParser.ASSIGN)
                    self.state = 69
                    self.expr(0)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)

        def COLON(self):
            return self.getToken(yaplParser.COLON, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(yaplParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return yaplParser.RULE_formal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal" ):
                listener.enterFormal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal" ):
                listener.exitFormal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormal" ):
                return visitor.visitFormal(self)
            else:
                return visitor.visitChildren(self)




    def formal(self):

        localctx = yaplParser.FormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_formal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(yaplParser.ID_VAR)
            self.state = 75
            self.match(yaplParser.COLON)
            self.state = 76
            self.match(yaplParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return yaplParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NewContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(yaplParser.NEW, 0)
        def TYPE_IDENTIFIER(self):
            return self.getToken(yaplParser.TYPE_IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNew" ):
                listener.enterNew(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNew" ):
                listener.exitNew(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNew" ):
                return visitor.visitNew(self)
            else:
                return visitor.visitChildren(self)


    class MinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def MINUS(self):
            return self.getToken(yaplParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinus" ):
                listener.enterMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinus" ):
                listener.exitMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinus" ):
                return visitor.visitMinus(self)
            else:
                return visitor.visitChildren(self)


    class MultContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def MULT(self):
            return self.getToken(yaplParser.MULT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMult" ):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STR_VAR(self):
            return self.getToken(yaplParser.STR_VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class IsvoidContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ISVOID(self):
            return self.getToken(yaplParser.ISVOID, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsvoid" ):
                listener.enterIsvoid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsvoid" ):
                listener.exitIsvoid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsvoid" ):
                return visitor.visitIsvoid(self)
            else:
                return visitor.visitChildren(self)


    class FalseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(yaplParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalse" ):
                listener.enterFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalse" ):
                listener.exitFalse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalse" ):
                return visitor.visitFalse(self)
            else:
                return visitor.visitChildren(self)


    class IntegerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_VAR(self):
            return self.getToken(yaplParser.INT_VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class LessContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def LESS_THAN(self):
            return self.getToken(yaplParser.LESS_THAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLess" ):
                listener.enterLess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLess" ):
                listener.exitLess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLess" ):
                return visitor.visitLess(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(yaplParser.WHILE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def LOOP(self):
            return self.getToken(yaplParser.LOOP, 0)
        def POOL(self):
            return self.getToken(yaplParser.POOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class PlusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(yaplParser.PLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlus" ):
                listener.enterPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlus" ):
                listener.exitPlus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlus" ):
                return visitor.visitPlus(self)
            else:
                return visitor.visitChildren(self)


    class DivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def DIV(self):
            return self.getToken(yaplParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class EqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def EQUAL(self):
            return self.getToken(yaplParser.EQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)


    class NegativeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEGATIVE(self):
            return self.getToken(yaplParser.NEGATIVE, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegative" ):
                listener.enterNegative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegative" ):
                listener.exitNegative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegative" ):
                return visitor.visitNegative(self)
            else:
                return visitor.visitChildren(self)


    class NotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(yaplParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class ParenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(yaplParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(yaplParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen" ):
                listener.enterParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen" ):
                listener.exitParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)


    class TrueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(yaplParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrue" ):
                listener.enterTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrue" ):
                listener.exitTrue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrue" ):
                return visitor.visitTrue(self)
            else:
                return visitor.visitChildren(self)


    class BlockContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACE(self):
            return self.getToken(yaplParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(yaplParser.RBRACE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.SEMICOLON)
            else:
                return self.getToken(yaplParser.SEMICOLON, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)


    class LetContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(yaplParser.LET, 0)
        def var_typescript(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.Var_typescriptContext)
            else:
                return self.getTypedRuleContext(yaplParser.Var_typescriptContext,i)

        def IN(self):
            return self.getToken(yaplParser.IN, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.COMMA)
            else:
                return self.getToken(yaplParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet" ):
                listener.enterLet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet" ):
                listener.exitLet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet" ):
                return visitor.visitLet(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)
        def LPAREN(self):
            return self.getToken(yaplParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(yaplParser.RPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.COMMA)
            else:
                return self.getToken(yaplParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(yaplParser.IF, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def THEN(self):
            return self.getToken(yaplParser.THEN, 0)
        def ELSE(self):
            return self.getToken(yaplParser.ELSE, 0)
        def FI(self):
            return self.getToken(yaplParser.FI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class Less_equalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def LESS_EQUAL(self):
            return self.getToken(yaplParser.LESS_EQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLess_equal" ):
                listener.enterLess_equal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLess_equal" ):
                listener.exitLess_equal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLess_equal" ):
                return visitor.visitLess_equal(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)
        def ASSIGN(self):
            return self.getToken(yaplParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(yaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class MethodCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a yaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(yaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(yaplParser.ExprContext,i)

        def PERIOD(self):
            return self.getToken(yaplParser.PERIOD, 0)
        def ID_VAR(self):
            return self.getToken(yaplParser.ID_VAR, 0)
        def LPAREN(self):
            return self.getToken(yaplParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(yaplParser.RPAREN, 0)
        def AT(self):
            return self.getToken(yaplParser.AT, 0)
        def TYPE_IDENTIFIER(self):
            return self.getToken(yaplParser.TYPE_IDENTIFIER, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(yaplParser.COMMA)
            else:
                return self.getToken(yaplParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCall" ):
                listener.enterMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCall" ):
                listener.exitMethodCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = yaplParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = yaplParser.FunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 79
                self.match(yaplParser.ID_VAR)
                self.state = 80
                self.match(yaplParser.LPAREN)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 96757160212624) != 0):
                    self.state = 81
                    self.expr(0)
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==25:
                        self.state = 82
                        self.match(yaplParser.COMMA)
                        self.state = 83
                        self.expr(0)
                        self.state = 88
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 94
                self.match(yaplParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = yaplParser.IfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 95
                self.match(yaplParser.IF)
                self.state = 96
                self.expr(0)
                self.state = 97
                self.match(yaplParser.THEN)
                self.state = 98
                self.expr(0)
                self.state = 99
                self.match(yaplParser.ELSE)
                self.state = 100
                self.expr(0)
                self.state = 101
                self.match(yaplParser.FI)
                pass

            elif la_ == 3:
                localctx = yaplParser.WhileContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 103
                self.match(yaplParser.WHILE)
                self.state = 104
                self.expr(0)
                self.state = 105
                self.match(yaplParser.LOOP)
                self.state = 106
                self.expr(0)
                self.state = 107
                self.match(yaplParser.POOL)
                pass

            elif la_ == 4:
                localctx = yaplParser.BlockContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                self.match(yaplParser.LBRACE)
                self.state = 113 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 110
                    self.expr(0)
                    self.state = 111
                    self.match(yaplParser.SEMICOLON)
                    self.state = 115 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 96757160212624) != 0)):
                        break

                self.state = 117
                self.match(yaplParser.RBRACE)
                pass

            elif la_ == 5:
                localctx = yaplParser.LetContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.match(yaplParser.LET)
                self.state = 120
                self.var_typescript()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 121
                    self.match(yaplParser.COMMA)
                    self.state = 122
                    self.var_typescript()
                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 128
                self.match(yaplParser.IN)
                self.state = 129
                self.expr(19)
                pass

            elif la_ == 6:
                localctx = yaplParser.NewContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 131
                self.match(yaplParser.NEW)
                self.state = 132
                self.match(yaplParser.TYPE_IDENTIFIER)
                pass

            elif la_ == 7:
                localctx = yaplParser.NegativeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133
                self.match(yaplParser.NEGATIVE)
                self.state = 134
                self.expr(17)
                pass

            elif la_ == 8:
                localctx = yaplParser.IsvoidContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.match(yaplParser.ISVOID)
                self.state = 136
                self.expr(16)
                pass

            elif la_ == 9:
                localctx = yaplParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.match(yaplParser.NOT)
                self.state = 138
                self.expr(8)
                pass

            elif la_ == 10:
                localctx = yaplParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 139
                self.match(yaplParser.LPAREN)
                self.state = 140
                self.expr(0)
                self.state = 141
                self.match(yaplParser.RPAREN)
                pass

            elif la_ == 11:
                localctx = yaplParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 143
                self.match(yaplParser.ID_VAR)
                pass

            elif la_ == 12:
                localctx = yaplParser.IntegerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.match(yaplParser.INT_VAR)
                pass

            elif la_ == 13:
                localctx = yaplParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 145
                self.match(yaplParser.STR_VAR)
                pass

            elif la_ == 14:
                localctx = yaplParser.TrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(yaplParser.TRUE)
                pass

            elif la_ == 15:
                localctx = yaplParser.FalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 147
                self.match(yaplParser.FALSE)
                pass

            elif la_ == 16:
                localctx = yaplParser.AssignContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(yaplParser.ID_VAR)
                self.state = 149
                self.match(yaplParser.ASSIGN)
                self.state = 150
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 198
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 196
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = yaplParser.MultContext(self, yaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 153
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 154
                        self.match(yaplParser.MULT)
                        self.state = 155
                        self.expr(16)
                        pass

                    elif la_ == 2:
                        localctx = yaplParser.DivContext(self, yaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 156
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 157
                        self.match(yaplParser.DIV)
                        self.state = 158
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = yaplParser.PlusContext(self, yaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 159
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 160
                        self.match(yaplParser.PLUS)
                        self.state = 161
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = yaplParser.MinusContext(self, yaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 162
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 163
                        self.match(yaplParser.MINUS)
                        self.state = 164
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = yaplParser.Less_equalContext(self, yaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 165
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 166
                        self.match(yaplParser.LESS_EQUAL)
                        self.state = 167
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = yaplParser.LessContext(self, yaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 168
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 169
                        self.match(yaplParser.LESS_THAN)
                        self.state = 170
                        self.expr(11)
                        pass

                    elif la_ == 7:
                        localctx = yaplParser.EqualContext(self, yaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 171
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 172
                        self.match(yaplParser.EQUAL)
                        self.state = 173
                        self.expr(10)
                        pass

                    elif la_ == 8:
                        localctx = yaplParser.MethodCallContext(self, yaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 174
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 177
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==28:
                            self.state = 175
                            self.match(yaplParser.AT)
                            self.state = 176
                            self.match(yaplParser.TYPE_IDENTIFIER)


                        self.state = 179
                        self.match(yaplParser.PERIOD)
                        self.state = 180
                        self.match(yaplParser.ID_VAR)
                        self.state = 181
                        self.match(yaplParser.LPAREN)
                        self.state = 192
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & 96757160212624) != 0):
                            self.state = 182
                            self.expr(0)
                            self.state = 187
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==25:
                                self.state = 183
                                self.match(yaplParser.COMMA)
                                self.state = 184
                                self.expr(0)
                                self.state = 189
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)

                            self.state = 194
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 195
                        self.match(yaplParser.RPAREN)
                        pass

             
                self.state = 200
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 23)
         




