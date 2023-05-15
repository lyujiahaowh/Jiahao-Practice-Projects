largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        numval = int(num)
    except:
        print('Invalid input')
        continue

    if largest is None:
        largest = numval
    elif numval > largest:
        largest = numval

    if smallest is None:
        smallest = numval
    elif numval < smallest:
        smallest = numval 

print("Maximum is", largest)
print("Minimum is",  smallest)