class Error:
    def __init__(self, error_name, details, line=0, column=0):
        self.error_name = error_name
        self.details = details
        self.line = line
        self.column = column

    def as_string(self):
        result = f'{self.error_name}: "{self.details}" at line {self.line}->{self.column}'
        return result


class InvalidSyntaxError(Error):
    def __init__(self, details):
        super(InvalidSyntaxError, self).__init__("Invalid Syntax Error", details)


class UnknownDatabaseError(Error):
    def __init__(self, details, line, column):
        super(UnknownDatabaseError, self).__init__("Database does not exist", details, line, column)


class MissingValueError(Error):
    def __init__(self, details):
        super(MissingValueError, self).__init__("Missing Value", details)


class InvalidValueError(Error):
    def __init__(self, details, line, column):
        super(InvalidValueError, self).__init__("Invalid Value", details, line, column)


class TableExistsError(Error):
    def __init__(self, details, line, column):
        super(TableExistsError, self).__init__("A similar Table exists", details, line, column)


class UnknownTableError(Error):
    def __init__(self, details, line, column):
        super(UnknownTableError, self).__init__("Table does not exist", details, line, column)


class DatabaseExistsError(Error):
    def __init__(self, details, line, column):
        super(DatabaseExistsError, self).__init__("A similar Database exists", details, line, column)


class MissingSyntaxError(Error):
    def __init__(self, details):
        super(MissingSyntaxError, self).__init__("Missing Syntax", details)


class UnknownSyntaxError(Error):
    def __init__(self, details, line=0, column=0):
        super(UnknownSyntaxError, self).__init__("Unknown Syntax", details, line, column)


class UnknownColumnError(Error):
    def __init__(self, details, line, column):
        super(UnknownColumnError, self).__init__("Unknown Column", details, line, column)


class ColumnExistsError(Error):
    def __init__(self, details, line, column):
        super(ColumnExistsError, self).__init__("A similar Column exists", details, line, column)


class UnknownLengthType(Error):
    def __init__(self, details, line, column):
        super(UnknownLengthType, self).__init__("This does no match a length type", details, line, column)


class UnknownConstraint(Error):
    def __init__(self, details, line, column):
        super(UnknownConstraint, self).__init__("Find an A-SQL constraint for", details, line, column)


class UnknownFileError(Error):
    def __init__(self, details, line, column):
        super(UnknownFileError, self).__init__("Couldn't Find the file with Path", details, line, column)


class IllegalListError(Error):
    def __init__(self, details):
        super(IllegalListError, self).__init__("Illegal List Placement", details)


class IllegalConditionError(Error):
    def __init__(self, details):
        super(IllegalConditionError, self).__init__("Illegal Condition Placement", details)


class IllegalSyntaxError(Error):
    def __init__(self, details):
        super(IllegalSyntaxError, self).__init__("Illegal Syntax Error", details)