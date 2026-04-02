import csv
def main():
    print("Program starting.")
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturnday",
        "Sunday"
    ]
    dailyuse = {day: 0.0 for day in weekdays}
    dailycost = {day: 0.0 for day in weekdays}
    filename = input("Insert filename: ")
    print(f'Reading file "{filename}".')
    print("Analysing timestamps.")

    with open(filename, 'r') as file:
        next(file)
        for line in file:
            line = line.strip()
            if not line:
                continue
            weekday, hour, consumption, price = line.strip().split(';')
            cons = float(consumption)
            price = float(price)
            cost = round(cons * price, 2)
            dailyuse[weekday] += cons
            dailycost[weekday] += cost
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for day in weekdays:
        print(f" - {day} usage{dailyuse[day]: .2f} kWh, ", end='')
        print(f"cost{dailycost[day]: .2f} €")
    print("### Electricity consumption summary ###")
    print("Program ending.")
    return None
main()