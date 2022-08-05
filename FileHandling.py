class FileHandling:
    result = None

    def __init__(self, filename):
        self.fn = filename

    def Extract(self):
        code = open(self.fn, 'r').read()
        self.result = code
        return self.result

# TODO:Comments Parsing in files
# TODO:Resulting code dumped into a file
