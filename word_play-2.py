# Write a program that contains a function called `no_e` that returns `True` 
# if the given word does not contain the letter `"e"`. Use this function to read `words.txt` 
# and write to a file named `words_without_e.txt` the words from `words.txt` that do not contain
# the letter `"e"`. The program should also print to the console the percentage of words 
# in `words.txt` that do not contain the letter `"e"`.

def no_e(word):
    if 'e' not in word:
        return True

with open('words.txt') as file1, open('words_without_e.txt', 'w') as file2:
    input1 = file1.readlines()
    
    for line in input1:
        if no_e(line):
            file2.write(line)


with open('words.txt') as file3, open('words_without_e.txt') as file4:
    total1 = len(file3.readlines())
    total2 = len(file4.readlines())

    percent_e = total2 / total1 * 100

    print("{0} percent of the words in 'words.txt' don't contain the letter 'e'".format(percent_e))
