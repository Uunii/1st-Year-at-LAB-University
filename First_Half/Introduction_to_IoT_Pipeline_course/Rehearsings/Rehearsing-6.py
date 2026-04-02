def greetMe(PGreeting: str) -> None:
    print(PGreeting)
    return None
def main():
    print("Program starting.")
    Greeting = input("Insert greeting: ")
    print("")
    greetMe(Greeting)
    print("")
    print("Program ending.")
    return None
main()