'''Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
    The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
    The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
    After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
fname = input("Enter file:")
if len(fname) < 1: 
    fname = "mbox-short.txt"
handle = open(fname)

di = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for w in words:
        # if the key is not there the count is zero
        di[w] = di.get(w,0) + 1

largest = -1
theword = None
for k,v in di.items():
    if v > largest:
        larget = v
        theword = k # capture/remember the word that was largest

print(theword, largest)

'''
name = input("Enter file:")
dict = {}
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith("From "):
		line = line.rstrip()
		words = line.split()
		email = words[1]
		if email not in dict:
			dict[email] =1
		else:
			dict[email] +=1
mostName = None
mostCount = None
for mail in dict:
   if mostCount == None or mostCount < dict[email]:
      mostName = email
      mostCount = dict[email]
print(mostName, mostCount)
'''