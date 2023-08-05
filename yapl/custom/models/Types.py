from typing import List

# every class is a type
class Attribute():
    def __init__(self, name: str, _type: str):
        self.name = name
        self.type = _type

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name and self.type == __value.type


class Method():
    def __init__(self, name: str, return_type: str, params: List[Attribute]):
        self.name = name
        self.return_type = return_type
        self.params = params

    def __eq__(self, __value: object) -> bool:
        return self.params == __value.params and self.return_type == __value.return_type

class Klass():
    def __init__(self, name: str, parent: str = 'object'):
        self.name = name
        self.parent = parent
        self.attributes = {}
        self.methods = {}

    def get_attribute(self, name: str) -> Attribute:
        return self.attributes[name] if name in self.attributes else None
        
    def getMethod(self, name: str) -> Method:
        return self.methods[name] if name in self.methods else None
        
    def define_attribute(self, name: str, _type: str):
        self.attributes[name] = Attribute(name, _type)

    def define_method(self, name: str, return_type: str, params: List[List[str]]):
        params_list = [Attribute(param[0], param[1]) for param in params]
        self.methods[name] = Method(name, return_type, params_list)



    
