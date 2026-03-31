print("Program starting.")

svalue = int(input("\nInsert starting value: "))
evalue = int(input("Insert stopping value: "))

print("\nStarting while-loop:")

while svalue <= evalue:
    if svalue == evalue:
        print(svalue)
    else:
        print(svalue, end=" ")
    svalue += 1
print("\nProgram ending.")