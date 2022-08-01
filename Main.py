# the start of the A-SQL interpreter
import Interpreter

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
