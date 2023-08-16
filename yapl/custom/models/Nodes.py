from typing import List
from yapl.custom.models.Types import Attribute
class ErrorNode():
    def __init__(self):
        self.type = 'Error'
        self.message = None
    
    def get_error(self, left, right, operator, line = ""):
        self.message = f"Error on line {line}: unsupported operation {operator}: in between {left.type} and {right.type}"

class Node():
    def __init__(self):
        self.type = None
        self.line = None

class BiOperationNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class AssignNode(Node):
    def __init__(self, idx, value):
        self.idx = idx
        self.value = value

class LetNode(Node):
    def __init__(self, idx, _type, value):
        self.idx = idx
        self.type = _type
        self.value = value

class AttrNode(Node):
    def __init__(self, idx, _type, value = None):
        self.idx = idx
        self.type = _type
        if not value:
            self.set_default_value()
        else:
            self.value = value
        
    def set_default_value(self):
        if self.type == 'Int':
            self.value = IntegerNode(0)
        elif self.type == 'String':
            self.value = StringNode('')
        elif self.type == 'Bool':
            self.value = BooleanNode(False)
        else:
            self.value = None 

class BlockNode(Node):
    def __init__(self, statements):
        self.statements = statements

class MethodNode(Node):
    def __init__(self, name, params: List[Attribute], return_type, body):
        self.name = name
        self.params = params
        self.return_type = return_type
        self.body = body

class AttributesDeclarationNode(AttrNode):
    def __init__(self, idx, _type, value = None):
        super().__init__(idx, _type, value)


class ClassNode(Node):
    def __init__(self, name, inheritence, features):
        self.name = name
        self.inheritence = inheritence
        self.features = features
        

class IntegerNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = 'Int'

class StringNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = 'String'

class PlusNode(BiOperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operator = '+'
        self.type = 'Int'

class MinusNode(BiOperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operator = '-'
        self.type = 'Int'

class DivNode(BiOperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operator = '/'
        self.type = 'Int'

class MultNode(BiOperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operator = '*'
        self.type = 'Int'

class LessThanNode(BiOperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operator = '<'
        self.type = 'Bool'

class LessEqualNode(BiOperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operator = '<='
        self.type = 'Bool'
    
class EqualNode(BiOperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operator = '='
        self.type = 'Bool'

class NotNode(Node):
    def __init__(self, token):
        self.token = token
        # self.type = 'Not'
        self.type = 'Bool'

class NegativeNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = 'Negative'

class BooleanNode(Node):
    def __init__(self, token):
        self.token = token
        self.operator = '!'
        self.type = 'Bool'

class IdNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = 'Id'

class IfNode(Node):
    def __init__(self, condition, then_body, else_body):
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body

class WhileNode(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.expression = body

class ParamNode(Node):
    def __init__(self, idx, _type):
        self.idx = idx
        self.type = _type

class NewNode(Node):
    def __init__(self, typex):
        self.type = typex
        self.token = f'NEW {typex}'

class MethodCallNode(Node): # expr named functionCall
    def __init__(self, obj, method, params):
        self.obj = obj
        self.method = method
        self.params = params

class LetNode(Node):
    def __init__(self, param_list, expr):
        self.param_list = param_list
        self.expr = expr


class DispatchNode(Node): # for method dispatch or methodCall
    def __init__(self, typex, method, args, expr):
        self.type = typex
        self.method = method
        self.args = args
        self.expr = expr