
def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = input("Insert filename to read: ")
    with open(filename, 'r') as file:
        names = [name.strip() for name in file.readlines() if name.strip()]
    namesnum = len(names)
    shortestname = min(names, key=len)
    longestname = max(names, key=len)
    shortestchar = len(shortestname)
    longestchar = len(longestname)
    allchar = sum(len(name) for name in names)
    avgchar = round(allchar / namesnum, 2)
    average = "{:.2f}".format(avgchar)
    print("Reading names from ", filename, ".", sep='"')
    print("Analysing names...")
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print("Name count -", namesnum)
    print("Shortest name -", shortestchar, "chars")
    print("Longest name -", longestchar, "chars")
    print("Average name -", average, "chars")
    print("#### REPORT END ####")
    print("Program ending.")
    return None
main()