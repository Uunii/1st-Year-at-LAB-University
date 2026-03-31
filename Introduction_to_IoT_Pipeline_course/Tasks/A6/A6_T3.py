def main():
    print("Program starting.")
    print("This program can copy a file.")
    source = input("Insert source filename: ")
    destination = input("Insert destination filename: ")
    with open(source, 'r') as file:
        scontent = file.read()
    print("Reading file ", source, " content.", sep="'")
    print("File content ready in memory.")
    print("Writing content into file ", destination, ".", sep="'")
    with open(destination, "w") as file:
        file.write(scontent)
    print("Copying operation complete.")
    print("Program ending.")
    return None
main()