import re

# Read the file
file_path = 'regex_sum_1755532.txt'  # Update with the actual file path
with open(file_path) as file:
    content = file.read()

# Extract the numbers using regular expressions
numbers = re.findall('[0-9]+', content)

# Convert the extracted strings to integers and compute the sum
total_sum = sum(int(num) for num in numbers)

# Print the sum
print("Sum:", total_sum)
