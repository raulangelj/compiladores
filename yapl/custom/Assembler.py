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
        self.types = []
        self.params = {}
        self.quadruple_array = []
        self.spaces = {}
        self.default_functions = {
            "out_string": "out_string:\n\tli $v0, 4\n\tsyscall\n\tjr $ra",
            "substring": '''
substring:
    add  $t0, $zero, $zero  # $t0 = current index
    add  $t1, $zero, $a1    # $t1 = start index
    add  $t2, $zero, $a2    # $t2 = length
    add  $t3, $zero, $a0    # $t3 = pointer to current char in source string
    add  $t4, $zero, $a3    # $t4 = pointer to current char in destination string

    # Loop until we reach the start index
    bge  $t0, $t1, start_copying
    addi $t0, $t0, 1
    addi $t3, $t3, 1
    j    substring

start_copying:
    # Copy characters until length is 0 or we reach the end of the source string
    beq  $t2, $zero, end_substring
    lb   $t5, 0($t3)
    beq  $t5, $zero, end_substring
    sb   $t5, 0($t4)
    addi $t3, $t3, 1
    addi $t4, $t4, 1
    addi $t2, $t2, -1
    j    start_copying

end_substring:
    # Null-terminate the destination string
    sb   $zero, 0($t4)
    jr   $ra  # Return to the caller
'''
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
        self.quadruple_array.append(quadruple)
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
            # self.params[quadruple.result]
            self.param_counter += 1
            self.variable_counter += 1
        elif quadruple.type == 'Function':
            if quadruple.left == 'type_name':
                before_value = self.quadruple_array[-2]
                classs = before_value.left
                self.data[classs] = classs
                self.types.append(classs)
                self.spaces[f'{classs}_dest'] = len(classs)
            elif quadruple.left == 'substr':
                # la   $a0, sourceString  # Address of the source string
                # li   $a1, 7             # Start index for the substring
                # li   $a2, 5             # Length of the substring
                # la   $a3, destString    # Address of the destination string

                # jal  substring          # Call substring function
                result_assembly += f'\tla $a0, {self.types[-1]}\n'
                firvarName = f'param{self.param_counter - 2}'
                seconvarName = f'param{self.param_counter - 1}'
                thirdvarName = f'{self.types[-1]}_dest'
                result_assembly += f'\tli $a1, {self.data[firvarName]}\n'
                result_assembly += f'\tli $a2, {self.data[seconvarName]}\n'
                result_assembly += f'\tla $a3, {self.spaces[thirdvarName]}\n'
                result_assembly += f'\tjal substring\n'
            else:
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
        # add spaces
        for space in self.spaces:
            assembly += f'\t{space}: .space {self.spaces[space]}\n'


        print('========== ASSEMBLY ==========')
        print(assembly)
        return assembly
