class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: "{self.details}"'
        return result


class InvalidSyntaxError(Error):
    def __init__(self, details):
        super(InvalidSyntaxError, self).__init__("Invalid Syntax Error", details)


class UnknownDatabaseError(Error):
    def __init__(self, details):
        super(UnknownDatabaseError, self).__init__("Database does not exist", details)


class MissingValueError(Error):
    def __init__(self, details):
        super(MissingValueError, self).__init__("Missing Value", details)


class InvalidValueError(Error):
    def __init__(self, details):
        super(InvalidValueError, self).__init__("Invalid Value", details)


class TableExistsError(Error):
    def __init__(self, details):
        super(TableExistsError, self).__init__("A similar Table exists", details)


class UnknownTableError(Error):
    def __init__(self, details):
        super(UnknownTableError, self).__init__("Table does not exist", details)


class DatabaseExistsError(Error):
    def __init__(self, details):
        super(DatabaseExistsError, self).__init__("A similar Database exists", details)


class MissingSyntaxError(Error):
    def __init__(self, details):
        super(MissingSyntaxError, self).__init__("Missing Syntax", details)


class UnknownSyntaxError(Error):
    def __init__(self, details):
        super(UnknownSyntaxError, self).__init__("Unknown Syntax", details)


class UnknownColumnError(Error):
    def __init__(self, details):
        super(UnknownColumnError, self).__init__("Unknown Column", details)


class ColumnExistsError(Error):
    def __init__(self, details):
        super(ColumnExistsError, self).__init__("A similar Column exists", details)


class UnknownLengthType(Error):
    def __init__(self, details):
        super(UnknownLengthType, self).__init__("This does no match a length type", details)


class UnknownConstraint(Error):
    def __init__(self, details):
        super(UnknownConstraint, self).__init__("Find an A-SQL constraint for", details)


class UnknownFileError(Error):
    def __init__(self, details):
        super(UnknownFileError, self).__init__("Couldn't Find the file with Path", details)


class IllegalListError(Error):
    def __int__(self, details):
        super(IllegalListError, self).__init__("Illegal List Placement", details)


class IllegalConditionError(Error):
    def __int__(self, details):
        super(IllegalConditionError, self).__init__("Illegal Condition Placement", details)


class IllegalSyntaxError(Error):
    def __int__(self, details):
        super(IllegalSyntaxError, self).__init__("Illegal Syntax Error", details)
