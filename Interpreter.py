from Lexer.Lexer import Lexer
from Parser.Parser import Parser


def Run(code, input_type):
    if input_type == "<stdin>":
        lexer = Lexer(code, input_type)
        tokens, error = lexer.tokenize()
        print(f'Tokens: {tokens}')
        if error:
            return None, error
        else:
            parser = Parser(tokens)
            blocks, err = parser.parse()
            if err:
                return None, err
            else:
                return blocks, None
    elif input_type == "<stdout>":
        return "done", None
