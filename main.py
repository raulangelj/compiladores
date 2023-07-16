import sys
import os
from antlr4 import *
from antlr4 import *
from dist.grammar.yaplLexer import yaplLexer
from dist.grammar.yaplParser import yaplParser
from dist.grammar.yaplListener import yaplListener
from antlr4.tree.Trees import Trees

def main():
    if len(sys.argv) < 2:
        raise Exception("ERROR: A FILE *.yapl must be pass.\nUsage: main.py <input file>")

    # Load grammar
    try:
        file = sys.argv[1]
        input_stream = FileStream(file)
    except Exception as e:
        raise Exception(f"ERROR: openong the file {file}") from e

    # lexer
    lexer = yaplLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # parser
    parser = yaplParser(token_stream)
    tree = parser.program()

    # display parse tree in text form
    print(Trees.toStringTree(tree, None, parser))

    # display parse tree in GUI
    command = f'antlr4-parse .\\grammar\\yapl.g4 program -gui'
    process = os.popen(command, 'w')
    process.write(input_stream.strdata)
    process.close()

if __name__ == '__main__':
    main()