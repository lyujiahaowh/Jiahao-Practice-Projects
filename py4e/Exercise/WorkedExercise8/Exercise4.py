fh = open('romeo.txt')
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word in lst:
            continue
        lst.append(word)
print(lst.sort())
