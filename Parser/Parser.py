from var.Errors import UnknownSyntaxError, InvalidSyntaxError
from var.Objects import Token, Condition, TableColumnNavigation

TOKENS = {'use': "TT_USE", 'using': "TT_USING", 'create': "TT_CREATE", 'drop': "TT_DROP", 'inform': "TT_INFORM",
          'alter': "TT_ALTER", 'rename': "TT_REN", 'add': "TT_ADD", 'to': "TT_TO", 'database': "TT_DB",
          'select': "TT_SELECT", 'table': "TT_TBL", 'column': "TT_CLN", 'insert': "TT_INSERT", "into": "TT_INTO",
          'values': "TT_VAL", 'from': "TT_FRM", 'help': "TT_HELP", 'set': "TT_SET", 'where': "TT_WHERE",
          'update': "TT_UPDT", 'delete': "TT_DLT", 'inner': "TT_INNER", 'join': "TT_JOIN"}

DATATYPES = {'integer': "DT_INT", 'varchar': "DT_VARCHAR", 'boolean': "DT_BOOL", 'float': "DT_FLT"}

CONDITIONS = {'==': "CT_EQUAL", '>': "CT_GREATER", '<': "CT_LOWER", '<=': "CT_LSEQ", '>=': "CT_GRTEQ",
              '<>': "CT_NTEQ"}
"""
== indicates to check on equality
= sets one to the other -- was deprecated in version 0.0.3 since it doesnt really qualify to be a condition

e.g -- left-node == right-node -if left-node is equal to right-node-,
 while left-node = right-node -set left-node to right-node-
"""
METACOMMANDS = {'exit': "EXIT"}


class Parser:
    """
    The Parser

    this is where majority of token conversion take place,
    Converting into a syntax (blocks) that the interpreter can understand

    tokens received are categorised into 5 token types
    variable tuple,
    token,
    variable string,
    data type,
    condition symbol

    Each variable is added to a token as its value or as its secondary value
    Data types and Tokens are grouped into one conditional clause due to their similarities

    Conditional Symbols are different in architecture and have two nodes left and right,
    they wait inside the string variable to be instantiated and pick from their its nodes when the next
    token happens to be a conditional symbol

    For the lexer to work, priorities are given since the difference between each category is purely virtual and depends
    on its location in the code.
    1st Priority = Tuples -- This is as a result of preventing an error when we try to lower our code for comparisons
    2nd Priority = Tokens -- As a result of a virtual difference between tokens and strings
    3rd Priority = Strings and Conditional Symbols --
    3rd Virtual-Priority = "." Symbol -- To check for join statements and Meta commands
    4th Priority = SQL Datatypes --

    3rd Virtual-Priority
    "." is Recognized as a Navigational symbol and a meta command starter but doesn't necessitate a  new priority
    hence just  3rd virtual-Priority

    `Stephen Telian`
    """
    position = -1
    current_token = None

    def __init__(self, tokens):
        self.tokens = tokens
        self.advance()

    def advance(self):
        self.position += 1
        self.current_token = self.tokens[self.position] if self.position < len(self.tokens) else None

    def parse(self):
        """
        This here starts the processes of Parsing through all Token Types

        """
        """ For the final product"""
        blocks = []

        """ A Temporary Holder"""
        temp = None

        """ For Login in Previous token -types"""
        previous_token_priority_type = None
        while self.current_token is not None:
            if type(self.current_token) == tuple:
                """Tuple handling as First Priority"""
                if previous_token_priority_type == "second":
                    """Indicating that it is a value of a Token"""
                    temp.addValue(self.current_token)
                elif previous_token_priority_type == "third":
                    """Indicating that it is a value of a token after a primary value of string had already been 
                    identified """
                    temp.addValue(self.current_token)
                elif previous_token_priority_type == "first":
                    """Handling Multiple Tuples"""
                    temp.addValue(self.current_token)
                previous_token_priority_type = "first"
                self.advance()
            elif self.current_token.lower() in TOKENS:
                """Replace the Token into the standardized A-SQL Syntax"""
                tok = TOKENS[self.current_token.lower()]
                if previous_token_priority_type == "second":
                    blocks.append(temp)  # whatever was originally inside temp is added into blocks
                    temp = Token(tok)  # New Temp
                elif previous_token_priority_type is None:
                    temp = Token(tok)  # if this is the first token to be encountered
                elif previous_token_priority_type == "third" or previous_token_priority_type == "first":
                    """If the previous token type is either a string or a tuple"""
                    blocks.append(temp)
                    temp = Token(tok)
                previous_token_priority_type = "second"
                self.advance()
            elif type(self.current_token) == str and self.current_token != "." or self.current_token in CONDITIONS:
                if previous_token_priority_type == "second":
                    """ If previous token was an ASQL syntax type """
                    if self.current_token not in CONDITIONS:
                        temp.addValue(self.current_token)
                elif previous_token_priority_type is None:
                    """This implies that only a condition or un unknown string was passed hence raising an error"""
                    return None, UnknownSyntaxError(self.current_token)
                elif previous_token_priority_type == "third":
                    """Conditional Symbols are instantiated here"""
                    if self.current_token in CONDITIONS:
                        tok = CONDITIONS[self.current_token]
                        self.advance()
                        temp.changeLastValue(Condition(tok, temp.lastValue(), self.current_token))
                    elif type(temp.lastValue()) is Condition or type(temp.lastValue()) is list:
                        left_node = self.current_token

                        self.advance()
                        if self.current_token in CONDITIONS:
                            tok = CONDITIONS[self.current_token]
                            self.advance()
                            temp.addValue(Condition(tok, left_node, self.current_token))
                    else:
                        """ Multiple Strings"""
                        if temp is None:
                            return None, InvalidSyntaxError(self.current_token)
                        elif temp is not None:
                            temp.addValue(self.current_token)
                elif previous_token_priority_type == "first":
                    """If previous token has been identified to be a tuple and the current token is a string or a 
                    condition """
                    pass
                previous_token_priority_type = "third"
                self.advance()
            elif self.current_token == ".":
                if previous_token_priority_type == "first":
                    pass
                if previous_token_priority_type == "second":
                    pass
                if previous_token_priority_type == "third":
                    """Implies that the last token was identified to be a string
                    Strings, are given a token parent hence the string should be in a value"""

                    self.advance()

                    temp.changeLastValue(TableColumnNavigation(temp.lastValue(), self.current_token))
                self.advance()
                previous_token_priority_type = "third"

        blocks.append(temp) if temp is not None else None

        return blocks, None
