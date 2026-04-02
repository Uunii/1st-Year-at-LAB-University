def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ")
    print("#### START ", filename, " ####", sep='"')
    with open(filename, 'r') as file:
        content = file.read()
    print(content)
    print("#### END ", filename, " ####", sep='"')
    print("Program ending.")
    return None
main()