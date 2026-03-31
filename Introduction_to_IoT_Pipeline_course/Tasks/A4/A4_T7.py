print("Program starting.")
print("\nCheck multiplicative persistence.")
num = int(input("Insert an integer: "))
steps = 0
while num >= 10:
    digits = [int(digit) for digit in str(num)]
    print(" * ".join(str(digit) for digit in digits), end=" = ")
    product = 1
    for digit in digits:
        product *= digit
    print(product)  
    num = product  
    steps += 1  
print("No more steps.")
print("\nThis program took", steps, "step(s)")
print("\nProgram ending.")

