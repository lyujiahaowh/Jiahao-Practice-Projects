word = input("Enter your word: ")
letter = input("Enter your letter: ")

def count(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count