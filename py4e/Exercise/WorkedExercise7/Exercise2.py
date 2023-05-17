'''Write a program that prompts for a file name, then opens that file and reads through the file, 
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
Use the file name mbox-short.txt as the file name
'''
count = 0
total = 0

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    quit()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        colpos = line.find(':')
        sum_num = float(line[colpos + 1:])
        total = total + sum_num

average = total / count
print('Average spam confidence:', average)