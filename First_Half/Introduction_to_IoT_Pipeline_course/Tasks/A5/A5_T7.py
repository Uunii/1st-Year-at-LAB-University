DELIMITER = ','
print("Program starting.")

def collectWords():
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    return words

def analyseWords(word_string):
    words = word_string
    numword = len(words)
    numchar = sum(len(word) for word in words)
    Avg = numchar / numword

    print(f"- {numword} Words")
    print(f"- {numchar} Characters")
    print("- {:.2f} Average word length".format(Avg))
    print("Program ending.")
def main():
    collected_words = collectWords()
    analyseWords(collected_words)
    return None

main()
