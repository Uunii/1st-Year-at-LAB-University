print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name=input("Before the menu, please insert your name: ")

bname = name[::-1]
fchar = name[0:1]
chars = len(name)

print("\nOptions:")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")
choice = input("Your choice: ")
if(choice == "1"):
    print("Welcome", name,end='!\n')
elif(choice == "2"):
    print("Your name backwards is ", bname, sep='"', end='"\n')
elif(choice == "3"):
    print("The first character in name ", name, " is ", fchar, sep='"', end='"\n')
elif(choice == "4"):
    print("There are", chars, end='')
    print(" characters in the name ", name, sep='"', end='"\n')
elif(choice == "0"):
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")



