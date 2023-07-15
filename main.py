from antlr4 import *
from dist.ExprLexer import ExprLexer
from dist.ExprParser import ExprParser

def main():
    # Create an input stream from the expression
    expression = "2*(3+4)"
    input_stream = InputStream(expression)

    # Create a lexer and token stream
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Create a parser and specify the token stream
    parser = ExprParser(token_stream)

    # Parse the expression and get the parse tree
    parse_tree = parser.expr()

    # Print the parse tree
    print(parse_tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()