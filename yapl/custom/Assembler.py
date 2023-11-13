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
        self.param_counter = 0
        self.variable_counter = 0
        self.data = {}
        self.default_functions = {
            "out_string": "out_string:\n\tli $v0, 4\n\tsyscall\n\tjr $ra"
        }

    def adapta_special_characters(self, string: str) -> str:
        # if in the string there is a \n or \t, replace it with \\n or \\t
        string = string.replace('\n', '\\n')
        string = string.replace('\t', '\\t')
        return string

    def load_variables(self, var: str, temp: str) -> str:
        result = ''
        if self.utils.is_number(var):
            result += f'\tli {temp}, {var}\n'
        else:
            result += f'\tla {temp}, {var}\n'
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
        elif quadruple.type == 'PARAM':
            result_assembly += self.load_variables(f'param{self.variable_counter}', f'$a{self.param_counter}')
            self.data[f'param{self.variable_counter}'] = quadruple.result
            self.param_counter += 1
            self.variable_counter += 1
        elif quadruple.type == 'Function':
            result_assembly += f'\tjal {quadruple.left}\n'
            self.param_counter = 0
        return result_assembly

    def generate_code(self):
        assembly = ''
        for classs in self.ci:
            # store variables
            for var_quadruple in self.ci[classs].attributes:
                assembly += self.assemble_quadruple(var_quadruple)
            # go inside methods
            assembly += '.text\n\n'
            for method in self.ci[classs].methods:
                assembly += method + ':\n'
                for quadruple in self.ci[classs].methods[method]:
                    assembly += self.assemble_quadruple(quadruple)
                if method == 'main':
                    assembly += '\tli $v0, 10\n\tsyscall\n'
        # add default functions
        for function in self.default_functions:
            assembly += self.default_functions[function] + '\n'
        # add data
        assembly += '.data\n'
        for data in self.data:
            if type(self.data[data]) == str:
                assembly += f'\t{data}: .asciiz "{self.data[data]}"\n'
            else:
                assembly += f'\t{data}: .word {self.data[data]}\n'


        print('========== ASSEMBLY ==========')
        print(assembly)
