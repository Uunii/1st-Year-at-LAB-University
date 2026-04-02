print("Program starting.")

start = int(input("\nInsert starting point: "))
stop = int(input("Insert stopping point: "))
mid = int(input("Insert inspection point: "))

if(start >= stop):
    print("\nStarting point value must be less than the stopping point value.", end='')
if(mid > stop or mid < start ):
    print("\nInspection value must be within the range of start and stop.")
else:
    print("\nFirst loop - inspection with break:")
    for x in range(start, stop):
        if x == mid:
            break
        if x !=start:
            print(" ", end='')
        print(x, end='')
    print()    
    print("Second loop - inspection with continue:")
    first_printed = False
    for x in range(start, stop):
        if x == mid:
            continue
        if first_printed:
            print("", end=' ')
        else:
            first_printed = True
        print(x, end='')
    print()
    
print("\nProgram ending.")