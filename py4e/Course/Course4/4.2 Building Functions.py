# def function will not run itself automatically

# arugments
# an argument is a value we pass into the function as its input when we call the function
# we use arguments so we can direct the function to do different kinds of work when we call it at different times
# we put the arguments in the parentheses after the name of the function

# parameters
# a parameter is a variable which we use int he function definition
# it is a "handle" that allows the code in the function to access the arguments for a particular function invocation

# return values
# often a function will take its arguments, do some computation,
# and return a value to be used as the value of the function call in the calling expression
# the return keyword is used for this
# A "fruitful" function is one that produces a reslut(or return value)
# The return statement ends the function exectuion and "send back" the result of function

# Multiple Parameters / Arguments
# We can define more than on parameter int the function definition
# We simply add more arguments when we call the function
# We match the number and order of argument and parameters

def addtwo(a, b) :
    added = a + b
    return added

x = addtwo(3, 5)
print(x)

# Functions do not return values called "non-fruitful functions"
# If the return values than called "fruitful functions"