
class ErrorNode():
    def __init__(self):
        self.type = 'Error'
        self.message = None
    
    def get_error(self, left, right, operator):
        self.message = f"Unsupported operation {operator}: in between {left.type} and {right.type}"

class Node():
    def __init__(self):
        self.type = None

class BiOperationNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class IntegerNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = 'Integer'

class StringNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = 'String'

class PlusNode(BiOperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operator = '+'
        self.type = 'Integer'

class MinusNode(BiOperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operator = '-'
        self.type = 'Integer'

class DivNode(BiOperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operator = '/'
        self.type = 'Integer'

class MultNode(BiOperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.operator = '*'
        self.type = 'Integer'

class BooleanNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = 'Boolean'