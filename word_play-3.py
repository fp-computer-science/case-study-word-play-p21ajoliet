# Write a program that contains a function called `avoid` that takes a word 
# and a string of forbidden letters and returns `True` if the word does not 
# use any of the forbidden letters. The program should prompt the user to enter a string 
# of forbidden letters and use the function to print to the console the number of 
# words in `words.txt` that don't contain any of the forbidden letters.

def avoid(word, letters):
    for y in letters:
        if y not in word:
            return True

fletters = input("Type the forbidden letters: ")
fletters1 = []

for x in fletters:
    fletters1.append(x)

with open("words.txt") as file1:
    words = file1.readlines()

    for line in words:
        if avoid(line, fletters1):
            print(line)
