fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From:') :
        continue
    if line.startswith('From'):
        line = line.rstrip()
        words = line.split()
        print(words[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")

fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    words = line.split()
    # guardian in a compound statement
    if len(words) < 3 or words[0] != 'From' :
        print(words[2])
print("There were", count, "lines in the file with From as the first word")