class Token:
    values = None
    length = -1

    def __init__(self, type_):
        self.type_ = type_
        self.values = []

    def addValue(self, value):
        self.values.append(value)
        self.length += 1

    def lastValue(self):
        return self.values[self.length]

    def changeLastValue(self, new_value):
        self.values[self.length] = new_value

    def popLastValue(self):
        self.values.pop(self.length)
        self.length -= 1

    def __repr__(self):
        return f'{self.type_}:{self.values}'


class Condition:
    def __init__(self, type_, left_node=None, right_node=None):
        self.type_ = type_
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self):
        return f'({self.type_}:"{self.left_node}", "{self.right_node}")'


class MetaCommands:
    def __init__(self, command):
        self.command = command

    def __repr__(self):
        return f'META:{self.command}'


class TableColumnNavigation:
    def __init__(self, table, column):
        self.table = table
        self.column = column

    def __repr__(self):
        return f'[Table->{self.table}:Column->{self.column}]'


class SQLDataType:
    def __init__(self, type_, constraint, length=None):
        self.type_ = type_
        self.length = length
        self.constraint = constraint

    def __repr__(self):
        return f'{self.type_}:{self.length}'


class KeyValueEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'[Column->{self.key}:Value->{self.value}'
