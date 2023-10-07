import sys
import os
from antlr4 import *
from yapl.grammar.yaplLexer import yaplLexer
from yapl.grammar.yaplParser import yaplParser
from yapl.custom.YaplVisitorCustom import YaplVisitorCustom
from yapl.custom.visitorDefinition import VisitorDefinition
from yapl.custom.IntemediateVisitor import IntermediateVisitor
from antlr4.tree.Trees import Trees
from yapl.custom.ErrorsListener import ErrorListener
from termcolor import colored

def print_all_tokens(token_stream):
    for i in token_stream.tokens:
        if i.type == yaplLexer.ERROR:
            print(colored(f"ERROR: Bad token at line: {i.line} : {i.column}", 'red'))
        else:
            print(i)

def main():
    if len(sys.argv) < 2:
        raise Exception("ERROR: A FILE *.yapl must be pass.\nUsage: main.py <input file>")

    # Load grammar
    try:
        file = sys.argv[1]
        input_stream = FileStream(file)
    except Exception as e:
        raise Exception(f"ERROR: opening the file {file}") from e

    # lexer
    lexer = yaplLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    error_listener_lexer = ErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener_lexer)

    # parser
    parser = yaplParser(token_stream)
    error_listener_parser = ErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener_parser)
    tree = parser.program()

    # display parse tree in text form
    # TODO: add flag -tree
    # print(Trees.toStringTree(tree, None, parser))
    # print_all_tokens(token_stream)

    visitor = VisitorDefinition()
    visitor.visit(tree)
    visitor.show_variables_table()
    visitor.show_classes_table()

    semanticsVisitor = YaplVisitorCustom()
    semanticsVisitor.types = visitor.types
    semanticsVisitor.errors = visitor.errors
    program = semanticsVisitor.visit(tree)

    print(colored("The program is correct", 'green'))
    semanticsVisitor.show_variables_table()
    semanticsVisitor.show_classes_table()

    # visitor = YaplVisitorCustom()
    # program = visitor.visit(tree)

    # Semantic erros
    if len(visitor.errors) > 0:
        print(colored(f"ERROR: The program has {len(visitor.errors)} SEMANTIC errors", 'red'))
        for error in visitor.errors:
            print(colored(error.message, 'red'))
        exit(1)
    
    if error_listener_lexer.true or error_listener_parser.true:
        print(colored("ERROR: The program has LEXIC errors", 'red'))
        for error in error_listener_lexer.errors:
            print(colored(error, 'red'))
        for error in error_listener_parser.errors:
            print(colored(error, 'red'))
        exit(1)

    intermediateVisitor = IntermediateVisitor()
    intermediateVisitor.types = semanticsVisitor.types
    intermediateVisitor.visit(tree)
    intermediateVisitor.print_intermediate()
    intermediateVisitor.show_variables_table()
    intermediateVisitor.show_classes_table()

    # display parse tree in GUI
    # TODO: add flag -gui
    command = f'antlr4-parse grammar/yapl.g4 program -gui'
    process = os.popen(command, 'w')
    process.write(input_stream.strdata)
    process.close()

def evaluate_code(code: str):
    success = 1
    errors = {}
    # lexer
    lexer = yaplLexer(code)
    token_stream = CommonTokenStream(lexer)
    error_listener_lexer = ErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener_lexer)

    # parser
    parser = yaplParser(token_stream)
    error_listener_parser = ErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener_parser)
    tree = parser.program()

    # display parse tree in text form
    # TODO: add flag -tree
    # print(Trees.toStringTree(tree, None, parser))
    # print_all_tokens(token_stream)

    visitor = VisitorDefinition()
    visitor.visit(tree)
    visitor.show_variables_table()
    visitor.show_classes_table()

    semanticsVisitor = YaplVisitorCustom()
    semanticsVisitor.types = visitor.types
    semanticsVisitor.errors = visitor.errors
    program = semanticsVisitor.visit(tree)

    # visitor = YaplVisitorCustom()
    # program = visitor.visit(tree)

    # Semantic erros
    if len(visitor.errors) > 0:
        success = 0
        print(colored(f"ERROR: The program has {len(visitor.errors)} SEMANTIC errors", 'red'))
        error_array = []
        for i in visitor.errors:
            error_array.append(i.message + '\n')
        errors['semantic'] = error_array
    
    if error_listener_lexer.true or error_listener_parser.true:
        success = 0
        print(colored("ERROR: The program has LEXIC errors", 'red'))
        errors['lexical'] = error_listener_lexer.errors + error_listener_parser.errors

    return [success, errors]

if __name__ == '__main__':
    main()