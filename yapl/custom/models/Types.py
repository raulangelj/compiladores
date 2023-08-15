from typing import List, Literal, TypedDict

# every class is a type
class Attribute():
    def __init__(self, name: str, _type: str, value: str = None):
        self.name = name
        self.type = _type
        self.value = value

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name and self.type == __value.type


class Method():
    def __init__(self, name: str, return_type: str, params: List[Attribute]):
        self.name = name
        self.return_type = return_type
        self.params = params

    def __eq__(self, __value: object) -> bool:
        return self.params == __value.params and self.return_type == __value.return_type
    
class ScopeType(TypedDict):
    class_name: str
    method_name: str

class Klass():
    def __init__(self, name: str, scope: ScopeType = None, _type: Literal['class', 'var'] = 'class', inheritance: str = None, value = None, node = None):
        # TODO refactorizar, crear una class klass y otra var que herede de Type que es esta
        self.name = name
        self.scope = scope
        self.type = _type
        self.inheritance = inheritance # * is the type of var or class
        self.node = node
        self.attributes = {} # ! only for class
        self.methods = {} #! only for class
        if _type == 'var':
            self.value = value if value else self._default_type()

    def get_attribute(self, name: str) -> Attribute:
        return self.attributes[name] if name in self.attributes else None
        
    def getMethod(self, name: str) -> Method:
        return self.methods[name] if name in self.methods else None
        
    def define_attribute(self, name: str, _type: str, value):
        self.attributes[name] = Attribute(name, _type, value)

    def define_method(self, name: str, return_type: str, params: List[Attribute]):
        # params_list = [Attribute(param[0], param[1]) for param in params]
        self.methods[name] = Method(name, return_type, params)

    def get_methods_names(self) -> List[str]:
        return list(self.methods.keys())
    
    def get_attributes_names(self) -> List[str]:
        return list(self.attributes.keys())
    
    def _default_type(self):
        if self.inheritance == 'Int':
            return 0
        elif self.inheritance == 'String':
            return ''
        elif self.inheritance == 'Bool':
            return False
        else:
            return None
    
