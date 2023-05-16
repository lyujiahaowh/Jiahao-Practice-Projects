# Opening a file
# Before we can read the contents of the file
# we must tell Python which file we are going to work with and what we will be doing with the file
# This is done with the open() function
# open() returns a "file handle" - a variable used to perform operatiosn on the file
# Similar to "File->Open" in a Word Processor

# Using open()
# handle = open(filename, mode)
# returns a handle use to manipulate the file
# filename is a string
# mode is optional and should be 'r' if we are planning to read the file and 'w' if we are going to write to the file
# File handle is not a data, it's just a way to get at the data
# You action <=> Handle <=> file (handle is like our connection)

# The newline character
# We use a special character called the "newline" to indicate when a line ends
# We represent it as \n in strings
# Newline is still one character - not two
# \n ~= enter button in windows os
# \n is one kind of whitespace