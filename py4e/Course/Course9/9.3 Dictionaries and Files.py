'''Counting Pattern
    The general pattern to count the words in a line of text is to split the line into words
    then loop through the words and use a dictionary to track the count of each word independently.
'''
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

'''Definite Loops and Dictionaries
    Even though dictionaries are not stored in order, we can write a for loop that goes through all the entries in a dictionary 
    actually it goes through all of the keys in the dictionary and looks up the values
'''

'''Retrieving Lists of Keys and Values
    You can get a list of keys, values, or items (both) from a dictionary   
'''
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(list(jjj))
print(list(jjj.keys()))
print(list(jjj.values()))
print(list(jjj.items()))

'''Bonus: Two Iteration Variables!
    We loop through the key-value pairs in a dictionary using *two* iteration variables
    Each iteration, the first variable is the key and the second variable is the corresponding value for the key
'''
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for aaa,bbb in jjj.items() :
    print(aaa, bbb)

'''Using two nested loops
'''
name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
