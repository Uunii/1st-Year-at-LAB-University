def askName():
    name = input("Insert name: ")
    return name

def greetUser(name):
    print(f"Hello {name}!")
    return
def main():
    print("Program starting.")
    name = askName()
    greetUser(name)
    print("Program ending.")
    return None
main()