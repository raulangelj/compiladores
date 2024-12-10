from yapl.grammar.yaplVisitor import yaplVisitor
from yapl.grammar.yaplParser import yaplParser
from yapl.custom.Nodes import *

class YaplVisitorCustom(yaplVisitor):
    def __init__(self):
        self.errors = []
    # custom visits
    def visitInteger(self, ctx:yaplParser.IntegerContext):
        return IntegerNode(ctx.INT_VAR().getText())
    
    def visitString(self, ctx:yaplParser.StringContext):
        return StringNode(ctx.STR_VAR().getText())

    def visitPlus(self, ctx:yaplParser.PlusContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._getError(left, right, '+')
        return PlusNode(left, right)
    
    def visitMinus(self, ctx:yaplParser.MinusContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._getError(left, right, '-')
        return MinusNode(left, right)
    
    def visitMult(self, ctx:yaplParser.MultContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._getError(left, right, '*')
        return MultNode(left, right)
    
    def visitDiv(self, ctx: yaplParser.DivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._getError(left, right, '/')
        return DivNode(left, right)

    def visitTrue(self, ctx: yaplParser.TrueContext):
        return BooleanNode(ctx.TRUE().getText())
    
    def visitFalse(self, ctx: yaplParser.FalseContext):
        return BooleanNode(ctx.FALSE().getText())
    
    def visitLess(self, ctx: yaplParser.LessContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._getError(left, right, '<')
        return LessThanNode(left, right)
    
    def visitLess_equal(self, ctx: yaplParser.Less_equalContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._getError(left, right, '<=')
        return LessEqualNode(left, right)
    
    def visitEqual(self, ctx: yaplParser.EqualContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._getError(left, right, '=')
        return EqualNode(left, right)
    
    def visitNot(self, ctx: yaplParser.NotContext):
        node = self.visit(ctx.expr())
        self._getError(node, None, 'Not')
        return NotNode(node)
    
    def visitNegative(self, ctx: yaplParser.NegativeContext):
        node = self.visit(ctx.expr())
        print(node.type)
        self._getError(node, None, 'Negative')
        return NegativeNode(node)
    
    def _arithmeticErros(self, left, right, operator):
        error = ErrorNode()
        if left.type != 'Integer' or right.type != 'Integer':
            error.get_error(left, right, operator)
            self.errors.append(error)

    def _comparisonErrors(self, left, right, operator):
        error = ErrorNode()
        if left.type != right.type:
            error.get_error(left, right, operator)
            self.errors.append(error)
    
    def _getError(self, left, right, operator):
        match operator:
            case '+':
                self._arithmeticErros(left, right, operator)
            case '-':
                self._arithmeticErros(left, right, operator)
            case '*':
                self._arithmeticErros(left, right, operator)
            case '/':
                self._arithmeticErros(left, right, operator)
            case '<':
                self._comparisonErrors(left, right, operator)
            case '<=':
                self._comparisonErrors(left, right, operator)
            case '=':
                self._comparisonErrors(left, right, operator)
            case 'Not':
                # key 'not'
                if left.type != 'Boolean':
                    error = ErrorNode()
                    error.message = f"Unsupported operation {operator}: with {left.type}"
                    self.errors.append(error)
            case 'Negative':
                # key '~'
                if left.type == 'String':
                    error = ErrorNode()
                    error.message = f"Unsupported operation {operator}: with {left.type}"
                    self.errors.append(error)
            case _:
                pass
            