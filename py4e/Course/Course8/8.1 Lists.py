# Programming
# Algorithm  - A set of rules or steps used to solve a problem
# Data Structure - A particular way of organizing data in a computer

# What is Not a “Collection”?
# Most of our variables have one value in them - when we put a new value in the variable, the old value is overwritten

# A List is a Kind of Collection
# A collection allows us to put many values in a single “variable”
# A collection is nice because we can carry all many values around in one convenient package.
# exp:
friends = [ 'Joseph', 'Glenn', 'Sally' ]
carryon = [ 'socks', 'shirt', 'perfume' ]

# List Constants
# List constants are surrounded by square brackets and the elements in the list are separated by commas
# A list element can be any Python object - even another list
# A list can be empty
# print([1, 24, 76])
# print(['red', 'yellow', 'blue'])
# print(['red', 24, 98.6])
# print([ 1, [5, 6], 7])
# print([])

# Looking Inside Lists
# Just like strings, we can get at any single element in a list using an index specified in square brackets

# Lists are Mutable
# Strings are “immutable” - we cannot change the contents of a string - we must make a new string to make any change
# False exp:
# fruit = 'Banana'
# fruit[0] = 'b'

# Lists are “mutable” - we can change an element of a list using the index operator
# True exp:
lotto = [2, 14, 26, 41, 63]
lotto[2] = 28

# How Long is a List?
# The len() function takes a list as a parameter and returns the number of elements in the list
greet = 'Hello Bob'
print(len(greet))
# Actually len() tells us the number of elements of any set or sequence (such as a string...)
x = [ 1, 2, 'joe', 99]
print(len(x))

# Using the range Function
# The range function returns a list of numbers that range from zero to one less than the parameter
print(range(4))

friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
# We can construct an index loop using for and an integer iterator
print(range(len(friends)))

# A Tale of Two Loops...
# exp:
friends = ['Joseph', 'Glenn', 'Sally']

for friend in friends :
    print('Happy New Year:',  friend)

for i in range(len(friends)) :
    friend = friends[i]
    print('Happy New Year:',  friend)
