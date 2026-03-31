def frameWord(word):
    length = int(len(word))
    char = "*"
    print(char * (length + 4))
    print(f"* {word} *")
    print(char * (length + 4))

def main():
    print("Program starting.")
    word = input("Insert word: ")
    print("")
    frameWord(word)
    print("\nProgram ending.")
    return None
main()