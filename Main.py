# the start of the A-SQL interpreter
import Interpreter
from FileHandling import FileHandling
import sys

if len(sys.argv) > 1:
    fh = FileHandling(sys.argv[1])
    code = fh.Extract()
    result, error = Interpreter.Run(code, "<stdin>")
    if error:
        print(error.as_string())
    else:
        if result is not None:
            print(result)
        else:
            print("")
else:
    while True:
        code = input("myDB > ")
        result, error = Interpreter.Run(code, "<stdin>")
        if error:
            print(error.as_string())
        else:
            if result is not None:
                print(result)
            else:
                print("")
