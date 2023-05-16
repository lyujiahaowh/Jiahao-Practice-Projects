# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    shout = line.rstrip().upper()
    print(shout)