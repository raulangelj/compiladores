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
        nodo = IntegerNode(ctx.INT_VAR().getText())
        nodo.line = ctx.INT_VAR().symbol.line
        return nodo
    
    def visitString(self, ctx:yaplParser.StringContext):
        nodo = StringNode(ctx.STR_VAR().getText())
        nodo.line = ctx.STR_VAR().symbol.line
        return nodo

    def visitPlus(self, ctx:yaplParser.PlusContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._getError(left, right, '+')
        nodo = PlusNode(left, right)
        nodo.line = ctx.PLUS().symbol.line
        nodo.token = '+'
        return nodo
    
    def visitMinus(self, ctx:yaplParser.MinusContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._getError(left, right, '-')
        nodo = MinusNode(left, right)
        nodo.line = ctx.MINUS().symbol.line
        nodo.token = '-'
        return nodo
    
    def visitMult(self, ctx:yaplParser.MultContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._getError(left, right, '*')
        node = MultNode(left, right)
        node.line = ctx.MULT().symbol.line
        node.token = '*'
        return node
    
    def visitDiv(self, ctx: yaplParser.DivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._getError(left, right, '/')
        nodo = DivNode(left, right)
        nodo.line = ctx.DIV().symbol.line
        nodo.token = '/'
        return nodo

    def visitTrue(self, ctx: yaplParser.TrueContext):
        nodo = BooleanNode(ctx.TRUE().getText())
        nodo.line = ctx.TRUE().symbol.line
        return nodo
    
    def visitFalse(self, ctx: yaplParser.FalseContext):
        nodo = BooleanNode(ctx.FALSE().getText())
        nodo.line = ctx.FALSE().symbol.line
        return nodo
    
    def visitLess(self, ctx: yaplParser.LessContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._getError(left, right, '<')
        nodo = LessThanNode(left, right)
        nodo.line = ctx.LESS_THAN().symbol.line
        nodo.token =  ctx.LESS_THAN().getText()
        return nodo
    
    def visitLess_equal(self, ctx: yaplParser.Less_equalContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._getError(left, right, '<=')
        nodo = LessEqualNode(left, right)
        nodo.line = ctx.LESS_EQUAL().symbol.line
        nodo.token = ctx.LESS_EQUAL().getText()
        return nodo
    
    def visitEqual(self, ctx: yaplParser.EqualContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._getError(left, right, '=')
        nodo = EqualNode(left, right)
        nodo.line = ctx.EQUAL().symbol.line
        nodo.token = ctx.EQUAL().getText()
        return nodo
    
    def visitNot(self, ctx: yaplParser.NotContext):
        node = self.visit(ctx.expr())
        self._getError(node, None, 'Not')
        nodo = NotNode(node)
        nodo.line = ctx.NOT().symbol.line
        return nodo
    
    def visitNegative(self, ctx: yaplParser.NegativeContext):
        node = self.visit(ctx.expr())
        self._getError(node, None, 'Negative')
        nodo = NegativeNode(node)
        nodo.line = ctx.NEGATIVE().symbol.line
        return nodo
    
    def visitId(self, ctx:yaplParser.IdContext):
        node = IdNode(ctx.ID_VAR().getText())
        node.line = ctx.ID_VAR().symbol.line
        return node
    
    def visitAssign(self, ctx:yaplParser.AssignContext):
        idx = ctx.ID_VAR().getText()
        expression = self.visit(ctx.expr())
        nodo = AssignNode(idx, expression)
        nodo.line = ctx.ASSIGN().symbol.line
        nodo.type = expression.type
        return nodo
    
    def visitBlock(self, ctx:yaplParser.BlockContext):
        body_list = [self.visit(expr) for expr in ctx.expr()]
        nodo = BlockNode(body_list)
        nodo.line = ctx.LBRACE().symbol.line
        # TODO falta el type
        return nodo
    
    def visitMethodDef(self, ctx:yaplParser.MethodDefContext):
        name = ctx.ID_VAR().getText()
        # params = [self.visit(ctx.formal(i)) for i in range(len(ctx.formal()))]
        params = []
        for i in range(len(ctx.formal())):
            idx = ctx.formal(i).ID_VAR().getText()
            typex = ctx.formal(i).TYPE_IDENTIFIER().getText()
            params.append(Attribute(idx, typex))
        typex = ctx.TYPE_IDENTIFIER().getText()
        body = self.visit(ctx.expr())
        nodo = MethodNode(name, params, typex, body)
        nodo.line = ctx.ID_VAR().symbol.line
        # TODO falta el type
        return nodo
    
    def visitClasss(self, ctx:yaplParser.ClasssContext):
        name = ctx.TYPE_IDENTIFIER(0).getText()
        parent = ctx.TYPE_IDENTIFIER(1).getText() if ctx.TYPE_IDENTIFIER(1) is not None else None
        feature = [self.visit(ctx.feature(i)) for i in range(len(ctx.feature()))]
        scope = { 'class_name': name, 'method_name': None }
        methods = [f for f in feature if isinstance(f, MethodNode)]
        for f in feature:
            self._addSimbolToTable(scope, f)
        nodo = ClassNode(name, parent, feature)
        nodo.line = ctx.CLASS().symbol.line
        # * add class to table
        self.types.append(Klass(name, None, 'class', parent, None, nodo))
        # * add methods to table
        for m in methods:
            self.types[-1].define_method(m.name, m.return_type, m.params)
        # TODO falta el type
        return nodo

    def visitAttr(self, ctx:yaplParser.AttrContext):
        idx = ctx.ID_VAR().getText()
        typex = ctx.TYPE_IDENTIFIER().getText()
        expression = self.visit(ctx.expr()) if ctx.expr() is not None else None
        nodo = AttrNode(idx, typex, expression)
        nodo.line = ctx.ID_VAR().symbol.line
        if nodo.value:
            # * CHECK if expression is same type
            if typex != nodo.value.type:
                error = ErrorNode()
                error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Cannot assign {expression.type} to {typex}"
                self.errors.append(error)
        return nodo
    
    def show_classes_table(self):
        headers = ['Name' , 'Parent', 'Attributes', 'Methods']
        table = [
            [t.name, t.inheritance, t.get_attributes_names(), t.get_methods_names()]
            for t in self.types
            if t.type == 'class'
        ]
        print("\n========== Classes Table ==========\n")
        print(tabulate(table, headers, tablefmt="fancy_grid"))
    
    def show_variables_table(self):
        headers = ['Name', 'Type', 'Scope', 'Value']
        table = []
        for t in self.types:
            if t.type == 'var':
                scope = t.scope['class_name'] if t.scope['method_name'] is None else f'{t.scope["class_name"]} => {t.scope["method_name"]}'
                table.append([t.name, t.inheritance, scope, t.value])
        print("\n========== Variables Table ==========\n")
        print(tabulate(table, headers, tablefmt="fancy_grid"))

    def check_global_semantics(self):
        # * CHECK if main class is defined
        if not self._is_defined('Main', None):
            self._add_error(
                "ERROR: Main class is not defined"
            )
        # * CHECK if main method is defined
        main_class = [t for t in self.types if t.name == 'Main' and t.type == 'class']
        if main_class:
            main_class = main_class[0]
        if not main_class or not main_class.getMethod('main'):
            self._add_error(
                "ERROR: Main method is not defined"
            )
            return
        # * CHECK if main method has no params
        if len(main_class.getMethod('main').params) > 0:
            self._add_error(
                "ERROR: Main method must have no params"
            )
            return
        # * CHECK if main method has no return type
        if main_class.getMethod('main').return_type != 'SELF_TYPE':
            self._add_error(
                "ERROR: Main method must have no return type"
            )
            return

    # TODO Rename this here and in `check_global_semantics`
    def _add_error(self, message: str):
        error = ErrorNode()
        error.message = message
        self.errors.append(error)

    def _is_defined(self, name: str, scope: ScopeType) -> bool:
        return any(t.name == name and t.scope == scope for t in self.types)
    
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
            # * CHECK if variable is defined
            if not self._is_defined(node.idx, scope):
                error = ErrorNode()
                error.message = f"ERROR on line {node.line}: Variable {node.idx} is not defined"
                self.errors.append(error)
            else:
                # assign the value in the simbols table
                for t in self.types:
                    if t.name == node.idx and t.scope == scope:
                        # * CHECK if expression is same type
                        if t.inheritance != node.value.type:
                            error = ErrorNode()
                            error.message = f"ERROR on line {node.line}:Cannot assign {node.value.type} to {t.inheritance}"
                            self.errors.append(error)
                        t.value = node.value.token
                        break
    
    def _arithmeticErros(self, left, right, operator):
        error = ErrorNode()
        # show error if left or right is not Int type but if is Id let it pass
        if left.type not in ['Int', 'Id'] or right.type not in ['Int', 'Id']:
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
                if left.type not in ['Bool', 'Id']:
                    self._extracted_from__getError_20(operator, left)
            case 'Negative':
                # key '~'
                if left.type == 'String':
                    self._extracted_from__getError_20(operator, left)
            case _:
                pass

    # TODO Rename this here and in `_getError`
    def _extracted_from__getError_20(self, operator, left):
        error = ErrorNode()
        error.message = f"Unsupported operation {operator}: with {left.type}"
        self.errors.append(error)
            