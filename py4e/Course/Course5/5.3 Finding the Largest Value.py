# Loop Idioms - What We Do in Loops
# Note: Even though these examples are simple, the patterns apply to all kinds of loops

# Making "smart" loops
# The trick is “knowing” something about the whole loop when you are stuck writing code that only sees one entry at a time
# 1st : Set some variables to initial values
# 2nd : for thing in data:
# Look for something or do something to each entry separately, updating a variable
# Look at the variables

# Looping through a set
print('Before')
for thing in [9, 41, 12, 3, 74, 15] :
    print(thing)
print('After')

# exp: Finding the largest value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)
# We make a variable that contains the largest value we have seen so far. 
# If the current number we are looking at is larger, it is the new largest value we have seen so far.
