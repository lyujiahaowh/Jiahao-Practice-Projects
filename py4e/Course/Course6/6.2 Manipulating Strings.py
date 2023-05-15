# String concatenation
# When the + operator is applied to strings, it means "concatenation"

# Using in as a logical operator
# The in keyword can also be used to check to see if one string is "in" another string
# The in expression is a logical expression that returns True or False and can be used in an if statement

# String comparison
word = input("Enter your word:")
if word == 'banana':
    print('All right, banana.')

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

# String library
# Python has a number of string functions which are in the string library
# These functions are already built into every string - we invoke them by appending the function to the string variable
# These functions do not modify the original string, instead they return a new string that has been altered 
# lowercase function usage:
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
# uppercase function usage:
print('Hi There'.upper())
# type() and dir():
stuff = 'Hello world'
type(stuff)
dir(stuff)
# more:
# str.capitalize(); str.replace(old, new[ , content]); str.center(width[, fillchar]); str.lower(); str.endswith(suffix[, start[, end]])
# str.rstrip([chars]); str.find(sub[, start[, end]]); str.strip([chars]); str.lstrip([chars]); str.upper()

# Searching a string
# We use the find() function to search for a substring within another string
# find() finds the first occurrence of the substring
# If the substring is not found, find() returns -1
# Remember that string position starts at zero
fruit = 'banana'
pos = fruit.find('na')
print(pos)
# not found, it result '-1'
aa = fruit.find('z')
print(aa)

# Making Everything UPPER CASE
# You can make a copy of a string in lower case or upper case
# Often when we are searching for a string using find() we first convert the string to lower case so we can search a string regradless of case
# everything upper
greet = 'Hello Bob'
nnn = greet.upper()
print(nnn)
# everything lower
www = greet.lower()
print(www)

# Search and replace
# The replace() function is like a "search and replace" operation in a word processor
# It replaces all occurrences of the search string with the replacement string
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)

nstr = greet.replace('o', 'X')
print(nstr)

# Stripping Whitespace
# Sometimes we want to take a string and remove whitespace at the beginning and/or end
# Istrip() and rstrip() remove whitespace at the left or right
# strip() removes both beginning and ending whitespace
greet = '    Hello Bob   '
greet.lstrip()
greet.rstrip()
greet.strip()

# Prefixes
line = 'Please have a nice day'
line.startswith('Please')
line.startswith('p')

# Parsing and Extracting
# From stephen.marquard@ut.ac.za Sat Jan  5 09:14:16 2008
data = 'From stephen.marquard@ut.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

# Strings and character sets
# every string inside Python 3 is capable of representing all character sets

