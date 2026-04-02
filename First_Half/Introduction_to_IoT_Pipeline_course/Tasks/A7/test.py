def main():
    print("Program starting.\nCollect positive integers.")
    numbers = []
    while (num := int(input("Insert positive integer (negative stops): "))) >= 0: numbers.append(num)
    print(f"Displaying {len(numbers)} integers:\n" + 
          "\n".join(f"- Index {i} => Ordinal {i+1} => Integer {n}" for i, n in enumerate(numbers)) if numbers else "No integers to display.")
    print("Program ending.")
main()