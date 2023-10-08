from typing import List
from yapl.custom.models.Types import Attribute
from Constant import *
class ErrorNode():
    def __init__(self):
        self.type = 'Error'
        self.message = None
    
    def get_error(self, left, right, operator, line = ""):
        self.message = f"Error on line {line}: unsupported operation {operator}: in between {left.type} and {right.type}"

class Node():
    def __init__(self):
        self.type = None
        self.token = ''
        self.line = None
        self.width = 0

class BiOperationNode(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

class AssignNode(Node):
    def __init__(self, idx, value):
        super().__init__()
        self.idx = idx
        self.value = value

class LetNode(Node):
    def __init__(self, idx, _type, value):
        super().__init__()
        self.idx = idx
        self.type = _type
        self.value = value

class AttrNode(Node):
    def __init__(self, idx, _type, value = None):
        super().__init__()
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
        super().__init__()
        self.statements = statements

class MethodNode(Node):
    def __init__(self, name, params: List[Attribute], return_type, body):
        super().__init__()
        self.name = name
        self.params = params
        self.return_type = return_type
        self.body = body

class AttributesDeclarationNode(AttrNode):
    def __init__(self, idx, _type, value = None):
        super().__init__(idx, _type, value)


class ClassNode(Node):
    def __init__(self, name, inheritence, features):
        super().__init__()
        self.name = name
        self.inheritence = inheritence
        self.features = features
        

class IntegerNode(Node):
    def __init__(self, token):
        super().__init__()
        self.token = token
        self.type = 'Int'
        self.width = INT_SIZE

class StringNode(Node):
    def __init__(self, token):
        super().__init__()
        self.token = token
        self.type = 'String'
        self.width = CHAR_SIZE * len(token)

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
        super().__init__()
        self.token = token
        # self.type = 'Not'
        self.type = 'Bool'

class NegativeNode(Node):
    def __init__(self, value, token):
        super().__init__()
        self.value = value
        self.type = 'Negative'
        self.token = token

class BooleanNode(Node):
    def __init__(self, token):
        super().__init__()
        self.token = token
        self.operator = '!'
        self.type = 'Bool'
        self.width = BOOL_SIZE

class IdNode(Node):
    def __init__(self, token):
        super().__init__()
        self.token = token
        self.type = 'Id'

class IfNode(Node):
    def __init__(self, condition, then_body, else_body):
        super().__init__()
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body
        self.generate_r = False

class WhileNode(Node):
    def __init__(self, condition, body):
        super().__init__()
        self.condition = condition
        self.expression = body

class ParamNode(Node):
    def __init__(self, idx, _type):
        super().__init__()
        self.idx = idx
        self.type = _type

class NewNode(Node):
    def __init__(self, typex):
        super().__init__()
        self.type = typex
        self.token = f'NEW {typex}'

class MethodCallNode(Node): # expr named functionCall
    def __init__(self, obj, method, params):
        super().__init__()
        self.obj = obj
        self.method = method
        self.params = params
        self.return_var = None

class LetNode(Node):
    def __init__(self, param_list, expr):
        super().__init__()
        self.param_list = param_list
        self.expr = expr


class DispatchNode(Node): # for method dispatch or methodCall
    def __init__(self, parent, method, args, expr, type_):
        super().__init__()
        self.parent = parent
        self.method = method
        self.args = args
        self.expr = expr
        self.type = type_

class IsVoidNode(Node):
    def __init__(self, expr, value):
        super().__init__()
        self.expr = expr
        self.type = 'Bool'
        self.value = value

class ProgramNode(Node):
    def __init__(self, classes):
        super().__init__()
        self.classes = classes