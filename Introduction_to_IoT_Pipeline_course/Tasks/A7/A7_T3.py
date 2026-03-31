import csv
weekdays = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturnday", "Sunday"]
daycounts = {day: 0 for day in weekdays}
def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f'Reading file "{filename}".')
    print("Analysing timestamps.")
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            line = line.strip()
            if not line:
                continue
            for day in weekdays:
                if line.startswith(day):
                    daycounts[day] += 1
                    break
        print("Displaying results.")
        print("### Timestamp analysis ###")
        for day in weekdays:
            print(f" - {day} {daycounts[day]} stamps")
        print("### Timestamp analysis ###")
        print("Program ending.")
        return None
main()