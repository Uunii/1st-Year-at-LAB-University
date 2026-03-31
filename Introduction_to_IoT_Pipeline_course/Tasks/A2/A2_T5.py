print("Program starting.")
word = input("\nInsert a closed compound word:")
rword = word[::-1]
char = len(word)
lchar = word[-1]
print(" The word you inserted is '", word, "' and in reverse it is '", rword, "'.", sep='', end='\n')
print("The inserted word length is", char)
print("Last character is '", lchar, "'", sep='')
print("\nTake substring from the inserted word by inserting...")
start = int(input("1) Starting point:"))
end = int(input(" 2) Ending point:"))
step = int(input(" 3) Step size:"))
sstring = word[start:end:step] 
print(" \nThe word '", word, "' sliced to the defined substring is '", sstring,"'.", sep='', end='\n')
print("Program ending.")
