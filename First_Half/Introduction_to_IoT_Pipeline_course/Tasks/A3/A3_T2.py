print("Program starting.")
print("String comparisons")
w1 = input("Insert first word: ")
c1 = input("Insert a character: ")
if c1 in w1 :
    print("Word ", w1, " contains character ", c1,sep='"', end='"')
else:
    print("Word ", w1, " doesn't contain character ", c1,sep='"', end='"')

w2 = input("\nInsert second word: ")
if w1 < w2:
    print(f"The first word ",w1," is before the second word " ,w2," alphabetically.", sep='"',)
elif w1 > w2:
    print(f"The second word ",w2," is before the first word ",w1," alphabetically.",sep='"', )
elif w1 == w2:
    print(f"Both inserted words are the same alphabetically, ", w1, sep='"', end='"\n')


print("Program ending.")
