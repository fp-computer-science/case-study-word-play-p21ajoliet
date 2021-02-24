#Write a program that reads `words.txt` and writes to a file named `greater_than_20.txt` 
#the words from `words.txt` that are longer than 20 characters (not counting newline characters).

with open('words.txt') as file1, open ('greater_than_20.txt', 'w') as file2:
    input1 = file1.readlines()
    
    for line in input1:
        if len(line.strip()) > 20:
            file2.write(line)