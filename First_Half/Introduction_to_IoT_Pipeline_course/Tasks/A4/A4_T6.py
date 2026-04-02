print("Program starting.")
num = int(input("Insert a positive integer: "))    
if num < 1:
    print("Please enter a positive integer.")
else:
    sequence = []
    steps = 0    
    while num != 1:
        sequence.append(num)
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1  
        steps += 1      
    sequence.append(1)       
    print(" -> ".join(map(str, sequence)))
    print("Sequence had", steps, "total steps.")
print("\nProgram ending.")