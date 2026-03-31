class data():
    Ints = []
    nonInts = []
def main():
    print("Program starting.")
    integers = input("Insert comma separated integers: ")
    integer = integers.split(',')
    Ints = data.Ints
    nonInts = data.nonInts
    summ = 0
    for value in integer:
        value = value.strip()
        try:
            num = int(value)
            summ += num
            Ints.append(num)
        except ValueError:
            nonInts.append(value)
    sum = len(Ints)
    remainder = summ % 2
    if remainder == 1:
        itis = "odd"
    else:
        itis = "even"
    if Ints == []:
        for letter in nonInts:
            print((f"Invalid value '{letter}' detected."))
        print("No values to analyse.")
    elif nonInts != []:
        for letter in nonInts:
            print((f"Invalid value '{letter}' detected."))
        print("There are", sum, "integers in the list.")
        print("Sum of the integers is", summ, "and it's", itis)
    else:
        print("There are", sum, "integers in the list.")
        print("Sum of the integers is", summ, "and it's", itis)
    print("Program ending.")
    return None
main()