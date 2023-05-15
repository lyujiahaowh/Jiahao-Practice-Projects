# Loops(repeated steps) have iteration variables that change each time through a loop.
# Often these iteration variables go through a sequence of numbers.
# If you don't set up the interation variables it will cause an infinite loop.
# Zero-trip loop is like the opposite of infinite loop

# Breaking out of a loop
# The break statement ends the current loop and jumps to the statement immediately following the loop
# It is like a loop test taht can happen anywhere in the body of loop

while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')

# Finishing an interation with continue
# the continue statement ends the current iteraction and jumps to the top of the loop and starts the next interaction

while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

# Break skips the loop and continue skips the top of the loop
# The continue doesn't get you out of the loop, the continue goes to the next iteration basically. Abandons the current iteration and goes to the next iteration. 
