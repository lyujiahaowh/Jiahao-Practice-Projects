'''Regular Expressions
In computing, a regular expression, also referred to as “regex” or “regexp”, 
provides a concise and flexible means for matching strings of text, 
such as particular characters, words, or patterns of characters. 
A regular expression is written in a formal language that can be interpreted by a regular expression processor.

Really clever “wild card” expressions for matching and parsing strings
'''
'''Understanding Regular Expressions
Very powerful and quite cryptic
Fun once you understand them
Regular expressions are a language unto themselves
A language of “marker characters” - programming with characters
It is kind of an “old school” language - compact
'''
'''Regular Expression Quick Guide
^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end

'''
'''The Regular Expression Module
Before you can use regular expressions in your program, you must import the library using “import re”
You can use re.search() to see if a string matches a regular expression, similar to using the find() method for strings
You can use re.findall() to extract portions of a string that match your regular expression, similar to a combination of find() and slicing:  var[5:10] 
'''
'''Using re.search() Like find()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

modified:
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line) :
        print(line)
'''
'''Using re.search() Like startswith()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) :
        print(line)
        
We fine-tune what is matched by adding special characters to the string
'''
'''Wild-Card Characters
The dot character matches any character
If you add the asterisk character, the character is “any number of times”

^X.*: ^ means match the start of the line . means match any character * means many times
'''
'''Fine-Tuning Your Match
Depending on how “clean” your data is and the purpose of your application, you may want to narrow your match down a bit

^X-\S+: ^ means match the start of the line \ means match any non-whitespace character + means one or more times
'''
