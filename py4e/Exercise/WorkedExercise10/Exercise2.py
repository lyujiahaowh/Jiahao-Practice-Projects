'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
'''1st attempt
'''
file_name = "mbox-short.txt"
hour_counts = {}

with open(file_name, 'r') as file:
    for line in file:
        if line.startswith("From "):
            words = line.split()
            time = words[5]
            hour = time.split(':')[0]
            hour_counts[hour] = hour_counts.get(hour, 0) + 1

sorted_hours = sorted(hour_counts.items())

for hour, count in sorted_hours:
    print(hour, count)

'''2nd attempt
'''
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Create a dictionary to store the count of messages by hour
counts = dict()

# Iterate through each line in the file
for line in handle:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hour = time.split(':')[0]
        counts[hour] = counts.get(hour, 0) + 1

# Sort the dictionary by hour
sorted_counts = sorted(counts.items())

# Print the counts sorted by hour
for hour, count in sorted_counts:
    print(hour, count)

'''3rd attempt
'''
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Create a dictionary to store the count of messages by hour
counts = dict()

# Iterate through each line in the file
for line in handle:
    words = line.split()
    if len(words) < 6 or words[0] != 'From':
        continue
    time = words[5]
    hour = time.split(':')[0]
    counts[hour] = counts.get(hour, 0) + 1

# Sort the dictionary by hour
sorted_counts = sorted(counts.items())

# Print the counts sorted by hour
for hour, count in sorted_counts:
    print(hour, count)
    
'''4th attempt
'''
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

counts = dict()

with open(name) as handle:
    for line in handle:
        if line.startswith('From '):
            hour = line.split()[5].split(':')[0]
            counts[hour] = counts.get(hour, 0) + 1

sorted_counts = sorted(counts.items())

for hour, count in sorted_counts:
    print(hour, count)
