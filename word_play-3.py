#Author: ALJ (AMDG) 2/24/21

def avoid(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

fletters = input("Type the forbidden letters: ")

with open("words.txt") as file1:
    words = file1.readlines()

    for line in words:
        if avoid(line, fletters):
            print(line)