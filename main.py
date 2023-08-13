import sys
import os
from antlr4 import *
from yapl.grammar.yaplLexer import yaplLexer
from yapl.grammar.yaplParser import yaplParser
from yapl.custom.YaplVisitorCustom import YaplVisitorCustom
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

    visitor = YaplVisitorCustom()
    program = visitor.visit(tree)

    visitor.show_variables_table()
    visitor.show_classes_table()
    visitor.check_global_semantics()
    # Semantic erros
    if len(visitor.errors) > 0:
        print(colored(f"ERROR: The program has {len(visitor.errors)} SEMANTIC errors", 'red'))
        for error in visitor.errors:
            print(colored(error.message, 'red'))
        exit(1)
    
    if error_listener_lexer.true or error_listener_parser.true:
        print(colored("ERROR: The program has LEXIC errors", 'red'))
        exit(1)

    # display parse tree in GUI
    # TODO: add flag -gui
    command = f'antlr4-parse grammar/yapl.g4 program -gui'
    process = os.popen(command, 'w')
    process.write(input_stream.strdata)
    process.close()

if __name__ == '__main__':
    main()