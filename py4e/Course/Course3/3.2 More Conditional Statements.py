# you need to visualize blocks

# multi-way
x = 0
if x < 2 :
    print('small')
elif x < 5 :
    print('medium')
elif x < 8 :
    print('large')
else :
    print('xlarge')
print('All done')

# no else is acceptable, so if you dont want an else that would be ok
y = 2
if y < 2 :
    print('small')
elif y < 10 :
    print('medium')
print('All done')

# try/expect block
astr = 'Hello bob'
try :
    istr = int (astr)
except :
    istr = -1
print('First', istr)

astr = '123'
try :
    istr = int(astr)
except :
    istr = -1
print('Second', istr)

bstr = 'Bob'
try : 
    print('Hello')
    istr = int(bstr)
    print('There')
except :
    istr = -1
print('Done', istr)

# sample try/expect
rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1
# this is a de-indent of the try/expect block
if ival > 0 :
    print('Nice work')
else:
    print('Not a number')