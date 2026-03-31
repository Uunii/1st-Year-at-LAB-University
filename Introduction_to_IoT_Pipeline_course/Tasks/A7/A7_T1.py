def main():
    print("Program starting.\nCollect positive integers.")
    list = []
    while True:
        num = int(input("Insert positive integer(negative stops): "))
        if num < 0:
            print("Stopped collecting positive integers."); break
        list.append(num)
    if list:
        print(f"Displaying {len(list)} integers:")
        for i in range(len(list)):
            print(f"- Index {i} => Ordinal {i+1} => Integer {list[i]}\n")
    else:
        print("No integers to display.")
    print("Program ending.")
    list.clear()
    return None
main()