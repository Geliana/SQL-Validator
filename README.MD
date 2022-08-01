# Awino SQL Interpreter

Built for the project _`Awino DB`_
Converts Single SQl Statements into _Awino code_
_`Awino DB`_ is targeted to be able to handle multiple databases using simple syntax
_`A-SQL`_ is targeted to be `ISO/IEC 9075:2016` Compliant (For more info, check `GRAMAR.MD` File)

SQL statements follow a Two-step Process to achieve _Awino code_
1. Parser
    > Where the statements are tokenized into single tokens per every coma, space or parenthesis
2. Lexer
    > The tokens are converted into Singular Token-Types with primary and secondary value

## Awino Code
Awino code follows the Following Format:
> _[Token Type]:[Primary Value]:[Secondary Value]_
It is produced by the Token Class 

### Token Type
Token Types are Recognized SQL statements including some custom AwinoDB recognized syntax

### Values
This refers to all variable types including all non-sql syntax, numbers, text inside "'`, and all tuples
Values are categorized into two
1. Primary Values
2. Secondary Values

### Primary Values
Primary values are all varchar, strings and numbers

### Secondary Values
Everything inside a tuple `Parentheseis`

