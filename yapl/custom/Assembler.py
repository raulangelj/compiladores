from yapl.custom.intermediate.IntermediateClass import *

class Utils():
    def __init__(self):
        pass

    def is_number(self, number: str):
        try:
            float(number)
            return True
        except ValueError:
            return False

class Assembler():
    def __init__(self, CI: dict[str, IntermediateClass] = {}):
        self.ci = CI
        self.assembly = ''
        self.utils = Utils()

    def load_variables(self, var: str, temp: str) -> str:
        result = ''
        if self.utils.is_number(var):
            result += f'li {temp}, {var}\n'
        else:
            result += f'lw {temp}, {var}\n'
        return result

    def assemble_quadruple(self, quadruple: Quadruple) -> str:
        result_assembly = ''
        if quadruple.type == 'Quadruple':
            if quadruple.op == '+':
                result_assembly += self.load_variables(quadruple.left, '$t0')
                result_assembly += self.load_variables(quadruple.right, '$t1')
                result_assembly += f'add {quadruple.result}, $t0, $t1\n'
                # result_assembly += f'sw {quadruple.result}, {quadruple.result}\n'
            elif quadruple.op == '-':
                result_assembly += self.load_variables(quadruple.left, '$t0')
                result_assembly += self.load_variables(quadruple.right, '$t1')
                result_assembly += f'sub {quadruple.result}, $t0, $t1\n'
                # result_assembly += f'sw {quadruple.result}, {quadruple.result}\n'
            elif quadruple.op == '*':
                result_assembly += self.load_variables(quadruple.left, '$t0')
                result_assembly += self.load_variables(quadruple.right, '$t1')
                result_assembly += f'mul {quadruple.result}, $t0, $t1\n'
                # result_assembly += f'sw {quadruple.result}, {quadruple.result}\n'
            elif quadruple.op == '/':
                result_assembly += self.load_variables(quadruple.left, '$t0')
                result_assembly += self.load_variables(quadruple.right, '$t1')
                result_assembly += f'div {quadruple.result}, $t0, $t1\n'
                # result_assembly += f'sw {quadruple.result}, {quadruple.result}\n'
        return result_assembly

    def generate_code(self):
        assembly = ''
        for classs in self.ci:
            # store variables
            for var_quadruple in self.ci[classs].attributes:
                assembly += self.assemble_quadruple(var_quadruple)
            # go inside methods
            for method in self.ci[classs].methods:
                for quadruple in self.ci[classs].methods[method]:
                    assembly += self.assemble_quadruple(quadruple)

        print('========== ASSEMBLY ==========')
        print(assembly)
