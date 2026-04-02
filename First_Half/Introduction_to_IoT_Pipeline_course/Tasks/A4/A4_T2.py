print("Program starting.")

svalue = int(input("\nInsert starting value: "))
evalue = int(input("Insert stopping value: "))

print("\nStarting for-loop:")

for x in range(svalue, evalue+1):
    if x == evalue:
        print(x, end='')
    else:
        print(x, end=' ')

print("\n\nProgram ending.")