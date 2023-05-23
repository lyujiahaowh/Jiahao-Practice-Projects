'''Matching and Extracting Data
re.search() returns a True/False depending on whether the string matches  the regular expression
If we actually want the matching strings to be extracted, we use re.findall()

[0-9]+ : means one or more digits

When we use re.findall(), it returns a list of zero or more sub-strings that match the regular expression
'''
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
# >>> ['2', '19', '42']
y = re.findall('[AEIOU]+',x)
print(y)
# >>> []

'''Warning: Greedy Matching
The repeat characters (* and +) push outward in both directions (greedy) to match the largest possible string
^F.+: ^ means first character in the match is an F .+ means one or more characters : means last character in the match is a :

>>> import re
>>> x = 'From: Using the : character'
>>> y = re.findall('^F.+:', x)
>>> print(y)
['From: Using the :']
'''
'''Non-Greedy Matching
Not all regular expression repeat codes are greedy!  If you add a ? character, the + and * chill out a bit...

^F.+?: ^ means first character in the match is an F .+? means  One or more characters but not greedy : means last character in the match is a :
'''
'''Fine-Tuning String Extraction
You can refine the match for re.findall() and separately determine which portion of the match is to be extracted by using parentheses

\S+@\S+ means at least one non-whitespace character

Parentheses are not part of the match - but they tell where to start and stop what string to extract
^From (\S+@\S+)
'''
'''
example lines:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

>>> data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> atpos = data.find('@')
>>> print(atpos)
21
>>> sppos = data.find(' ',atpos)
>>> print(sppos)
31
>>> host = data[atpos+1 : sppos]
>>> print(host)
uct.ac.za

Extracting a host name - using find and string slicing
'''
'''The Double Split Pattern
Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
'''
'''The Regex Version
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

import re 
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin)
print(y)

['uct.ac.za']

'@([^ ]*)' : @ means look through the string until you find an at sign [^ ] means match non-blank character * means match many of them
'''
'''Even Cooler regex version
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

import re 
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',lin)
print(y)
>>> ['uct.ac.za']

'^From .*@([^ ]*)' (^)Starting at the beginning of the line, (From)look for the string 'From ' 
(.*)Skip a bunch of characters, (@)looking for an at sign, (() means Start extracting, ([^ ]) means Match non-blank character ()) means Match many of them
'''
'''Spam Confidence
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 :  continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
'''
'''Escape Character
If you want a special regular expression character to just behave normally (most of the time) you prefix it with '\'

>>> import re
>>> x = 'We just received $10.00 for cookies.'
>>> y = re.findall('\$[0-9.]+',x)
>>> print(y)
['$10.00']

\$[0-9.]+ (\$) means A real dollar sign ([0-9.]) means A digit or period (+) means At least one or more
'''
'''Summary
Regular expressions are a cryptic but powerful language for matching strings and extracting elements from those strings
Regular expressions have special characters that indicate intent
'''
'''Python Regular Expression Quick Guide
https://docs.python.org/3/howto/regex.html
'''