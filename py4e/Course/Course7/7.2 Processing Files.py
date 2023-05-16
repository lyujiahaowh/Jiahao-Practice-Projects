# File Handle as a Sequence
# A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
# We can use the for statement to iterate through a sequence
# Remember - a sequence is an ordered set

# Counting Lines in a File
# Open a file read-only
# Use a for loop to read each line
# Count the lines and print out the number of lines
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# Reading the *Whole* File
# We can read the whole file (newlines and all) into a single string
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))

# Searching Through a File
# We can put an if statement in our for loop to only print lines that meet some criteria
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:') :
        print(line)
# From: stephen.marquard@uct.ac.za

# From: louis@media.berkeley.edu

# From: zqian@umich.edu

# From: rjlowe@iupui.edu
# ...

# Each line from the file has a newline at the end
# The print statement adds a newline to each line

# Searching Through a File (fixed)
# We can strip the whitespace from the right-hand side of the string using rstrip() from the string library
# The newline is considered “white space” and is stripped
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)
# fixed:
# From: stephen.marquard@uct.ac.za
# From: louis@media.berkeley.edu
# From: zqian@umich.edu
# From: rjlowe@iupui.edu
# ....

# Skipping with continue
# We can conveniently skip a line by using the continue statement
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    print(line)

# Using in to Select Lines
# We can look for a string anywhere in a line as our selection criteria
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line : 
        continue
    print(line)

# Prompt for File Name
fname = input('Enter the file name:  ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)

# Bad File Names
# exp:
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt

# Enter the file name: na na boo boo
# File cannot be opened: na na boo boo
fname = input('Enter the file name:  ')
try:
      fhand = open(fname)
except:
      print('File cannot be opened:', fname)
      quit()

count = 0
for line in fhand:
      if line.startswith('Subject:') :
          count = count + 1
print('There were', count, 'subject lines in', fname)

