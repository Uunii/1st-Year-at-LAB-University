print("Program starting.\n")
words = []   
while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    words.append(word)
nwords = len(words)
nchars = sum(len(word) for word in words)
print("\nYou inserted:")
print("-",nwords, "words")
print("-", nchars, "characters")
print("\nProgram ending.")