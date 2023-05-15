# String data type
# A string is a sequence of characters
# A string literal uses quotes 'Hello' or "Hello"
# For strings, + means “concatenate”
# When a string contains numbers, it is still a string
# We can convert numbers in a string into a number using int()

# Reading an converting
# We prefer to read data in using strings and then parse and convert the data as we need
# This gives us more control over error situations and/or bad user input
# Input numbers must be converted from strings

# Looking Inside Strings
# We can get at any single character in a string using an index specified in square brackets
# The index value must be an integer and starts at zero
# The index value can be an expression that is computed

# A Character Too Far
# You will get a python error if you attempt to index beyond the end of a string
# So be careful when constructing index values and slices

# Strubgs have length
# The built-in function len gives us the length of a string

# len Function
# A function is some stored code that we use. A function takes some input and produces an output.

# Looping Through Strings
# Using a while statement, an iteration variable, and the len function, we can construct a loop to look at each of the letters in a string individually
# exp 01:
fruit = 'banana'
index = 0
while index < len(fruit): 
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# A definite loop using a for statement is much more elegant
fruit = 'banana'
for letter in fruit: 
    print(letter)

# The iteration variable is completely taken care of by the for loop
fruit = 'banana'
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(letter)
    index = index + 1

# Looping and Counting
# This is a simple loop that loops through each letter in a string and counts the number of times the loop encounters the 'a' character
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' : 
       count = count + 1
print(count)

# Looking Deeper into in
# The iteration variable “iterates” through the sequence (ordered set)
# The block (body) of code is executed once for each value in the sequence
# The iteration variable moves through all of the values in the sequence
for letter in 'banana' :
      print(letter)

# Slicing Strings
# We can also look at any continuous section of a string using a colon operator
# The second number is one beyond the end of the slice - "up to but not including"
# If the second number is beyond the end of the string, it stops at the end
s = 'Monty Python'
print(s[6:20])
# If we leave off the first number or the last number of the slice, it is assumed to be the beginning or end of the string respectively
s = 'Monty Python'
print(s[:2])