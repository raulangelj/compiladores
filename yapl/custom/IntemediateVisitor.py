from yapl.grammar.yaplVisitor import yaplVisitor
from yapl.grammar.yaplParser import yaplParser
from tabulate import tabulate
from yapl.custom.models.Nodes import *
from yapl.custom.intermediate.IntermediateClass import *
from yapl.custom.models.Types import *

class IntermediateVisitor(yaplVisitor):
    def __init__(self):
        self.intermediate: dict[str, IntermediateClass] = {}
        self.types: dict[str, Klass] = {}
        self.actual_temp = 0
        self.actual_label = 0
        self.active_scope: ScopeType = {
            'class_name': None,
            'method_name': None,
            'level': 0
        }

    def generate(self, left: str, right: str, op: str = None, type: str = 'Quadruple') -> Quadruple:
        if type == 'If':
            self.actual_label += 1
            return Quadruple(op, left, right, f'L{self.actual_label}', type)
        if type == 'Goto':
            return Quadruple(op, left, right, f'L{self.actual_label}', type)
        self.actual_temp += 1
        return Quadruple(op, left, right, f't{self.actual_temp}', type)
    
    def generate_label(self) -> Quadruple:
        self.actual_label += 1
        return Quadruple(None, None, None, f'L{self.actual_label}', 'Label')
    
    def get_active_label(self) -> str:
        return f'L{self.actual_label}'
    
    def store_attribute(self, name: str, value: str, type: str = 'Quadruple') -> Quadruple:
        return Quadruple('=', value, None, name, type)
    
    def get_active_temp(self) -> str:
        return f't{self.actual_temp}'
    
    def print_intermediate(self):
        for c in self.intermediate:
            print(c)
            # Print attributes
            for m in self.intermediate[c].attributes:
                print(f'\t{m}')
            # Print methods
            for m in self.intermediate[c].methods:
                print(f'\t{m}')
                for q in self.intermediate[c].methods[m]:
                    print(f'\t\t{q}')

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
        nodo = PlusNode(left, right)
        nodo.line = ctx.PLUS().symbol.line
        nodo.token = f'{ctx.expr(0).getText()}+{ctx.expr(1).getText()}'
        nodo.type = 'Int'
        # * Generate intermediate code
        new_right = (
            right.token
            if isinstance(right, (IntegerNode, IdNode))
            else self.get_active_temp()
        )
        new_left = (
            left.token
            if isinstance(left, (IntegerNode, IdNode))
            else self.get_active_temp()
        )
        if self.active_scope['method_name']:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(new_left, new_right, '+'))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(new_left, new_right, '+'))
        return nodo
    
    def visitMinus(self, ctx:yaplParser.MinusContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        nodo = MinusNode(left, right)
        nodo.line = ctx.MINUS().symbol.line
        nodo.token = f'{ctx.expr(0).getText()}-{ctx.expr(1).getText()}'
        nodo.type = 'Int'
        # * Generate intermediate code
        new_right = (
            right.token
            if isinstance(right, (IntegerNode, IdNode))
            else self.get_active_temp()
        )
        new_left = (
            left.token
            if isinstance(left, (IntegerNode, IdNode))
            else self.get_active_temp()
        )
        if self.active_scope['method_name']:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(new_left, new_right, '-'))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(new_left, new_right, '-'))
        return nodo
    
    def visitMult(self, ctx:yaplParser.MultContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        node = MultNode(left, right)
        node.line = ctx.MULT().symbol.line
        node.token = f'{ctx.expr(0).getText()}*{ctx.expr(1).getText()}'
        node.type = 'Int'
        # * Generate intermediate code
        new_right = (
            right.token
            if isinstance(right, (IntegerNode, IdNode))
            else self.get_active_temp()
        )
        new_left = (
            left.token
            if isinstance(left, (IntegerNode, IdNode))
            else self.get_active_temp()
        )
        if self.active_scope['method_name']:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(new_left, new_right, '*'))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(new_left, new_right, '*'))
        return node
    
    def visitDiv(self, ctx: yaplParser.DivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        nodo = DivNode(left, right)
        nodo.line = ctx.DIV().symbol.line
        nodo.token = f'{ctx.expr(0).getText()}/{ctx.expr(1).getText()}'
        nodo.type = 'Int'
        # * Generate intermediate code
        new_right = (
            right.token
            if isinstance(right, (IntegerNode, IdNode))
            else self.get_active_temp()
        )
        new_left = (
            left.token
            if isinstance(left, (IntegerNode, IdNode))
            else self.get_active_temp()
        )
        if self.active_scope['method_name']:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(new_left, new_right, '/'))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(new_left, new_right, '/'))
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
        nodo = LessThanNode(left, right)
        nodo.line = ctx.LESS_THAN().symbol.line
        nodo.token =  f'{ctx.expr(0).getText()}<{ctx.expr(1).getText()}'
        nodo.type = 'Bool'
        # * Generate intermediate code
        new_right = (
            right.token
            if isinstance(right, (IntegerNode, IdNode))
            else self.get_active_temp()
        )
        new_left = (
            left.token
            if isinstance(left, (IntegerNode, IdNode))
            else self.get_active_temp()
        )
        if self.active_scope['method_name']:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(new_left, new_right, '<'))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(new_left, new_right, '<'))
        return nodo
    
    def visitLess_equal(self, ctx: yaplParser.Less_equalContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        nodo = LessEqualNode(left, right)
        nodo.line = ctx.LESS_EQUAL().symbol.line
        nodo.token = f'{ctx.expr(0).getText()}<={ctx.expr(1).getText()}'
        nodo.type = 'Bool'
        return nodo
    
    def visitEqual(self, ctx: yaplParser.EqualContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        nodo = EqualNode(left, right)
        nodo.line = ctx.EQUAL().symbol.line
        nodo.token = f'{ctx.expr(0).getText()}={ctx.expr(1).getText()}'
        nodo.type = 'Bool'
        return nodo
    
    def visitNot(self, ctx: yaplParser.NotContext):
        node = self.visit(ctx.expr())
        nodo = NotNode(node)
        nodo.type = node.type
        nodo.line = ctx.NOT().symbol.line
        return nodo
    
    def visitNegative(self, ctx: yaplParser.NegativeContext):
        node = self.visit(ctx.expr())
        nodo = NegativeNode(node, f'{ctx.expr().getText()}')
        nodo.type = node.type
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
        # * Intermediate code
        if not expression or isinstance(expression, (IntegerNode, StringNode, BooleanNode)):
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.store_attribute(idx, expression.token, 'Assign'))
        else:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.store_attribute(idx, self.get_active_temp(), 'Assign'))
        return nodo
    
    def visitBlock(self, ctx:yaplParser.BlockContext):
        # body_list = [self.visit(expr) for expr in ctx.expr()]
        body_list =[]
        for expr in ctx.expr():
            body_list.append(self.visit(expr))
        nodo = BlockNode(body_list)
        nodo.line = ctx.LBRACE().symbol.line
        # nodo.type = self._get_super_type(body_list)
        nodo.type = body_list[-1].type
        return nodo
    
    def _get_super_type(self, features: Node = []):
        if len(features) == 0 or None in features:
            return 'Object'
        same_type = all(f.type == features[0].type for f in features)
        return features[0].type if same_type else 'Object'

    
    def visitWhile(self, ctx:yaplParser.WhileContext):
        condition = self.visit(ctx.expr(0))
        self.active_scope['level'] += 1
        expression = self.visit(ctx.expr(1))
        self.active_scope['level'] -= 1
        nodo = WhileNode(condition, expression)
        nodo.line = ctx.WHILE().symbol.line
        nodo.type = 'Object'
        # TODO REVISAR QUE FALTA
        return nodo
    
    def visitIf(self, ctx:yaplParser.IfContext):
        condition = self.visit(ctx.expr(0))
        self.active_scope['level'] += 1
        # * Generate intermediate code
        if_true = self.generate(self.get_active_temp(), None, f'Goto {self.get_active_label()}', 'If')
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(if_true)
        if_false = self.generate_label()
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(if_false.result, None, f'Goto {if_false.result}', 'Goto'))

        # * Generate intermediate code
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, _type='Label', result=if_true.result))
        then_body = self.visit(ctx.expr(1))
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, _type='Label', result=f'END_{if_true.result}'))
        self.active_scope['level'] += 1
        
        # * Generate intermediate code
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, _type='Label', result=if_false.result))
        else_body = self.visit(ctx.expr(2))
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, _type='Label', result=f'END_{if_false.result}'))
        self.active_scope['level'] -= 2
        nodo = IfNode(condition, then_body, else_body)
        nodo.line = ctx.IF().symbol.line
        nodo.type = self._get_super_type([then_body, else_body])
        # TODO REVISAR QUE FALTA

        return nodo
    
    def visitFunctionCall(self, ctx:yaplParser.FunctionCallContext):
        params = [self.visit(ctx.expr(i)) for i in range(len(ctx.expr()))]
        method = ctx.ID_VAR().getText()
        nodo = MethodCallNode('self', method, params)
        nodo.line = ctx.ID_VAR().symbol.line
        method_return = self.types[self.active_scope['class_name']].getMethod(method).return_type
        nodo.type = self.active_scope['class_name'] if method_return == 'SELF_TYPE' else method_return
        nodo.token = f'{method}({", ".join([p.token for p in params])})'
        method_params = self.types[self.active_scope['class_name']].getMethod(method).params
        # TODO REVISAR QUE FALTA
        return nodo
    
    def visitAttributesDeclaration(self, ctx:yaplParser.AttributesDeclarationContext):
        idx = ctx.ID_VAR().getText()
        typex = ctx.TYPE_IDENTIFIER().getText()
        expression = self.visit(ctx.expr()) if ctx.expr() is not None else None
        nodo = AttrNode(idx, typex, expression)
        nodo.line = ctx.ID_VAR().symbol.line
        return nodo
        
    def visitLet(self, ctx:yaplParser.LetContext):
        params = []
        for i in range(len(ctx.var_typescript())):
            p = self.visit(ctx.var_typescript(i))
            params.append(p)
        body = self.visit(ctx.expr())
        self._addSimbolToTable(self.active_scope, body)
        nodo = LetNode(params, body)
        nodo.line = ctx.LET().symbol.line
        nodo.type = self._get_super_type(list(params) + [body])
        return nodo
    
    def visitParen(self, ctx:yaplParser.ParenContext):
        return self.visit(ctx.expr())
    
    def visitIsvoid(self, ctx:yaplParser.IsvoidContext):
        expr = self.visit(ctx.expr())
        # value = self._check_for_use_id(expr)
        nodo = IsVoidNode(expr, 'false')
        nodo.line = ctx.ISVOID().symbol.line
        return nodo
    
    def _find_class_with_method(self, methdo: str):
        return next((c for c in self.types if self.types[c].getMethod(methdo)), None)
    
    def _find_return_type_of_method(self, method: str):
        return self.types[self._find_class_with_method(method)].getMethod(method).return_type
    
    def visitMethodCall(self, ctx:yaplParser.MethodCallContext):
        # myPet.say_hello();
        # myPet@Animal.say_hello();
        my_var = self.visit(ctx.expr(0))
        methodCall = ctx.ID_VAR().getText()
        args = [self.visit(ctx.expr(i)) for i in range(1, len(ctx.expr()))]
        parent = ctx.TYPE_IDENTIFIER().getText() if ctx.TYPE_IDENTIFIER() is not None else None
        nodo = DispatchNode(parent, methodCall, args, my_var, self._find_return_type_of_method(methodCall))
        nodo.line = ctx.ID_VAR().symbol.line
        # TODO REVISAR QUE FALTA
        return nodo        
    
    def visitMethodDef(self, ctx:yaplParser.MethodDefContext):
        name = ctx.ID_VAR().getText()
        self.active_scope['method_name'] = name
        # * Create the method for the intermediate code
        self.intermediate[self.active_scope['class_name']].add_method(name, [])
        params = []
        for i in range(len(ctx.formal())):
            param = ctx.formal(i)
            idx = param.ID_VAR().getText()
            typex = param.TYPE_IDENTIFIER().getText()
            params.append(Attribute(idx, typex))
        typex = ctx.TYPE_IDENTIFIER().getText()
        nodo = MethodNode(name, params, typex, None)
        # TODO REVISAR QUE FALTA y modificar el body
        body = self.visit(ctx.expr())
        nodo.body = body
        nodo.line = ctx.ID_VAR().symbol.line
        nodo.type = typex
        return nodo
    
    def visitClasss(self, ctx:yaplParser.ClasssContext):
        name = ctx.TYPE_IDENTIFIER(0).getText()
        parent = ctx.TYPE_IDENTIFIER(1).getText() if ctx.TYPE_IDENTIFIER(1) is not None else None
        feature = []
        # TODO REVISAR QUE FAKTA
        nodo = ClassNode(name, parent, feature)
        nodo.line = ctx.CLASS().symbol.line
        self.active_scope['class_name'] = name
        self.intermediate[name] = IntermediateClass(name)
        feature = []
        for i in range(len(ctx.feature())):
            f = self.visit(ctx.feature(i))
            feature.append(f)
        return nodo
    
    def visitNew(self, ctx:yaplParser.NewContext):
        typex = ctx.TYPE_IDENTIFIER().getText()
        nodo = NewNode(typex)
        nodo.line = ctx.NEW().symbol.line
        return nodo

    def visitAttr(self, ctx:yaplParser.AttrContext):
        idx = ctx.ID_VAR().getText()
        typex = ctx.TYPE_IDENTIFIER().getText()
        expression = self.visit(ctx.expr()) if ctx.expr() is not None else None
        nodo = AttrNode(idx, typex, expression)
        nodo.line = ctx.ID_VAR().symbol.line
        # * Intermediate code
        if not expression or isinstance(expression, (IntegerNode, StringNode, BooleanNode)):
            self.intermediate[self.active_scope['class_name']].attributes.append(self.store_attribute(idx, expression.token, 'Assign'))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.store_attribute(idx, self.get_active_temp(), 'Assign'))
        return nodo
            