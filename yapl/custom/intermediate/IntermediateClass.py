
class Quadruple():
    def __init__(self, op: str, left: str, right: str, result: str, _type: str = 'Quadruple'):
        self.op = op
        self.left = left
        self.right = right
        self.result = result
        self.type = _type

    def __str__(self):
        # 'Assign', 'Quadriple', 'Goto', 'If', 'Label
        if self.type == 'Assign':
            return f'{self.result} = {self.left}'
        elif self.type == 'If':
            return f'if {self.left} goto {self.result}'
        elif self.type == 'PARAM':
            return f'PARAM {self.result}'
        elif self.type == 'Function':
            return f'CALL {self.left}, {self.right}'
        elif self.type == 'Label':
            return f'{self.result}'
        elif self.type == 'Goto':
            return f'goto {self.result}'
        return f'{self.result} = {self.left} {self.op} {self.right}'


class IntermediateClass():
    def __init__(self, name: str):
        self.name = name
        self.attributes: list[Quadruple] = []
        self.methods = {}
        self.locals = {}
        self.width = 0

    def get_method(self, name: str):
        return self.methods[name] if name in self.methods else None
    
    def add_method(self, name: str, method: [Quadruple]):
        self.methods[name] = method

    def add_attribute(self, name: str, attribute: [Quadruple]):
        self.attributes[name] = attribute