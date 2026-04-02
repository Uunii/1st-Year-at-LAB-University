print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name=input("Before the menu, please insert your name: ")

print("\nOptions:")
print("1 - Print welcome message")
print("0 - Exit")
choose = input("Your choice: ")
if(choose == "1"):
    print("Welcome ", name, sep='', end='!\n', )
elif(choose == "0"):
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")