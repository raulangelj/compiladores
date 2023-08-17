from yapl.grammar.yaplVisitor import yaplVisitor
from yapl.grammar.yaplParser import yaplParser
from tabulate import tabulate
from yapl.custom.models.Nodes import *
from yapl.custom.models.Types import *

class YaplVisitorCustom(yaplVisitor):
    def __init__(self):
        # self.types: List[Klass] = []
        self.types: dict[str, Klass] = {}
        self.errors = []
        self._set_default_types()
        self.active_scope: ScopeType = { 'class_name': None, 'method_name': None }

    def _set_default_types(self):
        # Defaults types
        self.types['Object'] = Klass('Object', None)
        self.types['IO'] = Klass('IO', None, inheritance='Object')
        self.types['Int'] = Klass('Int', None, inheritance='Object')
        self.types['String'] = Klass('String', None, inheritance='Object')
        self.types['Bool'] = Klass('Bool', None, inheritance='Object')
        # Defaults methods
        # Object
        self.types['Object'].define_method('abort', 'Object', [])
        self.types['Object'].define_method('type_name', 'String', [])
        self.types['Object'].define_method('copy', 'Object', [])
        # io
        self.types['IO'].define_method('out_string', 'SELF_TYPE', [Attribute('x', 'String')])
        self.types['IO'].define_method('out_int', 'SELF_TYPE', [Attribute('x', 'Int')])
        self.types['IO'].define_method('in_string', 'String', [])
        self.types['IO'].define_method('in_int', 'Int', [])
        # integer
        # does not have methods - default value is 0
        # String - default value is ''
        self.types['String'].define_method('length', 'Int', [])
        self.types['String'].define_method('concat', 'String', [Attribute('s', 'String')])
        self.types['String'].define_method('substr', 'String', [Attribute('i', 'Int'), Attribute('l', 'Int')])
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
        valid = self._getError(left, right, '+', nodo.line)
        nodo.token = f'{ctx.expr(0).getText()}+{ctx.expr(1).getText()}'
        nodo.type = 'Int'
        if valid == 'ERROR':
            nodo.type = 'ERROR'
            return nodo
        return nodo
    
    def visitMinus(self, ctx:yaplParser.MinusContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        nodo = MinusNode(left, right)
        nodo.line = ctx.MINUS().symbol.line
        valid = self._getError(left, right, '-', nodo.line)
        nodo.token = f'{ctx.expr(0).getText()}-{ctx.expr(1).getText()}'
        nodo.type = 'Int'
        if valid == 'ERROR':
            nodo.type = 'ERROR'
            return nodo   
        return nodo
    
    def visitMult(self, ctx:yaplParser.MultContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        node = MultNode(left, right)
        node.line = ctx.MULT().symbol.line
        valid = self._getError(left, right, '*', node.line)
        node.token = f'{ctx.expr(0).getText()}*{ctx.expr(1).getText()}'
        node.type = 'Int'
        if valid == 'ERROR':
            node.type = 'ERROR'
            return node   
        return node
    
    def visitDiv(self, ctx: yaplParser.DivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        nodo = DivNode(left, right)
        nodo.line = ctx.DIV().symbol.line
        valid = self._getError(left, right, '/', nodo.line)
        nodo.token = f'{ctx.expr(0).getText()}/{ctx.expr(1).getText()}'
        nodo.type = 'Int'
        if valid == 'ERROR':
            nodo.type = 'ERROR'
            return nodo   
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
        valid = self._getError(left, right, '<', nodo.line)
        nodo.token =  f'{ctx.expr(0).getText()}<{ctx.expr(1).getText()}'
        nodo.type = 'Bool'
        if valid == 'ERROR':
            nodo.type = 'ERROR'
            return nodo   
        return nodo
    
    def visitLess_equal(self, ctx: yaplParser.Less_equalContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        nodo = LessEqualNode(left, right)
        nodo.line = ctx.LESS_EQUAL().symbol.line
        valid = self._getError(left, right, '<=', nodo.line)
        nodo.token = f'{ctx.expr(0).getText()}<={ctx.expr(1).getText()}'
        nodo.type = 'Bool'
        if valid == 'ERROR':
            nodo.type = 'ERROR'
            return nodo   
        return nodo
    
    def visitEqual(self, ctx: yaplParser.EqualContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        nodo = EqualNode(left, right)
        nodo.line = ctx.EQUAL().symbol.line
        valid = self._getError(left, right, '=', nodo.line)
        nodo.token = f'{ctx.expr(0).getText()}={ctx.expr(1).getText()}'
        nodo.type = 'Bool'
        if valid == 'ERROR':
            nodo.type = 'ERROR'
            return nodo
        return nodo
    
    def visitNot(self, ctx: yaplParser.NotContext):
        node = self.visit(ctx.expr())
        nodo = NotNode(node)
        nodo.type = node.type
        nodo.line = ctx.NOT().symbol.line
        self._getError(node, None, 'Not', nodo.line)
        return nodo
    
    def visitNegative(self, ctx: yaplParser.NegativeContext):
        node = self.visit(ctx.expr())
        nodo = NegativeNode(node, f'~{ctx.expr().getText()}')
        nodo.type = node.type
        nodo.line = ctx.NEGATIVE().symbol.line
        self._getError(node, None, 'Negative', nodo.line)
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
        # body_list = [self.visit(expr) for expr in ctx.expr()]
        body_list =[]
        for expr in ctx.expr():
            body_list.append(self.visit(expr))
            self._addSimbolToTable(self.active_scope, body_list[-1])
        nodo = BlockNode(body_list)
        nodo.line = ctx.LBRACE().symbol.line
        nodo.type = self._get_super_type(body_list)
        return nodo
    
    def _get_super_type(self, features: Node = []):
        if len(features) == 0 or None in features:
            return 'Object'
        same_type = all(f.type == features[0].type for f in features)
        return features[0].type if same_type else 'Object'

    
    def visitWhile(self, ctx:yaplParser.WhileContext):
        condition = self.visit(ctx.expr(0))
        expression = self.visit(ctx.expr(1))
        nodo = WhileNode(condition, expression)
        nodo.line = ctx.WHILE().symbol.line
        nodo.type = 'Object'
        # * if contidion is an id check if it is defined
        valid_condition = self._check_for_use_id(condition)
        if valid_condition == 'ERROR':
            nodo.type = 'ERROR'
            return nodo
        # * Check if condition is bool
        if condition.type == 'Bool':
            pass
        elif condition.type == 'Int' and condition.token in ['0', '1']:
            condition.type = 'Bool'
            condition.value = BooleanNode('true' if condition.token == '1' else 'false')
        elif condition.type == 'Int' and hasattr(condition, 'value') and condition.value.token in ['0', '1']:
            condition.type = 'Bool'
            condition.value = BooleanNode('true' if condition.value.token == '1' else 'false')
        else:
            error = ErrorNode()
            error.message = f"ERROR on line {nodo.line}: Condition must be Bool"
            self.errors.append(error)
            nodo.type = 'ERROR'
        return nodo
    
    def visitIf(self, ctx:yaplParser.IfContext):
        condition = self.visit(ctx.expr(0))
        then_body = self.visit(ctx.expr(1))
        else_body = self.visit(ctx.expr(2))
        nodo = IfNode(condition, then_body, else_body)
        nodo.line = ctx.IF().symbol.line
        nodo.type = self._get_super_type([then_body, else_body])
        # * if contidion is an id check if it is defined
        valid_condition = self._check_for_use_id(condition)
        if valid_condition == 'ERROR':
            nodo.type = 'ERROR'
            return nodo
        # * Check if condition is bool
        if condition.type == 'Bool':
            pass
        elif condition.type == 'Int' and condition.token in ['0', '1']:
            condition.type = 'Bool'
            condition.value = BooleanNode('true' if condition.token == '1' else 'false')
        elif condition.type == 'Int' and hasattr(condition, 'value') and condition.value.token in ['0', '1']:
            condition.type = 'Bool'
            condition.value = BooleanNode('true' if condition.value.token == '1' else 'false')
        else:
            error = ErrorNode()
            error.message = f"ERROR on line {ctx.IF().symbol.line}: Condition must be Bool"
            self.errors.append(error)
            nodo.type = 'ERROR'
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
        # * check if method is defined
        if self.active_scope['class_name'] not in self.types or not self.types[self.active_scope['class_name']].getMethod(method):
            error = ErrorNode()
            error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Method {method} is not defined"
            self.errors.append(error)
            nodo.type = 'ERROR'
            return nodo
        
        # * Check if params count is the same as the method
        if len(params) != len(method_params):
            error = ErrorNode()
            error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Method {method} must have {len(method_params)} params"
            self.errors.append(error)
            nodo.type = 'ERROR'
            return nodo
        for i in range(len(params)):
            # * Check if var is defined
            valid = self._check_for_use_id(params[i])
            if valid == 'ERROR':
                nodo.type = 'ERROR'
                return nodo
            # * check if params are the same type as the method
            if params[i].type != method_params[i].type:
                error = ErrorNode()
                error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Method {method} param {method_params[i].name} must be {method_params[i].type}"
                self.errors.append(error)
                nodo.type = 'ERROR'
                return nodo
            # * Change the value of the param in local var
            if self.active_scope['class_name'] in self.types and self.types[self.active_scope['class_name']].get_local(self.active_scope['method_name'], method_params[i].name):
                self.types[self.active_scope['class_name']].get_local(method, method_params[i].name).value = params[i].token
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
            # * Check if var is defined in locals
            if self.active_scope['class_name'] in self.types and self.types[self.active_scope['class_name']].get_local(self.active_scope['method_name'], p.idx):
                error = ErrorNode()
                error.message = f"ERROR on line {ctx.LET().symbol.line}: Variable {p.idx} is already defined"
                self.errors.append(error)
                p.type = 'ERROR'
            # * Add to local variables table
            self.types[self.active_scope['class_name']].define_local(self.active_scope['method_name'], p.idx, p.type)
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
        # * Check if var is defined
        valid = self._check_for_use_id(my_var)
        if valid == 'ERROR':
            nodo.type = 'ERROR'
            return nodo
        # TODO FALTA REVISAR SI MY_VAR ES UNA FUNCION
        # * Check method validation
        my_var_type = my_var.type
        if parent:
            # * Check if type is the parent of the var
            if self.types[self.active_scope['class_name']].inheritance != parent:
                error = ErrorNode()
                error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Method {methodCall} is not defined in {parent}"
                return self._extracted_from_visitMethodCall_22(error, nodo)
            # * check if method is defined
            if parent not in self.types or not self.types[parent].getMethod(methodCall):
                return self._extracted_from_visitMethodCall_27(ctx, methodCall, nodo, my_var_type)
            # * Check if params count is the same as the method
            if len(args) != len(self.types[parent].getMethod(methodCall).params):
                error = ErrorNode()
                error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Method {methodCall} must have {len(self.types[parent].getMethod(methodCall).params)} params"
                return self._extracted_from_visitMethodCall_22(error, nodo)
            for i in range(len(args)):
                # * Check if var is defined
                valid = self._check_for_use_id(args[i])
                if valid == 'ERROR':
                    nodo.type = 'ERROR'
                    return nodo
                # * check if params are the same type as the method
                if args[i].type != self.types[parent].getMethod(methodCall).params[i].type:
                    error = ErrorNode()
                    error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Method {methodCall} param {self.types[parent].getMethod(methodCall).params[i].name} must be {self.types[parent].getMethod(methodCall).params[i].type}"
                    return self._extracted_from_visitMethodCall_22(error, nodo)
        else:
            # * check if method is defined
            if my_var_type not in self.types or not self.types[my_var_type].getMethod(methodCall):
                return self._extracted_from_visitMethodCall_27(ctx, methodCall, nodo, my_var_type)
            # * Check if params count is the same as the method
            if len(args) != len(self.types[my_var_type].getMethod(methodCall).params):
                error = ErrorNode()
                error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Method {methodCall} must have {len(self.types[my_var_type].getMethod(methodCall).params)} params"
                return self._extracted_from_visitMethodCall_22(error, nodo)
            for i in range(len(args)):
                # * Check if var is defined
                valid = self._check_for_use_id(args[i])
                if valid == 'ERROR':
                    nodo.type = 'ERROR'
                    return nodo
                # * check if params are the same type as the method
                if args[i].type != self.types[my_var_type].getMethod(methodCall).params[i].type:
                    error = ErrorNode()
                    error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Method {methodCall} param {self.types[my_var_type].getMethod(methodCall).params[i].name} must be {self.types[my_var_type].getMethod(methodCall).params[i].type}"
                    return self._extracted_from_visitMethodCall_22(error, nodo)
        return nodo

    # TODO Rename this here and in `visitMethodCall`
    def _extracted_from_visitMethodCall_27(self, ctx, methodCall, nodo, class_name):
        error = ErrorNode()
        error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Method {methodCall} is not defined in {class_name}"
        return self._extracted_from_visitMethodCall_22(error, nodo)

    # TODO Rename this here and in `visitMethodCall`
    def _extracted_from_visitMethodCall_22(self, error, nodo):
        self.errors.append(error)
        nodo.type = 'ERROR'
        return nodo
        
    
    def visitMethodDef(self, ctx:yaplParser.MethodDefContext):
        name = ctx.ID_VAR().getText()
        self.active_scope['method_name'] = name
        params = []
        for i in range(len(ctx.formal())):
            param = ctx.formal(i)
            idx = param.ID_VAR().getText()
            typex = param.TYPE_IDENTIFIER().getText()
            params.append(Attribute(idx, typex))
            # * Add to local variables table
            self.types[self.active_scope['class_name']].define_local(name, idx, typex)
        typex = ctx.TYPE_IDENTIFIER().getText()
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
        self._addSimbolToTable(self.active_scope, body)
        # * Validate signature if method is inherited
        if self.active_scope['class_name'] in self.types and self.types[self.active_scope['class_name']].inheritance:
            parent = self.types[self.active_scope['class_name']].inheritance
            if parent in self.types and self.types[parent].getMethod(name):
                parent_method = self.types[parent].getMethod(name)
                if parent_method.return_type != typex:
                    error = ErrorNode()
                    error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Method {name} must return {parent_method.return_type} as defined in parent"
                    self.errors.append(error)
                    typex = 'ERROR'
                if len(parent_method.params) != len(params):
                    error = ErrorNode()
                    error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Method {name} must have {len(parent_method.params)} params as defined in parent"
                    self.errors.append(error)
                    typex = 'ERROR'
                else:
                    for i in range(len(params)):
                        if params[i].type != parent_method.params[i].type:
                            error = ErrorNode()
                            error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Method {name} param {parent_method.params[i].name} must be {parent_method.params[i].type} as defined in parent"
                            self.errors.append(error)
                            typex = 'ERROR'
        nodo.body = body
        nodo.line = ctx.ID_VAR().symbol.line
        nodo.type = typex
        return nodo
    
    def visitClasss(self, ctx:yaplParser.ClasssContext):
        name = ctx.TYPE_IDENTIFIER(0).getText()
        parent = ctx.TYPE_IDENTIFIER(1).getText() if ctx.TYPE_IDENTIFIER(1) is not None else None
        # * add class to table if not exists
        if name not in self.types:
            self.types[name] = Klass(name, None, 'class', parent)
        else:
            error = ErrorNode()
            error.message = f"ERROR on line {ctx.CLASS().symbol.line}: Class {name} is already defined"
            self.errors.append(error)
        feature = []
        # * check if parent is not one of the basic types
        if parent in ['Int', 'String', 'Bool']:
            error = ErrorNode()
            error.message = f"ERROR on line {ctx.CLASS().symbol.line}: Cannot inherit from {parent}"
            self.errors.append(error)
            nodo.type = 'ERROR'
        # * add methods from parent to table
        if parent:
            if parent not in self.types:
                error = ErrorNode()
                error.message = f"ERROR on line {ctx.CLASS().symbol.line}: Cannot inherites from {parent} since is not defined"
                self.errors.append(error)
                nodo.type = 'ERROR'
            else:
                for method in self.types[parent].methods:
                    self.types[name].define_method(method, self.types[parent].methods[method].return_type, self.types[parent].methods[method].params)
        scope = { 'class_name': name, 'method_name': None }
        self.active_scope = scope
        for i in range(len(ctx.feature())):
            f = self.visit(ctx.feature(i))
            # if isinstance(f, MethodNode):
                # * add methods to table in class
                # self.types[name].define_method(f.name, f.return_type, f.params)
            feature.append(f)
            self._addSimbolToTable(scope, f)
        nodo = ClassNode(name, parent, feature)
        nodo.line = ctx.CLASS().symbol.line
        # TODO falta el type
        return nodo
    
    def visitNew(self, ctx:yaplParser.NewContext):
        typex = ctx.TYPE_IDENTIFIER().getText()
        nodo = NewNode(typex)
        nodo.line = ctx.NEW().symbol.line
        if typex not in self.types:
            error = ErrorNode()
            error.message = f"ERROR on line {ctx.NEW().symbol.line}: Class {typex} is not defined"
            self.errors.append(error)
            nodo.type = 'ERROR'
        return nodo

    def visitAttr(self, ctx:yaplParser.AttrContext):
        idx = ctx.ID_VAR().getText()
        typex = ctx.TYPE_IDENTIFIER().getText()
        expression = self.visit(ctx.expr()) if ctx.expr() is not None else None
        nodo = AttrNode(idx, typex, expression)
        nodo.line = ctx.ID_VAR().symbol.line
        # * check if attribute is defined
        if self.active_scope['class_name'] in self.types and self.types[self.active_scope['class_name']].get_attribute(idx):
            error = ErrorNode()
            error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Attribute {idx} is already defined"
            self.errors.append(error)
            nodo.type = 'ERROR'
        if nodo.value:
            # * CHECK if expression is same type
            if typex != nodo.value.type:
                error = ErrorNode()
                error.message = f"ERROR on line {ctx.ID_VAR().symbol.line}: Cannot assign {expression.type} to {typex}"
                self.errors.append(error)
            else:
                self.types[self.active_scope['class_name']].define_attribute(idx, typex, nodo.value.token)
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
            # scope = f'Class: {c}'
            for t in self.types[c].attributes:
                var = self.types[c].get_attribute(t)
                table.append([t, var.type, 'GLOCAL', var.value])
            # locals
            for l in self.types[c].locals:
                for t in self.types[c].locals[l]:
                    var = self.types[c].get_local(l, t)
                    table.append([t, var.type, f'LOCAL: {l}', var.value])
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
        if main_class.getMethod('main').return_type != 'SELF_TYPE':
            self._add_error(
                "ERROR: Main method must have no return type"
            )
            return

    def _add_error(self, message: str):
        error = ErrorNode()
        error.message = message
        self.errors.append(error)

    def _is_defined(self, name: str, scope: ScopeType) -> bool:
        isglobal_val = scope['class_name'] in self.types and self.types[scope['class_name']].get_attribute(name) is not None
        islocal_var = False
        if scope['method_name'] is not None:
            classVar = self.types[scope['class_name']]
            islocal_var = classVar.get_local(scope['method_name'], name) is not None
        return isglobal_val or islocal_var
    
    def _addSimbolToTable(self, scope: ScopeType, node: Node) -> str or None:
        # print(type (node))
        if isinstance(node, AttrNode):
            print('attr')
            value = node.value.token if node.value else None
            self.types[scope['class_name']].define_attribute(node.idx, node.type, value)
        elif isinstance(node, MethodNode):
            print('method')
            if isinstance(node.body, BlockNode):
                for s in node.body.statements:
                    new_scope = { 'class_name': scope['class_name'], 'method_name': node.name }
                    # self._addSimbolToTable(new_scope, s)
                # TODO check if a local var is the same type as the return type
                if hasattr(node.body.statements[-1], 'type') and node.body.statements[-1].type != node.return_type != 'SELF_TYPE':
                    error = ErrorNode()
                    error.message = f"ERROR on line {node.line}: Method {node.name} must return {node.return_type}"
                    self.errors.append(error)
                    return 'ERROR'
            else:
                self._addSimbolToTable(scope, node.body)
        elif isinstance(node, AssignNode):
            print('assign')
            # * CHECK if variable is defined
            if not self._is_defined(node.idx, scope):
                error = ErrorNode()
                error.message = f"ERROR on line {node.line}: Variable {node.idx} is not defined"
                self.errors.append(error)
                return 'ERROR'
            else:
                # assign the value in the simbols table
                # * Check asign is adding a ID
                if node.value.type == 'Id':
                    valid = self._check_for_use_id(node.value)
                    if valid == 'ERROR':
                        return 'ERROR'
                # * CHECK if expression is same type
                if self._get_variable(node.idx).type != node.value.type:
                    error = ErrorNode()
                    error.message = f"ERROR on line {node.line}:Cannot assign {node.value.type} to {self._get_variable(node.idx).type}"
                    self.errors.append(error)
                    return 'ERROR'
                value = node.value.token if node.value else None
                self._get_variable(node.idx).value = value
        elif isinstance(node, BlockNode):
            for s in node.statements:
                new_scope = { 'class_name': scope['class_name'], 'method_name': scope['method_name'] }
                self._addSimbolToTable(new_scope, s)
        return None
    
    def _get_variable(self, name: str) -> Attribute or None:
        if self.types[self.active_scope['class_name']].get_local(self.active_scope['method_name'], name):
            return self.types[self.active_scope['class_name']].get_local(self.active_scope['method_name'], name)
        elif self.types[self.active_scope['class_name']].get_attribute(name):
            return self.types[self.active_scope['class_name']].get_attribute(name)
        return None

    def _check_for_use_id(self, node: Node) -> str or None:
        error = ErrorNode()
        if node.type == 'Id':
            if node.token == 'self':
                node.type = self.active_scope['class_name']
                return None
            if not self._is_defined(node.token, self.active_scope):
                error.message = f"ERROR on line {node.line}: Variable {node.token} is not defined"
                self.errors.append(error)
                return 'ERROR'
            else:
                var = self._get_variable(node.token)
                if var.value is None:
                    error.message = f"ERROR on line {node.line}: Variable {node.token} is not initialized"
                    self.errors.append(error)
                    return 'ERROR'
                node.type = var.type
                if node.type == 'SELF_TYPE': # TODO REVICSAR!
                    node.type = self.active_scope['class_name']
                elif node.type == 'Int':
                    node.value = IntegerNode(var.value)
                elif node.type == 'String':
                    node.value = StringNode(var.value)
                elif node.type == 'Bool':
                    node.value = BooleanNode(var.value)
        return None
    
    def _arithmeticErros(self, left, right, operator, line) -> str or None:
        error = ErrorNode()
        # show error if left or right is not Int type but if is Id let it pass
        # if one is ID check in the simbols to see if it is defined
        valid_left = self._check_for_use_id(left)
        valid_right = self._check_for_use_id(right)
        if valid_left == 'ERROR' or valid_right == 'ERROR':
            return 'ERROR'
        if left.type == 'Bool':
            left.type = 'Int'
            left.value = IntegerNode('1' if left.token == 'true' else '0')
        if right.type == 'Bool':
            right.type = 'Int'
            right.value = IntegerNode('1' if right.token == 'true' else '0')
        if left.type not in ['Int'] or right.type not in ['Int']:
            error.get_error(left, right, operator, line)
            self.errors.append(error)
            return 'ERROR'
        return None

    def _comparisonErrors(self, left, right, operator) -> str or None:
        error = ErrorNode()
        # if one is ID check in the simbols to see if it is defined
        valid_left = self._check_for_use_id(left)
        valid_right = self._check_for_use_id(right)
        if valid_left == 'ERROR' or valid_right == 'ERROR':
            return 'ERROR'
        parent_left = self.types[left.type].inheritance
        parent_right = self.types[right.type].inheritance
        if left.type == right.type or parent_left == parent_right or parent_right == left.type or parent_left == right.type:
            return None
        error.get_error(left, right, operator)
        self.errors.append(error)
        return 'ERROR'
    
    def _getError(self, left, right, operator, line) -> str or None:
        match operator:
            case '+':
                return self._arithmeticErros(left, right, operator, line)
            case '-':
                return self._arithmeticErros(left, right, operator, line)
            case '*':
                return self._arithmeticErros(left, right, operator, line)
            case '/':
                return self._arithmeticErros(left, right, operator, line)
            case '<':
                return self._comparisonErrors(left, right, operator)
            case '<=':
                return self._comparisonErrors(left, right, operator)
            case '=':
                return self._comparisonErrors(left, right, operator)
            case 'Not':
                # key 'not'
                if left.type == 'Id':
                    valid_left = self._check_for_use_id(left)
                    if valid_left == 'ERROR':
                        return 'ERROR'
                if left.type not in ['Bool']:
                    return self._add_unsupported_errror(operator, left, line)
            case 'Negative':
                # key '~'
                if left.type == 'Id':
                    valid_left = self._check_for_use_id(left)
                    if valid_left == 'ERROR':
                        return 'ERROR'
                if left.type == 'String':
                    return self._add_unsupported_errror(operator, left, line)
            case _:
                return None

    def _add_unsupported_errror(self, operator, left, line) -> str:
        error = ErrorNode()
        error.message = f"Error on line {line}: unsupported operation {operator}: with {left.type}"
        self.errors.append(error)
        return 'ERROR'
            