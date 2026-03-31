print("Calculate fuel consumption.")
Distance = int(input("Enter travel distance(kilometers):"))
Fuelusage= int(input("Enter fuel usage(liters):"))
Consumption = (Fuelusage / Distance) * 100
print(f"Fuel consumption is {(Consumption)} l per 100 km")