# A Story of Two Collections..
# List:
# A linear collection of values that stay in order
# Dictionary:
# A “bag” of values, each with its own label

# Dictionaries
# Dictionaries are Python’s most powerful data collection
# Dictionaries allow us to do fast database-like operations in Python
# Dictionaries have different names in different languages
# -  Associative Arrays - Perl / PHP
# -  Properties or Map or HashMap - Java
# -  Property Bag - C# / .Net

# Lists index their entries based on the position in the list
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
purse['candy'] = purse['candy'] + 2

# Dictionaries are like bags - no order
# So we index the things we put in the dictionary with a “lookup tag”

# Comparing Lists and Dictionaries
# Dictionaries are like lists except that they use keys instead of numbers to look up values
lst = list()
lst.append(183)
lst.append(21)
print(lst[0])
# list
# Key   Value
# [0]   21
# [1]   183

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
# Dictionary
# Key           Value
# ['course']    182
# ['age']       21

# Dictionary Literals (Constants)
# Dictionary literals use curly braces and have a list of key : value pairs
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(jjj)
# You can make an empty dictionary using empty curly braces
ooo = { }
print(ooo)