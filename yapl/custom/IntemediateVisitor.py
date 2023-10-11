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
    
    def get_last_offset(self):
        if self.active_scope['method_name'] is None:
            diccionario = self.types[self.active_scope['class_name']].attributes

        elif self.active_scope['method_name'] not in self.types[self.active_scope['class_name']].locals:
            return Attribute('','')
        else:
            diccionario = self.types[self.active_scope['class_name']].locals[self.active_scope['method_name']]
        last_value = Attribute('', '')
        for j in diccionario.items():
            if type(j[1]) == dict:
                for i in j[1].items():
                    if i[1].offset >= last_value.offset:
                        last_value = i[1]
            elif j[1].offset >= last_value.offset:
                last_value = j[1]
        return last_value
                
    def show_variables_table(self):
        headers = ['Name', 'Type', 'Scope', 'Value', 'Width', 'Offset']
        for c in self.types:
            print(f"\n========== {c} Variables Table ==========\n")
            table = []
            for t in self.types[c].attributes:
                var = self.types[c].get_attribute(t)
                table.append([t, var.type, 'GLOBAL', var.value, var.width, var.offset])
            # locals
            for l in self.types[c].locals:
                for level in self.types[c].locals[l]:
                    for t in self.types[c].locals[l][level]:
                        var = self.types[c].get_local(l, level, t)
                        table.append([t, var.type, f'LOCAL: {l} - LEVEL: {level}', var.value, var.width, var.offset])
            print(tabulate(table, headers, tablefmt="fancy_grid"))

    def show_classes_table(self):
        headers = ['Name' , 'Parent', 'Attributes', 'Methods', 'Width']
        table = [
            [
                t,
                self.types[t].inheritance,
                self.types[t].get_attributes_names(),
                self.types[t].get_methods_names(),
                self.types[t].width
            ]
            for t in self.types
            if self.types[t].type == 'class'
        ]
        print("\n========== Classes Table ==========\n")
        print(tabulate(table, headers, tablefmt="fancy_grid"))

    def generate(self, left: str, right: str, op: str = None, type: str = 'Quadruple', left_node: Node = None) -> Quadruple:
        if type == 'If':
            self.actual_label += 1
            return Quadruple(op, left, right, f'L{self.actual_label}', type)
        if type == 'Assign_temp':
            # offset=self.local_offset)
            self.actual_temp += 1
            item = self.get_last_offset()
            classn = None
            if left_node.type == 'Id':
                if isinstance(left_node, BlockNode):
                    classn = left_node.statements[-1].token
                else:
                    # check for the type of the id in locals
                    var = self.types[self.active_scope['class_name']].get_local_at_any_level(self.active_scope['method_name'], left_node.token)
                    if var != None:
                        classn = var.type
                    else:
                        classn = self.types[self.active_scope['class_name']].get_attribute(left_node.token).type
            else:
                classn = left_node.type
            if classn.lower() == 'self' or classn.lower() == 'self_type':
                classn = self.active_scope['class_name']
            
            self.types[self.active_scope['class_name']].define_local(self.active_scope['method_name'], self.get_active_temp(), self.active_scope['level'], classn, left, self.types[classn].width, item.width + item.offset)
            return Quadruple(op, left, right, self.get_active_temp(), 'Assign')
        if type == 'PARAM':
            return Quadruple(None, None, None, f'{right}', type)
        if type == 'Function':
            return Quadruple(None, left, right, f'{self.actual_label}', type)
        if type == 'Goto':
            return Quadruple(op, left, right, f'{left}', type)
        self.actual_temp += 1
        item = self.get_last_offset()
        classn = None
        
        if left_node.type == 'Id':
            if isinstance(left_node, BlockNode):
                classn = left_node.statements[-1].token
            else:
                # check for the type of the id in locals
                var = self.types[self.active_scope['class_name']].get_local_at_any_level(self.active_scope['method_name'], left_node.token)
                if var != None:
                    classn = var.type
                else:
                    classn = self.types[self.active_scope['class_name']].get_attribute(left_node.token).type
        else:
            classn = left_node.type
        if classn.lower() == 'self' or classn.lower() == 'self_type':
            classn = self.active_scope['class_name']
        self.types[self.active_scope['class_name']].define_local(self.active_scope['method_name'], self.get_active_temp(), self.active_scope['level'], classn, left, self.types[classn].width, item.width + item.offset)
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
        if right.generate_r != None:
            new_right = right.generate_r
        elif isinstance(right, (IntegerNode, IdNode)):
            new_right = right.token
        elif isinstance(right, MethodCallNode):
            new_right = 'R'
        else:
            new_right = self.get_active_temp()
            nodo.generate_r = self.get_active_temp()
        if left.generate_r != None:
            new_left = left.generate_r 
        elif isinstance(left, (IntegerNode, IdNode)):
            new_left = left.token
        elif isinstance(left, MethodCallNode):
            new_left = 'R'
        else:
            new_left = self.get_active_temp()
            nodo.generate_r = self.get_active_temp()
        if self.active_scope['method_name']:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(new_left, new_right, '+', left_node=nodo))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(new_left, new_right, '+', left_node=nodo))
        return nodo
    
    def visitMinus(self, ctx:yaplParser.MinusContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        nodo = MinusNode(left, right)
        nodo.line = ctx.MINUS().symbol.line
        nodo.token = f'{ctx.expr(0).getText()}-{ctx.expr(1).getText()}'
        nodo.type = 'Int'
        # * Generate intermediate code
        if right.generate_r != None:
            new_right = right.generate_r
        elif isinstance(right, (IntegerNode, IdNode)):
            new_right = right.token
        elif isinstance(right, MethodCallNode):
            new_right = 'R'
        else:
            new_right = self.get_active_temp()
            nodo.generate_r = self.get_active_temp()
        if left.generate_r != None:
            new_left = left.generate_r 
        elif isinstance(left, (IntegerNode, IdNode)):
            new_left = left.token
        elif isinstance(left, MethodCallNode):
            new_left = 'R'
        else:
            new_left = self.get_active_temp()
            nodo.generate_r = self.get_active_temp()
        if self.active_scope['method_name']:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(new_left, new_right, '-', left_node=nodo))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(new_left, new_right, '-', left_node=nodo))
        return nodo
    
    def visitMult(self, ctx:yaplParser.MultContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        node = MultNode(left, right)
        node.line = ctx.MULT().symbol.line
        node.token = f'{ctx.expr(0).getText()}*{ctx.expr(1).getText()}'
        node.type = 'Int'
        # * Generate intermediate code
        if right.generate_r != None:
            new_right = right.generate_r
        elif isinstance(right, (IntegerNode, IdNode)):
            new_right = right.token
        elif isinstance(right, MethodCallNode):
            new_right = 'R'
        else:
            new_right = self.get_active_temp()
            node.generate_r = self.get_active_temp()
        if left.generate_r != None:
            new_left = left.generate_r 
        elif isinstance(left, (IntegerNode, IdNode)):
            new_left = left.token
        elif isinstance(left, MethodCallNode):
            new_left = 'R'
        else:
            new_left = self.get_active_temp()
            node.generate_r = self.get_active_temp()
        if self.active_scope['method_name']:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(new_left, new_right, '*', left_node=node))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(new_left, new_right, '*', left_node=node))
        return node
    
    def visitDiv(self, ctx: yaplParser.DivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        nodo = DivNode(left, right)
        nodo.line = ctx.DIV().symbol.line
        nodo.token = f'{ctx.expr(0).getText()}/{ctx.expr(1).getText()}'
        nodo.type = 'Int'
        # * Generate intermediate code
        if right.generate_r != None:
            new_right = right.generate_r
        elif isinstance(right, (IntegerNode, IdNode)):
            new_right = right.token
        elif isinstance(right, MethodCallNode):
            new_right = 'R'
        else:
            new_right = self.get_active_temp()
            nodo.generate_r = self.get_active_temp()
        if left.generate_r != None:
            new_left = left.generate_r 
        elif isinstance(left, (IntegerNode, IdNode)):
            new_left = left.token
        elif isinstance(left, MethodCallNode):
            new_left = 'R'
        else:
            new_left = self.get_active_temp()
            nodo.generate_r = self.get_active_temp()
        if self.active_scope['method_name']:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(new_left, new_right, '/', left_node=nodo))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(new_left, new_right, '/', left_node=nodo))
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
        if right.generate_r != None:
            new_right = right.generate_r
        elif isinstance(right, (IntegerNode, IdNode)):
            new_right = right.token
        elif isinstance(right, MethodCallNode):
            new_right = 'R'
        else:
            new_right = self.get_active_temp()
            nodo.generate_r = self.get_active_temp()
        if left.generate_r != None:
            new_left = left.generate_r 
        elif isinstance(left, (IntegerNode, IdNode)):
            new_left = left.token
        elif isinstance(left, MethodCallNode):
            new_left = 'R'
        else:
            new_left = self.get_active_temp()
            nodo.generate_r = self.get_active_temp()
        if self.active_scope['method_name']:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(new_left, new_right, '<', left_node=nodo))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(new_left, new_right, '<', left_node=nodo))
        return nodo
    
    def visitLess_equal(self, ctx: yaplParser.Less_equalContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        nodo = LessEqualNode(left, right)
        nodo.line = ctx.LESS_EQUAL().symbol.line
        nodo.token = f'{ctx.expr(0).getText()}<={ctx.expr(1).getText()}'
        nodo.type = 'Bool'
        # * Generate intermediate code
        if right.generate_r != None:
            new_right = right.generate_r
        elif isinstance(right, (IntegerNode, IdNode)):
            new_right = right.token
        elif isinstance(right, MethodCallNode):
            new_right = 'R'
        else:
            new_right = self.get_active_temp()
            nodo.generate_r = self.get_active_temp()
        if left.generate_r != None:
            new_left = left.generate_r 
        elif isinstance(left, (IntegerNode, IdNode)):
            new_left = left.token
        elif isinstance(left, MethodCallNode):
            new_left = 'R'
        else:
            new_left = self.get_active_temp()
            nodo.generate_r = self.get_active_temp()
        if self.active_scope['method_name']:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(new_left, new_right, '<=', left_node=nodo))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(new_left, new_right, '<=', left_node=nodo))
        return nodo
    
    def visitEqual(self, ctx: yaplParser.EqualContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        nodo = EqualNode(left, right)
        nodo.line = ctx.EQUAL().symbol.line
        nodo.token = f'{ctx.expr(0).getText()}={ctx.expr(1).getText()}'
        nodo.type = 'Bool'
        # * Generate intermediate code
        if right.generate_r != None:
            new_right = right.generate_r
        elif isinstance(right, (IntegerNode, IdNode)):
            new_right = right.token
        elif isinstance(right, MethodCallNode):
            new_right = 'R'
        else:
            new_right = self.get_active_temp()
            nodo.generate_r = self.get_active_temp()
        if left.generate_r != None:
            new_left = left.generate_r 
        elif isinstance(left, (IntegerNode, IdNode)):
            new_left = left.token
        elif isinstance(left, MethodCallNode):
            new_left = 'R'
        else:
            new_left = self.get_active_temp()
            nodo.generate_r = self.get_active_temp()
        if self.active_scope['method_name']:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(new_left, new_right, '==' ,left_node=nodo))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(new_left, new_right, '==', left_node=nodo))
        return nodo
    
    def visitNot(self, ctx: yaplParser.NotContext):
        node = self.visit(ctx.expr())
        nodo = NotNode(node)
        nodo.type = node.type
        nodo.line = ctx.NOT().symbol.line
        # * generacion de codigo intermedio
        if isinstance(node, DispatchNode):
            # ? USO LA ACTIVE TEMP POR QUE SE QUE AL SER UNA FUNCION LA R SE GUARDA EN UNA TEMPORAL
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(f'NOT {self.get_active_temp()}', None, None, 'Assign_temp', left_node=nodo))
        return nodo
    
    def visitNegative(self, ctx: yaplParser.NegativeContext):
        node = self.visit(ctx.expr())
        nodo = NegativeNode(node, f'{ctx.expr().getText()}')
        nodo.type = node.type
        nodo.line = ctx.NEGATIVE().symbol.line
        # * Generacion de codigo intermedio
        if self.active_scope['method_name']:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(f'~{node.token}', None, None, 'Assign_temp', left_node=nodo))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(f'~{node.token}', None, None, 'Assign_temp', left_node=nodo))
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
        if isinstance(expression, MethodCallNode):
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.store_attribute(idx, 'R', 'Assign'))
        elif not expression or isinstance(expression, (IntegerNode, StringNode, BooleanNode, IdNode)):
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
        # * Generacion de codigo intermedio
        # Guardo el ultimo valor en una variable temporal
        if self.active_scope['method_name'] is None:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(body_list[-1].token, None, None, 'Assign_temp', left_node=nodo))
        elif isinstance(body_list[-1], DispatchNode) and body_list[-1].token != '':
            nodo.token = body_list[-1].token
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(body_list[-1].token, None, None, 'Assign_temp', left_node=nodo))
        elif body_list[-1].token != '' and body_list[-1].token is not None and body_list[-1].token != 'R' and not isinstance(body_list[-1], LetNode):
            nodo.token = body_list[-1].token
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(body_list[-1].token, None, None, 'Assign_temp', left_node=nodo))
        return nodo
    
    def _get_super_type(self, features: Node = []):
        if len(features) == 0 or None in features:
            return 'Object'
        same_type = all(f.type == features[0].type for f in features)
        return features[0].type if same_type else 'Object'

    
    def visitWhile(self, ctx:yaplParser.WhileContext):
        # TODO REVISAR QUE FALTA
        # * Generar codigo intermedio
        while_label = self.generate_label()
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, _type='Label', result=while_label))

        condition = self.visit(ctx.expr(0))
        if isinstance(condition, IfNode) and condition.generate_r:
            temp_while = 'R'
        elif isinstance(condition, (IntegerNode, BooleanNode)):
            temp_while = condition.token
        else:
            temp_while = self.get_active_temp()

        while_true_label = self.generate_label()        
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, temp_while, None, f'Goto {while_true_label.result}', 'If'))
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(f'END_{while_label.result}', None, f'Goto END_{while_label.result}', 'Goto'))

        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, _type='Label', result=while_true_label.result))
        self.active_scope['level'] += 1
        expression = self.visit(ctx.expr(1))
        self.active_scope['level'] -= 1
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, _type='Label', result=f'END_{while_true_label.result}'))

        # self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, temp_while, None, f'Goto {while_label.result}', 'Goto'))
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(f'{while_label.result}', None, f'Goto {while_label.result}', 'Goto'))
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, _type='Label', result=f'END_{while_label.result}'))

        nodo = WhileNode(condition, expression)
        nodo.line = ctx.WHILE().symbol.line
        nodo.type = 'Object'
        return nodo
    
    def visitIf(self, ctx:yaplParser.IfContext):
        created_R = False
        condition = self.visit(ctx.expr(0))
        self.active_scope['level'] += 1
        # * Generate intermediate code
        value = 'R' if isinstance(condition, DispatchNode) else self.get_active_temp()
        
        if isinstance(condition, (IntegerNode, BooleanNode)):
            if_condition = condition.token
        else:
            if_condition = self.get_active_temp()

        if_true = self.generate(value, None, f'Goto {if_condition}', 'If')
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(if_true)
        if_false = self.generate_label()
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(if_false.result, None, f'Goto {if_false.result}', 'Goto'))

        # * THEN BODY
        # * Generate intermediate code
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, _type='Label', result=if_true.result))
        # if is BoolNode add a R
        then_body = self.visit(ctx.expr(1))
        if isinstance(then_body, (IntegerNode, BooleanNode)):
            created_R = True
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.store_attribute('R', then_body.token, 'Assign'))
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, _type='Label', result=f'END_{if_true.result}'))
        self.active_scope['level'] += 1

        # * ELSE BODY
        # * Generate intermediate code
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, _type='Label', result=if_false.result))
        else_body = self.visit(ctx.expr(2))
        if isinstance(else_body, (IntegerNode, BooleanNode)):
            created_R = True
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.store_attribute('R', else_body.token, 'Assign'))
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, _type='Label', result=f'END_{if_false.result}'))
        self.active_scope['level'] -= 2
        nodo = IfNode(condition, then_body, else_body)
        nodo.generate_r = created_R
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
        # generacion codigo intermedio
        for param in params:
                # ! AGREGAR A LA TABLA LA R AQUI!
            if self.active_scope['method_name'] is None:
                self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(None, param.token, None, 'PARAM', left_node=nodo))
            elif isinstance(param, (DispatchNode, BiOperationNode)):
                self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(None, self.get_active_temp(), None, 'PARAM', left_node=nodo))
            else:
                self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(None, param.token, None, 'PARAM', left_node=nodo))
        if self.active_scope['method_name'] is None:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.generate(method, len(params), None, 'Function', left_node=nodo))
        else:
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(method, len(params), None, 'Function', left_node=nodo))
        # store R en a temp
        if method_return != 'SELF_TYPE':
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate('R', None, None, 'Assign_temp', left_node=nodo))
            nodo.generate_r = self.get_active_temp()
        return nodo
    
    def visitAttributesDeclaration(self, ctx:yaplParser.AttributesDeclarationContext):
        idx = ctx.ID_VAR().getText()
        typex = ctx.TYPE_IDENTIFIER().getText()
        expression = self.visit(ctx.expr()) if ctx.expr() is not None else None
        nodo = AttrNode(idx, typex, expression)
        nodo.line = ctx.ID_VAR().symbol.line
        nodo.type = typex
        nodo.token = idx
        return nodo
        
    def visitLet(self, ctx:yaplParser.LetContext):
        params = []
        for i in range(len(ctx.var_typescript())):
            p = self.visit(ctx.var_typescript(i))
            params.append(p)
            # * Generacion de codigo intermedio
            # asignamos el valor por defecto de cada variable
            if self.active_scope['method_name'] is None:
                self.intermediate[self.active_scope['class_name']].attributes.append(self.store_attribute(p.idx, p.value, 'Assign'))
            else:
                self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.store_attribute(p.idx, p.value.token, 'Assign'))
        body = self.visit(ctx.expr())
        # self._addSimbolToTable(self.active_scope, body)
        nodo = LetNode(params, body)
        nodo.line = ctx.LET().symbol.line
        nodo.type = self._get_super_type(list(params) + [body])
        nodo.token = " ".join([p.token for p in params])
        return nodo
    
    def visitParen(self, ctx:yaplParser.ParenContext):
        body = self.visit(ctx.expr())
        return body
    
    def visitIsvoid(self, ctx:yaplParser.IsvoidContext):
        expr = self.visit(ctx.expr())
        # value = self._check_for_use_id(expr)
        nodo = IsVoidNode(expr, 'false')
        nodo.line = ctx.ISVOID().symbol.line
        # * Generacion de codigo intermedio
        # ! AGREGAR A LA TABLA LA R AQUI!
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(f'ISVOID {expr.token}', None, None, 'Assign_temp', left_node=nodo))
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
        # * Genearion de codigo intermedio
        if isinstance(my_var, (IntegerNode, BooleanNode, BooleanNode)):
            # generate a temp for this
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(my_var.token, None, None, 'Assign_temp', left_node=nodo))
        for param in args:
            if isinstance(param,  (DispatchNode, BiOperationNode)):
                self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(None, self.get_active_temp(), None, 'PARAM', left_node=nodo))
            else:
                self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(None, param.token, None, 'PARAM', left_node=nodo))
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate(methodCall, len(args), None, 'Function', left_node=nodo))
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate('R', None, None, 'Assign_temp', left_node=nodo))
        nodo.generate_r = self.get_active_temp()
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
        # * Generacion de codigo intermedio
        # Si body tiene statements que jale el ultimo
        if typex == 'Object':
            # ! LA MEMORIA SERIA LA DE OBJECT
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, 'Object', _type='Return'))
        elif typex.lower() == 'self_type':
            # ! LA MEMORIA SERIA LA DE SELF_TYPE
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, 'SELF', _type='Return'))
        elif isinstance(body, BlockNode):
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, body.statements[-1].token, _type='Return'))
        elif isinstance(body, (DispatchNode)):
            # ! FALTA AGREGAR A LA TABLA LA R AQUI!
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, 'R', _type='Return'))
        elif body.token == '':
            # ! FALTA AGREGAR A LA TABLA LA R AQUI!
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, 'R', _type='Return'))
        else:
            # return_value = body.token if body.token else 
            self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(Quadruple(None, None, None, body.token, _type='Return'))
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
        # * generar el codigo intermedio
        # ! GUARDAR EN LA TABLA DE SIMBOLOS A DONDE ESTA EL TIPO DE TYPEX!
        self.intermediate[self.active_scope['class_name']].methods[self.active_scope['method_name']].append(self.generate('Object', None, None, 'Assign_temp', left_node=nodo))
        return nodo

    def visitAttr(self, ctx:yaplParser.AttrContext):
        idx = ctx.ID_VAR().getText()
        typex = ctx.TYPE_IDENTIFIER().getText()
        expression = self.visit(ctx.expr()) if ctx.expr() is not None else None
        nodo = AttrNode(idx, typex, expression)
        nodo.line = ctx.ID_VAR().symbol.line
        nodo.type = typex
        nodo.token = idx
        # * Intermediate code
        if isinstance(expression, (IntegerNode, StringNode, BooleanNode, IdNode)):
            self.intermediate[self.active_scope['class_name']].attributes.append(self.store_attribute(idx, expression.token, 'Assign'))
        elif not expression:
            value = self.defaultValue(typex)
            self.intermediate[self.active_scope['class_name']].attributes.append(self.store_attribute(idx, value, 'Assign'))
        else:
            self.intermediate[self.active_scope['class_name']].attributes.append(self.store_attribute(idx, self.get_active_temp(), 'Assign'))
        return nodo
            
    def defaultValue(self, type_: str):
        if type_ == 'String':
            return ''
        elif type_ == 'Int':
            return 0
        elif type_ == 'Bool':
            return False
        else:
            return 'Object'
