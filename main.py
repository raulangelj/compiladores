import sys
import os
from antlr4 import *
from antlr4 import *
from dist.grammar.yaplLexer import yaplLexer
from dist.grammar.yaplParser import yaplParser
from dist.grammar.yaplListener import yaplListener
from antlr4.tree.Trees import Trees

def main():
    # if len(sys.argv) < 2:
    #     print("ERROR: A FILE *.yapl must be pass.\nUsage: main.py <input file>")
    #     exit(0)
    # Load grammar
    try:
        # file = sys.argv[1]
        file = '.\\tests\simple.yapl'
        input_stream = FileStream(file)
        
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

        listener = yaplListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
    except Exception as e:
        raise Exception(f"ERROR: The file {file} does not exist.", e)
    # # Create an input stream from the expression
    # expression = "2*(3+4)"
    # input_stream = InputStream(expression)

    # # Create a lexer and token stream
    # lexer = ExprLexer(input_stream)
    # token_stream = CommonTokenStream(lexer)

    # # Create a parser and specify the token stream
    # parser = ExprParser(token_stream)

    # # Parse the expression and get the parse tree
    # parse_tree = parser.expr()

    # # Print the parse tree
    # print(parse_tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()