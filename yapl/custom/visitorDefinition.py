from yapl.grammar.yaplVisitor import yaplVisitor
from yapl.grammar.yaplParser import yaplParser
from tabulate import tabulate
from Constant import *
from yapl.custom.models.Nodes import *
from yapl.custom.models.Types import *

class VisitorDefinition(yaplVisitor):
    def __init__(self):
        # self.types: List[Klass] = []
        self.types: dict[str, Klass] = {}
        self.errors = []
        self._set_default_types()
        self.active_scope: ScopeType = { 'class_name': None, 'method_name': None, 'level': 0 }
        self.vars_used = set([])
        self.active_function_width = 0

    def _set_default_types(self):
        # Defaults types
        self.types['Object'] = Klass('Object', None)
        self.types['IO'] = Klass('IO', None, inheritance='Object')
        self.types['Int'] = Klass('Int', None, inheritance='Object', width=INT_SIZE)
        self.types['String'] = Klass('String', None, inheritance='Object') # with of 1 per char
        self.types['Bool'] = Klass('Bool', None, inheritance='Object', width=BOOL_SIZE)
        # Defaults methods
        # Object
        self.types['Object'].define_method('abort', 'Object', [], 0)
        self.types['Object'].define_method('type_name', 'String', [], 0)
        self.types['Object'].define_method('copy', 'Object', [], 0)
        # io
        self.types['IO'].define_method('out_string', 'SELF_TYPE', [Attribute('x', 'String', 1024 * CHAR_SIZE)], 1024 * CHAR_SIZE)
        self.types['IO'].define_method('out_int', 'SELF_TYPE', [Attribute('x', 'Int', INT_SIZE)], INT_SIZE)
        self.types['IO'].define_method('in_string', 'String', [], 1024* CHAR_SIZE)
        self.types['IO'].define_method('in_int', 'Int', [], INT_SIZE)
        # integer
        # does not have methods - default value is 0
        # String - default value is ''
        self.types['String'].define_method('length', 'Int', [], 1024 + CHAR_SIZE)
        self.types['String'].define_method('concat', 'String', [Attribute('s', 'String', 1024 * CHAR_SIZE)], 1024 + CHAR_SIZE)
        self.types['String'].define_method('substr', 'String', [Attribute('i', 'Int', INT_SIZE), Attribute('l', 'Int', INT_SIZE)], 1024 + CHAR_SIZE + 2 * INT_SIZE)
        # Bool - default value is false
        # does not have methods
        # add methods from parent to table
        for t in self.types:
            parent = self.types[t].inheritance
            if parent and parent in self.types:
                for method in self.types[parent].methods:
                    self.types[t].define_method(method, self.types[parent].methods[method].return_type, self.types[parent].methods[method].params)


    # custom visits
    def visitInteger(self, ctx:yaplParser.IntegerContext):
        nodo = IntegerNode(ctx.INT_VAR().getText())
        nodo.line = ctx.INT_VAR().symbol.line
        # sumar width de la funcion
        # self.active_function_width += INT_SIZE
        return nodo
    
    def visitString(self, ctx:yaplParser.StringContext):
        nodo = StringNode(ctx.STR_VAR().getText())
        nodo.line = ctx.STR_VAR().symbol.line
        # sumar width de la funcion
        # self.active_function_width += CHAR_SIZE * len(nodo.token)
        return nodo

    def visitPlus(self, ctx:yaplParser.PlusContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # if left.type == 'Id':
        #     self.vars_used.add(left.token)
        # if right.type == 'Id':
        #     self.vars_used.add(right.token)
        nodo = PlusNode(left, right)
        nodo.line = ctx.PLUS().symbol.line
        nodo.token = f'{ctx.expr(0).getText()}+{ctx.expr(1).getText()}'
        nodo.type = 'Int'
        return nodo
    
    def visitMinus(self, ctx:yaplParser.MinusContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # if left.type == 'Id':
        #     self.vars_used.add(left.token)
        # if right.type == 'Id':
        #     self.vars_used.add(right.token)
        nodo = MinusNode(left, right)
        nodo.line = ctx.MINUS().symbol.line
        nodo.token = f'{ctx.expr(0).getText()}-{ctx.expr(1).getText()}'
        nodo.type = 'Int'
        return nodo
    
    def visitMult(self, ctx:yaplParser.MultContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # if left.type == 'Id':
        #     self.vars_used.add(left.token)
        # if right.type == 'Id':
        #     self.vars_used.add(right.token)
        node = MultNode(left, right)
        node.line = ctx.MULT().symbol.line
        node.token = f'{ctx.expr(0).getText()}*{ctx.expr(1).getText()}'
        node.type = 'Int'
        return node
    
    def visitDiv(self, ctx: yaplParser.DivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # if left.type == 'Id':
        #     self.vars_used.add(left.token)
        # if right.type == 'Id':
        #     self.vars_used.add(right.token)
        nodo = DivNode(left, right)
        nodo.line = ctx.DIV().symbol.line
        nodo.token = f'{ctx.expr(0).getText()}/{ctx.expr(1).getText()}'
        nodo.type = 'Int'
        return nodo

    def visitTrue(self, ctx: yaplParser.TrueContext):
        nodo = BooleanNode(ctx.TRUE().getText())
        nodo.line = ctx.TRUE().symbol.line
        self.active_function_width += BOOL_SIZE
        return nodo
    
    def visitFalse(self, ctx: yaplParser.FalseContext):
        nodo = BooleanNode(ctx.FALSE().getText())
        nodo.line = ctx.FALSE().symbol.line
        self.active_function_width += BOOL_SIZE
        return nodo
    
    def visitLess(self, ctx: yaplParser.LessContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # if left.type == 'Id':
        #     self.vars_used.add(left.token)
        # if right.type == 'Id':
        #     self.vars_used.add(right.token)
        nodo = LessThanNode(left, right)
        nodo.line = ctx.LESS_THAN().symbol.line
        nodo.token =  f'{ctx.expr(0).getText()}<{ctx.expr(1).getText()}'
        nodo.type = 'Bool'
        return nodo
    
    def visitLess_equal(self, ctx: yaplParser.Less_equalContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # if left.type == 'Id':
        #     self.vars_used.add(left.token)
        # if right.type == 'Id':
        #     self.vars_used.add(right.token)
        nodo = LessEqualNode(left, right)
        nodo.line = ctx.LESS_EQUAL().symbol.line
        nodo.token = f'{ctx.expr(0).getText()}<={ctx.expr(1).getText()}'
        nodo.type = 'Bool'  
        return nodo
    
    def visitEqual(self, ctx: yaplParser.EqualContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # if left.type == 'Id':
        #     self.vars_used.add(left.token)
        # if right.type == 'Id':
        #     self.vars_used.add(right.token)
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
        # TODO ADD SIMBOL TO TABLE ADD SIMBOL
        return nodo
    
    def visitBlock(self, ctx:yaplParser.BlockContext):
        body_list = [self.visit(expr) for expr in ctx.expr()]
        nodo = BlockNode(body_list)
        nodo.line = ctx.LBRACE().symbol.line
        # nodo.type = self._get_super_type(body_list)
        nodo.type = body_list[-1].type
        nodo.token = f'{body_list[-1].token}'
        return nodo
    
    def _get_super_type(self, features: Node = None):
        if features is None:
            features = []
        if len(features) == 0 or None in features:
            return 'Object'
        same_type = all(f.type == features[0].type for f in features)
        return features[0].type if same_type else 'Object'

    
    def visitWhile(self, ctx:yaplParser.WhileContext):
        condition = self.visit(ctx.expr(0))
        # if condition.type == 'Id':
        #     self.vars_used.add(condition.token)
        # if condition.type == 'Int':
        #     self.active_function_width += INT_SIZE
        self.active_scope['level'] += 1
        expression = self.visit(ctx.expr(1))
        self.active_scope['level'] -= 1
        nodo = WhileNode(condition, expression)
        nodo.line = ctx.WHILE().symbol.line
        nodo.type = 'Object'
        return nodo
    
    def visitIf(self, ctx:yaplParser.IfContext):
        condition = self.visit(ctx.expr(0))
        # if condition.type == 'Id':
        #     self.vars_used.add(condition.token)
        # if condition.type == 'Int':
        #     self.active_function_width += INT_SIZE
        self.active_scope['level'] += 1
        then_body = self.visit(ctx.expr(1))
        self.active_scope['level'] += 1
        else_body = self.visit(ctx.expr(2))
        self.active_scope['level'] -= 2
        nodo = IfNode(condition, then_body, else_body)
        nodo.line = ctx.IF().symbol.line
        nodo.type = self._get_super_type([then_body, else_body])
        return nodo
    
    def visitFunctionCall(self, ctx:yaplParser.FunctionCallContext):
        params = [self.visit(ctx.expr(i)) for i in range(len(ctx.expr()))]
        for p in params:
            if p.type == 'Id':
                self.vars_used.add(p.token)
        method = ctx.ID_VAR().getText()
        nodo = MethodCallNode('self', method, params)
        nodo.line = ctx.ID_VAR().symbol.line
        method_return = None
        nodo.type = method_return
        nodo.token = f'{method}({", ".join([p.token for p in params])})'
        return nodo
    
    def visitAttributesDeclaration(self, ctx:yaplParser.AttributesDeclarationContext):
        idx = ctx.ID_VAR().getText()
        typex = ctx.TYPE_IDENTIFIER().getText()
        expression = self.visit(ctx.expr()) if ctx.expr() is not None else None
        nodo = AttrNode(idx, typex, expression)
        nodo.line = ctx.ID_VAR().symbol.line
        if typex == 'Int':
            self.active_function_width += INT_SIZE
        elif typex == 'String':
            self.active_function_width += CHAR_SIZE * len(expression.token)
        elif typex == 'Bool':
            self.active_function_width += BOOL_SIZE
        # TODO AGREGAR TAMAÑO SI ES OBJETO
        return nodo
        
    def visitLet(self, ctx:yaplParser.LetContext):
        # * NO SE NECESITA AGREGAR WIDTH POR QUE SE LE AGREGA CON EL VISIT
        params = []
        for i in range(len(ctx.var_typescript())):
            p = self.visit(ctx.var_typescript(i))
            params.append(p)
            # * Check if var is defined in locals
            if self.active_scope['class_name'] in self.types and self.types[self.active_scope['class_name']].get_local(self.active_scope['method_name'], self.active_scope['level'], p.idx):
                error = ErrorNode()
                error.message = f"ERROR on line {ctx.LET().symbol.line}: Variable {p.idx} is already defined"
                self.errors.append(error)
                p.type = 'ERROR'
            width = 8 # width por defecto es 8 debido a que eso ocupa un puntero
            if p.type == 'Int':
                width = INT_SIZE
            elif p.type == 'Bool':
                width = BOOL_SIZE
            # * Add to local variables table
            self.types[self.active_scope['class_name']].define_local(self.active_scope['method_name'], p.idx, self.active_scope['level'], p.type, width=width)
        body = self.visit(ctx.expr())
        # self._addSimbolToTable(self.active_scope, body)
        nodo = LetNode(params, body)
        nodo.line = ctx.LET().symbol.line
        nodo.type = self._get_super_type(list(params) + [body])
        return nodo
    
    def visitParen(self, ctx:yaplParser.ParenContext):
        return self.visit(ctx.expr())
    
    def visitIsvoid(self, ctx:yaplParser.IsvoidContext):
        expr = self.visit(ctx.expr())
        nodo = IsVoidNode(expr, 'false')
        nodo.line = ctx.ISVOID().symbol.line
        return nodo
    
    def _find_class_with_method(self, methdo: str):
        return next((c for c in self.types if self.types[c].getMethod(methdo)), None)
    
    def visitMethodCall(self, ctx:yaplParser.MethodCallContext):
        # myPet.say_hello();
        # ( NEW Animal ).say_hello()
        # myPet@Animal.say_hello();
        my_var = self.visit(ctx.expr(0))
        if my_var == 'Id':
            self.vars_used.add(my_var.token)
        methodCall = ctx.ID_VAR().getText()
        args = [self.visit(ctx.expr(i)) for i in range(1, len(ctx.expr()))]
        parent = ctx.TYPE_IDENTIFIER().getText() if ctx.TYPE_IDENTIFIER() is not None else None
        nodo = DispatchNode(parent, methodCall, args, my_var, None)
        nodo.line = ctx.ID_VAR().symbol.line
        return nodo
    
    def _get_return_type(self, typex):
        return typex if typex != 'SELF_TYPE' else self.active_scope['class_name']
    
    def visitMethodDef(self, ctx:yaplParser.MethodDefContext):
        self.vars_used = set([])
        self.active_function_width = 0
        name = ctx.ID_VAR().getText()
        self.active_scope['method_name'] = name
        params = []
        for i in range(len(ctx.formal())):
            param = ctx.formal(i)
            idx = param.ID_VAR().getText()
            typex = param.TYPE_IDENTIFIER().getText()
            width = 8 # width por defecto es 8 debido a que eso ocupa un puntero
            if typex == 'Int':
                width = INT_SIZE
            elif typex == 'Bool':
                width = BOOL_SIZE
            params.append(Attribute(idx, typex))
            # * Add to local variables table
            self.types[self.active_scope['class_name']].define_local(name, idx, self.active_scope['level'], typex, width=width)
        typex = self._get_return_type(ctx.TYPE_IDENTIFIER().getText())
        nodo = MethodNode(name, params, typex, None)
        # * check if method is defined
        if self.active_scope['class_name'] in self.types and self.types[self.active_scope['class_name']].getMethod(name):
            error = ErrorNode()
            error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Method {name} is already defined"
            self.errors.append(error)
            nodo.type = 'ERROR'
        # * Add to the table for recursive calls
        self.types[self.active_scope['class_name']].define_method(name, typex, params)
        body = self.visit(ctx.expr())
        self.types[self.active_scope['class_name']].getMethod(name).width = body.width
        # self._addSimbolToTable(self.active_scope, body)
        nodo.body = body
        # for item in self.vars_used:
        #     self.types[self.active_scope['class_name']].getMethod(name).width += self.types[self.active_scope['class_name']].get_attribute(item).width
        # self.types[self.active_scope['class_name']].getMethod(name).width += self.active_function_width
        # el width de la funcion seria la suma de las variables locales
        width = 0
        for l in self.types[self.active_scope['class_name']].locals:
            for level in self.types[self.active_scope['class_name']].locals[l]:
                for t in self.types[self.active_scope['class_name']].locals[l][level]:
                    width += self.types[self.active_scope['class_name']].locals[l][level][t].width
        self.types[self.active_scope['class_name']].getMethod(name).width = width
        nodo.line = ctx.ID_VAR().symbol.line
        nodo.type = typex
        return nodo
    
    def visitProgram(self, ctx:yaplParser.ProgramContext):
        clases = [
            self.visit(ctx.classs(i)) for i in range(len(ctx.classs()))
        ]
        nodo = ProgramNode(clases)
        nodo.line = '0'
        nodo.type = 'Object'
        self.check_global_semantics()
        # * ADD ALL METHODS FROM PARNET TO CHILDREN
        for c in self.types:
            parent = self.types[c].inheritance
            if parent and parent in self.types:
                for method in self.types[parent].methods:
                    self.types[c].define_method(method, self.types[parent].methods[method].return_type, self.types[parent].methods[method].params)
        return nodo

    
    def visitClasss(self, ctx:yaplParser.ClasssContext):
        name = ctx.TYPE_IDENTIFIER(0).getText()
        parent = ctx.TYPE_IDENTIFIER(1).getText() if ctx.TYPE_IDENTIFIER(1) is not None else 'Object'
        # * add class to table if not exists
        if name not in self.types:
            self.types[name] = Klass(name, None, 'class', parent)
        else:
            error = ErrorNode()
            error.message = f"ERROR on line {ctx.CLASS().symbol.line}: Class {name} is already defined"
            self.errors.append(error)
        feature = []
        scope = { 'class_name': name, 'method_name': None, 'level': 0 }
        self.active_scope = scope
        for i in range(len(ctx.feature())):
            f = self.visit(ctx.feature(i))
            feature.append(f)
        nodo = ClassNode(name, parent, feature)
        nodo.line = ctx.CLASS().symbol.line
        nodo.type = 'Object'
        width = 0
        for a in self.types[name].attributes:
            width += self.types[name].attributes[a].width
        for m in self.types[name].methods:
            width += self.types[name].methods[m].width
        self.types[name].width = width
        return nodo
    
    def visitNew(self, ctx:yaplParser.NewContext):
        typex = ctx.TYPE_IDENTIFIER().getText()
        nodo = NewNode(typex)
        nodo.line = ctx.NEW().symbol.line
        self.active_function_width += self.types[typex].width
        return nodo

    def visitAttr(self, ctx:yaplParser.AttrContext):
        idx = ctx.ID_VAR().getText()
        typex = ctx.TYPE_IDENTIFIER().getText()
        expression = self.visit(ctx.expr()) if ctx.expr() is not None else None
        nodo = AttrNode(idx, typex, expression)
        nodo.line = ctx.ID_VAR().symbol.line
        
        # Check if attribute is defined
        class_name = self.active_scope['class_name']
        class_type = self.types.get(class_name)
        
        if class_name in self.types and class_type.get_attribute(idx):
            error = ErrorNode()
            error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Attribute {idx} is already defined"
            self.errors.append(error)
            nodo.type = 'ERROR'

        # get type of asign expression
        class_typex = self.types.get(typex)
        width = class_typex.width
        class_type.define_attribute(idx, typex, width=width)
        # if expression:
        #     # Check if expression is same type
        #     if typex != expression.type:
        #         error = ErrorNode()
        #         error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Cannot assign {expression.type} to {typex}"
        #         self.errors.append(error)
        #     else:
        #         class_type.define_attribute(idx, typex, expression.token)
        # else:
        #     class_type.define_attribute(idx, typex)
        
        return nodo

    
    def show_classes_table(self):
        headers = ['Name' , 'Parent', 'Attributes', 'Methods']
        table = [
            [
                t,
                self.types[t].inheritance,
                self.types[t].get_attributes_names(),
                self.types[t].get_methods_names(),
            ]
            for t in self.types
            if self.types[t].type == 'class'
        ]
        print("\n========== Classes Table ==========\n")
        print(tabulate(table, headers, tablefmt="fancy_grid"))
    
    def show_variables_table(self):
        headers = ['Name', 'Type', 'Scope', 'Value']
        for c in self.types:
            print(f"\n========== {c} Variables Table ==========\n")
            table = []
            for t in self.types[c].attributes:
                var = self.types[c].get_attribute(t)
                table.append([t, var.type, 'GLOBAL', var.value])
            # locals
            for l in self.types[c].locals:
                for level in self.types[c].locals[l]:
                    for t in self.types[c].locals[l][level]:
                        var = self.types[c].get_local(l, level, t)
                        table.append([t, var.type, f'LOCAL: {l} - LEVEL: {level}', var.value])
            print(tabulate(table, headers, tablefmt="fancy_grid"))

    def check_global_semantics(self):
        # * CHECK if main class is defined
        if 'Main' not in self.types:
            self._add_error(
                "ERROR: Main class is not defined"
            )
        # * CHECK if main method is defined
        main_class = None
        if 'Main' in self.types:
            main_class = self.types['Main']
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
        # if main_class.getMethod('main').return_type != 'SELF_TYPE':
        #     self._add_error(
        #         "ERROR: Main method must have no return type"
        #     )
        #     return
        # * CHECK if all parents are defined
        for c in self.types:
            if self.types[c].inheritance and self.types[c].inheritance not in self.types:
                self._add_error(
                    f"ERROR: Parent class {self.types[c].inheritance} is not defined"
                )

    def _add_error(self, message: str):
        error = ErrorNode()
        error.message = message
        self.errors.append(error)
            