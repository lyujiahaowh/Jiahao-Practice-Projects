'''
Tuples Are Like Lists
Tuples are another kind of sequence that functions much like a list - they have elements which are indexed starting at 0

but... Tuples are “immutable”
Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string
'''
'''
Things not to do With Tuples
x = (3, 2, 1)
x.sort()
x.append(5)
x.reverse()
'''
'''
Tuples are more efficient
Since Python does not have to build tuple structures to be modifiable
 they are simpler and more efficient in terms of memory use and performance than lists
So in our program when we are making "temporary variabels" we prefer tuples over lists
'''
'''
Tuples and assignment
We can also put a tuple on the left-hand side of an assignment statement
We can even omit the parentheses
'''
'''
Tuples and dictionaries
The items() method in dictionaries returns a list of (key, value) tuples
'''
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items() :
    print(k, v)
tups = d.items()
print(tups)

'''
Tuples are comparable
The comparison operators work with tuples and other sequences
If the first item is equal, Python goes on to the next element, and so on, until it finds elements that differ
(0, 1, 2) < (5, 1, 2)
>>> Ture
(0, 1, 2000000) < (0, 3, 4)
>>> Ture
('Jones', 'Sally') < ('Jones', 'Sam')
>>> Ture
('Jones', 'Sally') > ('Adams', 'Sam')
>>> Ture
'''
'''
Sorting lists of tuples
We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
First we sort the dictionary by the key using the items() method and sorted() function
d = {'a' : 10, 'b' : 1, 'c' : 22}
d.items()
>>> dict_items([('a', 10), ('b', 1), ('c', 22)])
sorted(d.items())
>>> [('a', 10), ('b', 1), ('c', 22)]
'''
'''
Using sorted()
We can do this even more directly using the built-in function sorted that takes a sequence as a parameter and returns a sorted sequence
d = {'a' : 10, 'b' : 1, 'c' : 22}
t = sorted(d.items())
t
>>> [('a', 10), ('b', 1), ('c', 22)]
for k, v in sorted(d.items())
    print(k, v)
>>> a 10
>>> b 1
>>> c 22
'''
'''
Sort by values instead of key
If we could construct a list of tuples of the form (value, key) we could sort by value
We do this with a for loop that creates a list of tuples
c = {'a' : 10, 'b' : 1, 'c' : 22}
tmp = list()
for k, v in c.items() :
    tmp.append((v, k))
print(tmp)
>>> [(10, 'a'), (22, 'c'), (1,'b')]
tmp = sorted(tmp, reverse=True)
print(tmp)
>>> [(22, 'c'), (10, 'a'), (1,'b')]
'''
'''
The top 10 most common words
original
'''
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items() :
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key, val)

'''
Even shorter version
merge functions in 99 - 104 code to
'''
c = {'a' : 10, 'b' : 1, 'c' : 22}
print(sorted([(v,k) for k,v in c.items()]))
'''
List comprehension creates a dynamic list
In this case, we make a list of reversed tuples and the sort it.
'''

x, y = 3, 4