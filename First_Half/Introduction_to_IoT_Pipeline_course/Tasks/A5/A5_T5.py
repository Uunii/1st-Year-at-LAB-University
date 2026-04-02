def showOptions(first_run):
    if first_run:
        print("Options:")
    else:
        print("\nOptions:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")

def main():
    word = ""
    print("Program starting.")
    first_run = True
    while True:
        showOptions(first_run)
        first_run = False
        choice = input("Your choice: ")
        if choice == "1":
            word = input("Insert word: ")
        elif choice == "2":
            print(f'Current word - "{word}"')
        elif choice == "3":
            print(f'Word reversed - "{word[::-1]}"')
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option! try again.")
    print("\nProgram ending.")
    return None
main()
