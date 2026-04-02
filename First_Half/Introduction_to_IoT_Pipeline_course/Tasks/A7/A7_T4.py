import csv
def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f'Reading file "{filename}".')
    print("Electricity usage:")
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
            print(f" - {weekday} {hour}:00, price{price: .2f}, ", end='')
            print(f"consumption{cons: .2f} kWh, total{cost: .2f} €")
    print("Program ending.")
    return None
main()