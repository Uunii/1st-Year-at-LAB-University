def main():
    print("Program starting.")
    print("\nCollecting plain text rows for ciphering.")
    alltext = ""
    while True:
        text = input("Insert row(empty stops): ")
        if text == "":
            break
        alltext += text + "\n"
    convertedtext = ""
    for char in alltext:
        if 'a' <= char <= 'z':
            newchar = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            newchar = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            newchar = char
        convertedtext += newchar

    print("\n#### Ciphered text ####")
    print(convertedtext)
    print("#### Ciphered text ####")
    while True:
        filename = input("Insert filename to save: ")
        if filename == "":
            print("File name not defined.")
            print("Aborting save operation.")
            print("Program ending.")
            break
        else:
            with open(filename, 'w')as file:
                file.write(convertedtext)
                print("Ciphered text saved!")
                print("Program ending.")
                break
    return None
main()