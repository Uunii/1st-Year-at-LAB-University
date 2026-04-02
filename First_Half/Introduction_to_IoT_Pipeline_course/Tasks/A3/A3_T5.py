print("Program starting.")
print("\nOptions:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")



choice = input("Your choice: ")
if(choice == "1"):
    Ce = float(input("Insert the amount of Celsius: "))
    Fa = (Ce * 9/5) + 32
    print(Ce,"°C equals to", Fa, "°F")
elif(choice == "2"):
    F = float(input("Insert the amount of Fahrenheit: "))
    C = round((F-32) * 5/9 ,1)
    print(F,"°F equals to", C, "°C")

print("\nProgram ending.")


   
