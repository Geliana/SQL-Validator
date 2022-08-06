class Read:
    result = None

    def __init__(self, filename):
        self.fn = filename

    def Extract(self):
        code = open(self.fn, 'r').read()
        self.result = code
        return self.result


class Write:
    def __init__(self, result, filename="output.asql"):
        self.result = result
        self.fn = filename

    def dump(self):
        with open(self.fn, 'w') as f:
            f.write(str(self.result))
