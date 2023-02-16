## course 01 - steps.py

## Sequence of steps
x = 2
print(x)
x = x + 2
print(x)

# --------------------------

## Conditional steps
y = 5
if y < 10:
    print('Smaller')
if y > 20:
    print('Bigger')

print('Finish')

# --------------------------

## Repeated steps
n = 5
while n >= 0 :
    print(n)
    n = n - 1
print('Blastoff!')

# --------------------------

# yellow is sequential
# green is repeated
# organge is conditional*
# A short Python "Story" about how to count words in a file
# A word used to read data from a user
name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
# A sentence about updating one of many counts

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
# A paragraph about how to find the largest item in a list

print(bigword, bigcount)