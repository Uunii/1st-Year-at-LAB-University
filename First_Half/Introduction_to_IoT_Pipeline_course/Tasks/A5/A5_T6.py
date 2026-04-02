def showOptions(first_run):
    if first_run:
        print("Options:")
    else:
        print("\nOptions:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def askChoice():
    try:
        choice = int(input("Your choice: "))
        return choice
    except ValueError:
        return 4

def main():
    count = 0 
    print("Program starting.")
    first_run = True
    while True:
        showOptions(first_run)
        first_run = False
        choice = askChoice()
        if choice == 1:
            print("Current count -", count)
        elif choice == 2:
            count += 1
            print("Count increased!")    
        elif choice == 3:
            count = 0
            print("Cleared count!")
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
    print("\nProgram ending.")
    return None
main()