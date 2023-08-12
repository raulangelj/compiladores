from yapl.grammar.yaplVisitor import yaplVisitor
from yapl.grammar.yaplParser import yaplParser
from tabulate import tabulate
from yapl.custom.models.Nodes import *
from yapl.custom.models.Types import *

class YaplVisitorCustom(yaplVisitor):
    def __init__(self):
        self.types: List[Klass] = []
        self.errors = []
        self._set_default_types()

    def _set_default_types(self):
        # Defaults types
        self.types.append(Klass('object', None))
        self.types.append(Klass('io', None))
        self.types.append(Klass('Int', None))
        self.types.append(Klass('String', None))
        self.types.append(Klass('Bool', None))
        # Defaults methods
        # object
        self.types[0].define_method('abort', 'object', [])
        self.types[0].define_method('type_name', 'String', [])
        self.types[0].define_method('copy', 'object', [])
        # io
        self.types[1].define_method('out_string', 'SELF_TYPE', [['x', 'String']])
        self.types[1].define_method('out_int', 'SELF_TYPE', [['x', 'Int']])
        self.types[1].define_method('in_string', 'String', [])
        self.types[1].define_method('in_int', 'Int', [])
        # integer
        # does not have methods - default value is 0
        # String - default value is ''
        self.types[3].define_method('length', 'Int', [])
        self.types[3].define_method('concat', 'String', [['s', 'String']])
        self.types[3].define_method('substr', 'String', [['i', 'Int'], ['l', 'Int']])
        # Bool - default value is false
        # does not have methods

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
        # print(node.type)
        self._getError(node, None, 'Negative')
        return NegativeNode(node)
    
    def visitAssign(self, ctx:yaplParser.AssignContext):
        idx = ctx.ID_VAR().getText()
        expression = self.visit(ctx.expr())
        return AssignNode(idx, expression)
    
    def visitBlock(self, ctx:yaplParser.BlockContext):
        body_list = [self.visit(expr) for expr in ctx.expr()]
        return BlockNode(body_list)
    
    def visitMethodDef(self, ctx:yaplParser.MethodDefContext):
        name = ctx.ID_VAR().getText()
        params = [self.visit(ctx.formal(i)) for i in range(len(ctx.formal()))]
        typex = ctx.TYPE_IDENTIFIER().getText()
        body = self.visit(ctx.expr())
        return MethodNode(name, typex, params, body)
    
    def visitClasss(self, ctx:yaplParser.ClasssContext):
        name = ctx.TYPE_IDENTIFIER(0).getText()
        parent = ctx.TYPE_IDENTIFIER(1).getText() if ctx.TYPE_IDENTIFIER(1) is not None else None
        feature = [self.visit(ctx.feature(i)) for i in range(len(ctx.feature()))]
        # print(name)
        # print(parent)
        # print(feature)
        scope = { 'class_name': name, 'method_name': None }
        print('------------------')
        for f in feature:
            self._addSimbolToTable(scope, f)
        return ClassNode(name, parent, feature)


    # def visitAttributesDeclaration(self, ctx:yaplParser.AttributesDeclarationContext):
    #     idx = ctx.ID_VAR().getText()
    #     typex = ctx.TYPE().getText()
    #     expression = self.visit(ctx.expr()) if ctx.expr() is not None else None
    #     print(expression)
    #     print(typex)
    #     print(idx)
    #     return AttributesDeclarationNode(idx, typex, expression)

    def visitAttr(self, ctx:yaplParser.AttrContext):
        idx = ctx.ID_VAR().getText()
        typex = ctx.TYPE_IDENTIFIER().getText()
        expression = self.visit(ctx.expr()) if ctx.expr() is not None else None
        # print(expression)
        # print(typex)
        # print(idx)
        return AttrNode(idx, typex, expression)
    
    def show_variables_table(self):
        headers = ['Name', 'Type', 'Scope', 'Value']
        table = []
        for t in self.types:
            if t.type == 'var':
                scope = t.scope['class_name'] if t.scope['method_name'] is None else f'{t.scope["class_name"]} => {t.scope["method_name"]}'
                table.append([t.name, t.inheritance, scope, t.value])
        print("\n========== Variables Table ==========\n")
        print(tabulate(table, headers, tablefmt="fancy_grid"))

    
    def _addSimbolToTable(self, scope: ScopeType, node: Node):
        # print(type (node))
        if isinstance(node, AttrNode):
            print('attr')
            self.types.append(Klass(node.idx, scope, 'var', node.type, node.value.token, node))
        elif isinstance(node, MethodNode):
            print('method')
            for s in node.body.statements:
                self._addSimbolToTable(scope, s)
        elif isinstance(node, AssignNode):
            print('assign')
            # assign the value in the simbols table
            for t in self.types:
                if t.name == node.idx and t.scope == scope:
                    t.value = node.value.token
                    break
    
    def _arithmeticErros(self, left, right, operator):
        error = ErrorNode()
        if left.type != 'Int' or right.type != 'Int':
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
                if left.type != 'Bool':
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
            