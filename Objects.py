class Token:
    def __init__(self, type_, value=None, secondary_value=None):
        self.type_ = type_
        self.value = value
        self.secondary_value = secondary_value

    def __repr__(self):
        if self.secondary_value: return f'[\'{self.type_}\':"{self.value}":{self.secondary_value}]'
        if self.value: return f'[\'{self.type_}\':"{self.value}"'
        return f'{self.type_}'


class Condition:
    def __init__(self, type_, left_node=None, right_node=None):
        self.type_ = type_
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self):
        return f'({self.type_}:{self.left_node}, {self.right_node})'


class DataType:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value


    def __repr__(self):
        return f'{self.type_}:{self.value}'

    def lower(self):
        self.value.lower()
