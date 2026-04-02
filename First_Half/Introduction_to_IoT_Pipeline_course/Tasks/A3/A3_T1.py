print("Program starting.")
print("Insert two integers.")
int1 = int(input("Insert first integer: "))
int2 = int(input("Insert second integer: "))
print("Comparing inserted integers.")
if(int1 < int2):
    print("Second integer is greater.")
elif(int1 > int2):
    print("First integer is greater.")
else:
    print("Integers are the same")

print("\nAdding integers together")
sum = int1 + int2
print(int1, "+", int2, "=", sum)
print("\nChecking the parity of the sum...")
remainder = sum % 2
if(remainder == 1):
    print("Sum is odd.")
else:
    print("Sum is even.")
print("Program ending.")

