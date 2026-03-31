def main():
    print("Program starting.")
    fname = input("Insert first name: ")
    lname = input("Insert last name: ")
    filename = input("Insert filename: ")
    print("Program ending.")

    with open(filename, 'w') as file:
        file.write(str(fname + '\n'))
        file.write(str(lname + '\n'))
    return None
main()