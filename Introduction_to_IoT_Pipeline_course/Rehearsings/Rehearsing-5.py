# # import requests
# # url = "https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=20"
# # response = requests.get(url)
# # print(f"Status code: {response.status_code}")
# # data = response.json()
# # for entry in data["feeds"]:
# #     movement_value = entry["field1"]
# #     temp_value = entry["field2"]
# #     time_value = entry["created_at"]
# #     print(f"Movement value: {movement_value}")
# #     print(f"Temperature value: {temp_value}")
# #     print(f"At: {time_value}")


import requests

base_url = "https://rata.digitraffic.fi/api/v1/live-trains/station"
departure_station = input("Departure station: ").lower()
if departure_station == "helsinki":
    departure_station = "HKI"
elif departure_station == "lahti":
    departure_station = "LH"
arrival_station = input("Arrival station: ").lower()
if arrival_station == "helsinki":
    arrival_station = "HKI"
elif arrival_station == "lahti":
    arrival_station = "LH"
url = f"{base_url}/{departure_station}/{arrival_station}"
response = requests.get(url)

if response.status_code == 200:
    trains = response.json()
    for train in trains:
        train_number = train["trainNumber"]
        length = len(str(train_number))
        scheduled_departure = None
        actual_departure = None
        scheduled_arrival = None
        actual_arrival = None
        for row in train["timeTableRows"]:
            if row["stationShortCode"] == departure_station and row["type"] == "DEPARTURE":
                scheduled_departure = row["scheduledTime"]
            if row["stationShortCode"] == arrival_station and row["type"] == "ARRIVAL":
                scheduled_arrival = row["scheduledTime"]
            if length == 1:
                print(f"Train Number: {train_number}, ",end='')
                if scheduled_departure == None:
                    print(f"   Departure: {scheduled_departure},",end='')
                    print(f"                     Arrival: {scheduled_arrival}")
                else:
                    print(f"   Departure: {scheduled_departure}, ",end='')
                    print(f"Arrival: {scheduled_arrival}")
                break
            elif length == 2:
                print(f"Train Number: {train_number}, ",end='')
                if scheduled_departure == None:
                    print(f"  Departure: {scheduled_departure},",end='')
                    print(f"                     Arrival: {scheduled_arrival}")
                else:
                    print(f"  Departure: {scheduled_departure}, ",end='')
                    print(f"Arrival: {scheduled_arrival}")
                break
            elif length == 3:
                
                print(f"Train Number: {train_number}, ",end='')
                if scheduled_departure == None:
                    print(f" Departure: {scheduled_departure},",end='')
                    print(f"                     Arrival: {scheduled_arrival}")
                else: 
                    print(f" Departure: {scheduled_departure}, ",end='')
                    print(f"Arrival: {scheduled_arrival}")
                break
            elif length == 4:
                print(f"Train Number: {train_number}, ", end='')
                if scheduled_departure == None:
                    print(f"Departure: {scheduled_departure},",end='')
                    print(f"                     Arrival: {scheduled_arrival}")
                else: 
                    print(f"Departure: {scheduled_departure}, ",end='')
                    print(f"Arrival: {scheduled_arrival}")
                break
else:
            print(f"Failed to retrieve train data. Status code: {response.status_code}")

# # Data to be written to the text file
# data = """Hello, World!
# This is a simple text file.
# It contains multiple lines of text."""
# # Writing to the text file
# with open("data.txt", "w") as file:
#     file.write(data)
# print("Data written to data.txt")

# # Reading from the text file
# with open("data.txt", "r") as file:
#     content = file.read()
# print("Content of data.txt:")
# print(content)

# import csv
# # Data to be written to the CSV file
# data = [
#     ["Name", "Age", "Town"],
#     ["Mari", 40, "Tampere"],
#     ["Johanna", 49, "Espoo"],
#     ["Katja", 47, "Turenki"]
# ]
# # Writing to the CSV file
# with open("data.csv", "w", newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data)
# print("Data written to data.csv")

# import csv
# # Reading from the CSV file
# with open("data.csv", "r") as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)

# import json
# # Initial data to be written to the JSON file
# data = {
#     "users": [
#         {"login": "user1", "password": "pass1"},
#         {"login": "user2", "password": "pass2"}
#     ]
# }
# # Writing to the JSON file
# with open("data.json", "w") as file:
#     json.dump(data, file, indent=4)
# print("Initial data written to data.json")
# new_user={"login": "user3", "password": "pass3"}
# with open("data.json", "r") as file:data= json.load(file)
# data["users"].append(new_user)
# with open("data.json", "w") as file:
#     json.dump(data, file, indent=4)
# print("Updated data written to data.json")


# import json
# # Reading from the JSON file
# with open("data.json", "r") as file:
#     data = json.load(file)
# print("Content of data.json:")
# print(data)