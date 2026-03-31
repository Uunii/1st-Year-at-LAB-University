def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print("#### Number analysis - START ####")
    total = 0
    count = 0
    nums = []
    with open(filename, 'r') as file:
        for line in file:
            num = int(line.strip())
            total += num
            count += 1
            nums.append(num)
            maxnum = max(nums)
    avg = total / count
    print("File ", filename, " results:", sep='"')
    print("Count;Sum;Greatest;Average")
    average = "{:.2f}".format(avg)
    print(count, total, maxnum, average, sep=';')
    print("\n#### Number analysis - END ####")
    print("Program ending.")
    return None
main()
