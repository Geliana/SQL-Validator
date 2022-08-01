"""
Awino db Lexer
version 1.0.2
Stephen Telian
"""
from Errors import MissingSyntaxError, UnknownSyntaxError
from Objects import DataType

OPENING_PARENTHESIS = "("
CLOSING_PARENTHESIS = ")"
alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = alphabets + alphabets.upper()
DIGITS = "0123456789"
STRING_CHARS = f'\'\"`'
SPACE = " "
END = ";"
COMMA = ","
TAB = "\t"
NEWLINE = "\n"
ACCEPTED_SYMBOLS = "*=().-><"


class Lexer:
    """
    The Lexer

    It breaks down the code letter by letter per every division made by a space, a string-character, or an
    opening parenthesis. it then converts them to either a tuple or a string.
    Anything inside string-characters are left as is and are not formatted (literal)

    In order to perform this there are 4 different modes
    Normal
    Tuple
    nested tuple mode(A tuple within a tuple)
    string
    major division by space mode -- this mode handles multiple non-comma separated syntax inside a tuple e.g ('column_name' INTEGER(255) NOT NULL)

    Tuple Mode implies that a parenthesis has been found and tuple mode wasn't originally active
    if tuple mode was originally active it means it is a nested tuple and a sub-mode (nested_tuple) is initiated
    if the tuple is found with a space inside, a query is made to check for the previous character,
    this initiates another sub-mode that nests a new tuple inside the original tuple

    String mode implies that a string symbol has been found e.g. '"` Everything inside these
    symbols is taken as it is, meaning that they are literal despite anything

    Normal mode is anything in between except nested tuples

    """
    position = -1
    current_char = None
    previous_char = None

    def __init__(self, code, input_type):
        self.code = code
        self.input_type = input_type
        self.advance()

    def advance(self):
        self.position += 1
        self.current_char = self.code[self.position] if self.position < len(self.code) else None
        self.previous_char = self.code[self.position - 1] if self.position > 0 else None

    def tokenize(self):
        # the complete end Result
        tokens = []

        # All Modes
        tuple_mode = False
        string_mode = False
        digit_mode = False
        nested_tuple_mode = False
        major_division_by_space_mode = False

        # All variables
        temp = None
        variable_tuple = []
        variable_string = ""
        temp_holder = []
        nested_tuple_variable = []

        while self.current_char is not None:
            if self.current_char == OPENING_PARENTHESIS:
                """An opening parenthesis has been encountered"""
                if not tuple_mode:
                    tuple_mode = True  # initialise tuple mode
                elif tuple_mode:
                    """Tuple mode was already initiated indicating that a nested tuple has been encountered"""
                    nested_tuple_mode = True
                    if major_division_by_space_mode:
                        temp_holder.append(temp)
                    elif not major_division_by_space_mode:
                        variable_tuple.append(temp)
                    temp = None
                self.advance()
            elif self.current_char == CLOSING_PARENTHESIS:
                if tuple_mode and not nested_tuple_mode:
                    """Implying the ned of a tuple"""
                    tuple_mode = False  # Exit Tuple mode
                    if not major_division_by_space_mode:
                        variable_tuple.append(temp) if temp is not None else None
                        tokens.append(tuple(variable_tuple))
                        variable_tuple = []
                    else:
                        temp_holder.append(temp) if temp is not None else None
                        variable_tuple.append(tuple(temp_holder))
                        tokens.append(tuple(variable_tuple))
                        temp_holder = []
                        variable_tuple = []
                    temp = None
                elif tuple_mode and nested_tuple_mode:
                    """Implying the end of of parsing within a nested tuple"""
                    nested_tuple_mode = False
                    nested_tuple_variable.append(temp)
                    temp = None
                    temp_holder.append(tuple(nested_tuple_variable))
                    nested_tuple_variable = []

                self.advance()
            elif self.current_char in STRING_CHARS:
                """Handles all symbols that represent strings"""
                if not string_mode:
                    string_mode = True  # initialise string mode
                elif string_mode:
                    string_mode = False  # Exit string mode
                    if not tuple_mode:
                        tokens.append(variable_string)
                    elif tuple_mode:
                        variable_tuple.append(variable_string)
                    variable_string = ""
                self.advance()
            elif string_mode:
                variable_string += self.current_char
                self.advance()
            elif not string_mode and self.current_char in ALPHABETS:
                if temp is None:
                    temp = self.current_char
                elif temp is not None:
                    temp += self.current_char
                self.advance()
            elif not string_mode and self.current_char in DIGITS:
                digit_mode = True
                if temp is None:
                    temp = self.current_char
                elif temp is not None:
                    temp += self.current_char
                self.advance()
            elif self.current_char in COMMA:
                if major_division_by_space_mode:
                    major_division_by_space_mode = False
                    temp_holder.append(temp) if temp is not None else None
                    variable_tuple.append(tuple(temp_holder))
                    temp = None
                    temp_holder = []
                self.advance()
            elif self.current_char in SPACE and not string_mode:
                if not tuple_mode:
                    if temp is not None:
                        data = DataType("STRING", temp)
                        tokens.append(data) if temp is not None else None
                        temp = None
                elif tuple_mode:
                    if self.previous_char in COMMA:
                        variable_tuple.append(temp) if temp is not None else None
                        temp = None
                    elif self.previous_char not in COMMA:
                        major_division_by_space_mode = True
                        temp_holder.append(temp) if temp is not None else None
                        temp = None
                self.advance()
            elif self.current_char in END or self.current_char in TAB or self.current_char in NEWLINE:
                self.advance()
            elif self.current_char in ACCEPTED_SYMBOLS and not tuple_mode:
                if temp is None:
                    temp = self.current_char
                elif temp is not None:
                    temp += self.current_char
                self.advance()
            else:
                return None, UnknownSyntaxError(self.current_char)
        tokens.append(temp) if temp is not None else None
        """Handle Errors"""
        if tokens is None:
            if string_mode:
                return None, MissingSyntaxError("'")
            elif tuple_mode:
                return None, MissingSyntaxError(")")

        return tokens, None
