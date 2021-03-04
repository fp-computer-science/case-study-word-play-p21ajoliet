#Author: ALJ (AMDG) 3/4/21

def is_abecedarian(word1):
    word2 = list(word1)
    word3 = list(word1)
    word3.sort()

    if word3 == word2:
        return True
    return True

with open("words.txt") as file1:
    words = file1.readlines()

for line in words:
    if is_abecedarian(line):
        print(line)
