lst = list()
fh = open('romeo.txt')
for line in fh:
    words = line.split()
    for word in words:
        if word in lst:
            continue
        lst.append(word)
print(sorted(lst))