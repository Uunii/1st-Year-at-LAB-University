print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")

print("\nOptions:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = input("Your choice: ")

while(choice == "1"):
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    choice1 = input("Your choice: ")
    if(choice1 == "1"):
        m = float(input("Insert meters: "))
        km = m / 1000
        print(m, "m is", km, "km")
    elif(choice1 == "2"):
        km = float(input("Insert kilometers: "))
        m = km * 1000
        print(km, "km is", m, "m")
    elif(choice1 == "0"):
        print("Exiting...")
    else:
        print("Unknown option.")
    break
while(choice == "2"):
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    choice2 = input("Your choice: ")
    if(choice2 == "1"):
        gramm = float(input("Insert grams: "))
        pound = round(gramm / 453.6, 4)
        print(gramm, "g is", pound, "lb")
    elif(choice2 == "2"):
        pound = float(input("Insert pounds: "))
        gramm = round(pound * 453.6, 4)
        print(pound, "lb is", gramm, "g")
    elif(choice2 == "0"):
        print("Exiting...")
    else:
        print("Unknown option.")
    break
while(choice == "0"):
    print("\nExiting...")
    break
print("\nProgram ending.")




