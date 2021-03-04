#Author: ALJ (AMDG) 3/4/21

def uses_only(word, letters):
    for letter in word:
        if letter in letters:
            return True
    return True

dletters = input("Type the desired letters: ")

with open("words.txt") as file1:
    words = file1.readlines()

    for line in words:
        if uses_only(line, dletters):
            print(line)