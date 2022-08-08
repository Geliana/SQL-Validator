from var.Errors import IllegalListError, IllegalConditionError, MissingSyntaxError, UnknownSyntaxError, \
    InvalidSyntaxError, IllegalSyntaxError
from var.Objects import Token, KeyValueEntry, MetaCommands, TableColumnNavigation, Condition

TOKENS = {'use': "TT_USE", 'using': "TT_USING", 'create': "TT_CREATE", 'drop': "TT_DROP", 'inform': "TT_INFORM",
          'alter': "TT_ALTER", 'rename': "TT_REN", 'add': "TT_ADD", 'to': "TT_TO", 'database': "TT_DB",
          'select': "TT_SELECT", 'table': "TT_TBL", 'column': "TT_CLN", 'insert': "TT_INSERT", "into": "TT_INTO",
          'values': "TT_VAL", 'from': "TT_FRM", 'help': "TT_HELP", 'set': "TT_SET", 'where': "TT_WHERE",
          'update': "TT_UPDT", 'delete': "TT_DLT", 'inner': "TT_INNER", 'join': "TT_JOIN"}

CONDITIONS = {'=': "CT_SET", '==': "CT_EQUAL", '>': "CT_GREATER", '<': "CT_LOWER", '<=': "CT_LSEQ", '>=': "CT_GRTEQ",
              '<>': "CT_NTEQ"}
"""
== indicates to check on equality
= sets one to the other -- deprecated in version 0.0.4 as it doesnt necessarily qualify to be a condition

e.g -- left-node == right-node -if left-node is equal to right-node-,
 while left-node = right-node -set left-node to right-node-
"""

METACOMMANDS = {'exit': "EXIT"}


class Parser:
    """
    The Parser               --- Revised under version 0.0.3

    Majority Token Conversion takes place Here,
    Converting Recognized A-SQL syntax into pre-determines blocks

    Tokens are received in List form from the Lexer and are categorised into block types

    variables
        -- Tuples -- come in form of python Tuples enclosed in parentheses
        -- strings -- Can either come enclosed inside string symbols or just as they are
    SQL Tokens, Identifiers and Symbols
        -- SQL Tokens
        -- Conditions
        -- Constraints
        -- Datatypes
        -- Join Table Column Navigational Strings using '.' Notation
        -- Key value set store indicated by the "=" sign
    Special Non-SQL Syntax
        -- Meta Commands __ which come with a '.' at the beginning

    Variables are considered to be values of their corresponding Tokens and are treated as so

    SQL Tokens or simply referred to as Tokens and may come fitted with a value or values and
    the length of the values, they have been Pre-Configured and are here to just be identified
    and Fitted with their value(s)

    Conditions are Defined above with a simple Brief Explanation for each of them
    They are different in architecture since they give Comparsions between two values
    Hence they come bundled with a Left-node and Right-node

    Datatypes are PreDefined (above) Known SQL Datatypes and are constructed to come with a length
    and a constraint

    Joint Table Column Strings are Navigational tools on a table level divided by a full stop
    Table.Column

    Meta Commands are small one line simple statements

    Key Value Entries are two strings divided by a '=' sign, they are allocated left_node and  right_node. The left_node
    is set to the Right node. Perfect for Column value integreations

    For the Lexer to work, priorities are given since the difference between each category is purely virtual and depends
    on its location in the entry code.
    1st Priority = Tuples -- This is as a result of preventing an error when we try to lower our code for comparisons
    2nd Priority = SQL Tokens -- Known and common SQL tokens
    3rd Priority  = Conditions
    4th Priority = Strings
    5th Priority = KeyValueEntries
    6th Priority = Table Navigational Strings / Meta Command


    Stephen Telian
    Last Update: 6th August 2022

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
            if type(self.current_token) is tuple:
                """A Tuple has been identified"""
                if previous_token_priority_type is None:
                    """Indicating that only a tuple was passed"""
                    return None, IllegalListError(self.current_token)
                elif previous_token_priority_type == "first":
                    """Indicating that a list was passed previously meaning it is a continuous stream of list"""
                    temp.addValue(self.current_token)
                elif previous_token_priority_type == "second":
                    """Previous token type was a Token and hence this is its preceding value"""
                    temp.addValue(self.current_token)
                elif previous_token_priority_type == "third":
                    """Previous Token type was a condition"""
                    temp.addValue(self.current_token)
                elif previous_token_priority_type == "fourth":
                    """Previous token type was string"""
                    temp.addValue(self.current_token)
                elif previous_token_priority_type == "fifth":
                    "Previous was a key value entry"
                    temp.addValue(self.current_token)
                elif previous_token_priority_type == "sixth":
                    """Previous was a navigational string"""
                    temp.addValue(self.current_token)
                previous_token_priority_type = "first"
                self.advance()
            elif self.current_token.lower() in TOKENS:
                self.current_token = self.current_token.lower()
                """Hence it is a tokens"""
                if previous_token_priority_type is None:
                    """The first token to be encountered"""
                    temp = Token(TOKENS[self.current_token])
                elif previous_token_priority_type == "first":
                    """The previous token was identified to be a tuple and hence is to be finalized being
                     put into the blocks"""
                    blocks.append(temp)
                    temp = Token(TOKENS[self.current_token])
                elif previous_token_priority_type == "second":
                    """The previous token has been identified to be a token hence let it be finalized and taken
                     into blocks """
                    blocks.append(temp)
                    temp = Token(TOKENS[self.current_token])
                elif previous_token_priority_type == "third":
                    """Previous token type was a condition"""
                    blocks.append(temp)
                    temp = Token(TOKENS[self.current_token])
                elif previous_token_priority_type == "fourth":
                    """Previous token type was a string"""
                    blocks.append(temp)
                    temp = Token(TOKENS[self.current_token])
                elif previous_token_priority_type == "fifth":
                    """Previous token was a key value Entry"""
                    blocks.append(temp)
                    temp = Token(TOKENS[self.current_token])
                elif previous_token_priority_type == "sixth":
                    """Previous token type was a affliated to the dot notation """
                    blocks.append(temp)
                    temp = Token(TOKENS[self.current_token])
                previous_token_priority_type = "second"
                self.advance()
            elif self.current_token in CONDITIONS:
                if previous_token_priority_type is None:
                    """A condition was passed only """
                    return None, IllegalConditionError(self.current_token)
                elif previous_token_priority_type == "first":
                    """A tuple was identified before this """
                    return None, MissingSyntaxError(f'Expected value before: {self.current_token}')
                elif previous_token_priority_type == "second":
                    last_value = temp.lastValue()
                    temp.popLastValue()
                    self.advance()
                    temp.addValue(Condition(CONDITIONS[self.current_token], last_value, self.current_token))
                elif previous_token_priority_type == "third":
                    """Condition Irregularity"""
                    return None, IllegalSyntaxError(self.current_token)
                elif previous_token_priority_type == "fourth":
                    """Previous Token was a string"""
                    con = self.current_token
                    last_value = temp.lastValue()
                    temp.popLastValue()
                    self.advance()
                    temp.addValue(Condition(CONDITIONS[con], last_value, self.current_token))
                elif previous_token_priority_type == "fifth":
                    return None, IllegalConditionError(self.current_token)
                elif previous_token_priority_type == "sixth":
                    return None, IllegalConditionError(self.current_token)

                previous_token_priority_type = "third"
                self.advance()
            elif type(self.current_token) is str and self.current_token != "." and self.current_token != "=":
                """A string that is neither a token nor a condition has been identified"""
                if previous_token_priority_type is None:
                    return None, UnknownSyntaxError(self.current_token)
                elif previous_token_priority_type == "first":
                    """Previous token was a Tuple hence this will be another value to its collection """
                    temp.addValue(self.current_token)
                elif previous_token_priority_type == "second":
                    """Previous token was a Token Type"""
                    temp.addValue(self.current_token)
                elif previous_token_priority_type == "third":
                    temp.addValue(self.current_token)
                elif previous_token_priority_type == "fourth":
                    temp.addValue(self.current_token)
                elif previous_token_priority_type == "fifth":
                    return None, IllegalSyntaxError(self.current_token)
                elif previous_token_priority_type == "sixth":
                    temp.addValue(self.current_token)
                previous_token_priority_type = "fourth"
                self.advance()
            elif self.current_token == "=":
                if previous_token_priority_type is None:
                    return None, UnknownSyntaxError(self.current_token)
                elif previous_token_priority_type == "first":
                    return None, InvalidSyntaxError(self.current_token)
                elif previous_token_priority_type == "second":
                    """Handle special Tokens set to values"""
                    temp = KeyValueEntry(temp, self.current_token)
                elif previous_token_priority_type == "third":
                    return None, UnknownSyntaxError(self.current_token)
                elif previous_token_priority_type == "fourth":
                    last_value = temp.lastValue()
                    temp.popLastValue()
                    blocks.append(temp)
                    temp = KeyValueEntry(last_value, self.current_token)
                elif previous_token_priority_type == "fifth" or previous_token_priority_type == "sixth":
                    return None, IllegalSyntaxError(self.current_token)
                previous_token_priority_type = "fifth"
                self.advance()
            elif self.current_token == ".":
                if previous_token_priority_type is None:
                    self.advance()
                    temp = MetaCommands(METACOMMANDS[self.current_token])
                elif previous_token_priority_type == "first":
                    return None, InvalidSyntaxError(self.current_token)
                elif previous_token_priority_type == "second":
                    return None, InvalidSyntaxError(self.current_token)
                elif previous_token_priority_type == "third":
                    return None, InvalidSyntaxError(self.current_token)
                elif previous_token_priority_type == "fourth":
                    last_value = temp.lastValue()
                    temp.popLastValue()
                    self.advance()
                    temp.addValue(TableColumnNavigation(last_value, self.current_token))
                elif previous_token_priority_type == "fifth":
                    return None, InvalidSyntaxError(self.current_token)
                elif previous_token_priority_type == "sixth":
                    blocks.append(temp)
                    temp = MetaCommands(METACOMMANDS[self.current_token])
                previous_token_priority_type = "sixth"
                self.advance()
        blocks.append(temp) if temp is not None else None

        return blocks, None
