## 2.1 Experssions
#### Fixed values such as numbers,letters,strings are called "cosntants" because they do not change
#### Numeric constants are as you expect
#### String constants are use single quotes ('') or double quotes ("")

### Reserved words - you cannot use reserved words as variable names / identifiers
#### false, class, finally, is, return, None, continue, for, lambda, try, True, def, from, nonlocal, while, and, del, global, not, with, as, elif, if, or, yield, assert, else, import, pass, break, except, in, raise

#### in python , = means <-
### Variables - A variable is a nemed place in the memory where a programmer can store data and later retrieve the data using the variable "name"
#### Programmers choose names for variables that are meaningful to the program
#### You can change the content of a variable at any time
#### Python variable name rules - 1. must start with a letter or underscore 2. must consist of letters, numbers, and underscores 3. case sensitive

### Sentences - A sentence in a program is a unit of code that the Python interpreter can execute
#### Sentences have structure and syntax
#### A sentence in Python is composed of expressions and statements
#### Sentences must end with a new line character
#### Sentences or Lines - x = 2 is an assignment statement / x = x + 2 is an assignment/assignment with experssion statement / print(x) is an expression/print statement
#### organge is variable, white is operator, blue is constant, yellow is function
#### Mnenomics - A memory aid, usually involving a pattern of letters, ideas, or associations, that assists in remembering something. It is only good for humans, not computers.
#### Phython does not understand plural nouns, so it is better to use singular nouns for variables
#### However , it is helpful to use plural nouns for lists when something has more than one value
#### Python does not understand past tense, so it is better to use present tense for variables

### Assignment Statements
#### We assign a value to a variable using an assignment statement (=)
#### An assignment statement consists of an experession on the right-hand side and a variable to store result

## 2.2 Expressions
### Numeric Expressions
#### Bescause of lack of mathematical symbols on computer keyboards, Python uses operators(coumputer-speak) to represent mathematical concepts
#### Asterisk (*) is used for multiplication
#### Exponentiation is done with double asterisk (**), it looks didfferent than in math
#### Remainder is done with the percent sign (%), instead of giving a quotient, it gives the remainder

### Order of Evaluation
#### When we string operators together, Python must know which on is to do first
#### This is called "operator precedence"

### Operator Precedence Rules
#### Highest precedence rule to lowest precedence rule
##### Parentheses are aways evaluated first/respected
##### Exponentiation (raise to a power)
##### Multiplication, Division, and Remainder
##### Addition and Subtraction
##### Left to right
##### ex. 1 + 2 ** 3 / 4 * 5 -> 1 + 8 / 4 * 5 -> 1 + 2 * 5 -> 1 + 10 -> 11

### Operator Precedence
#### Remember the rules top to bottom
#### When writing code - use parentheses to make your code easier to read
#### When wirting code - keep mathematical expressions simple enough that they are easy to read and understand
#### Break long series of mathematical operations up to make them more clear

### What does "Type" mean?
#### In Python variables, literals, and constants have a "type"
#### Python knows the difference between an integer number and a string
#### For example "+" means "addition" if something is a number and "concatenate" if something is a string