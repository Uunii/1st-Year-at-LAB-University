import requests
import pandas as pd
import matplotlib.pyplot as plt

url1 = "https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=20"
response1 = requests.get(url1)
data = response1.json()
tempdata = [entry["field2"] for entry in data['feeds']]
movedata = [entry["field1"] for entry in data['feeds']]
df = pd.DataFrame({
    'Temperature': tempdata,
    'Movement' : movedata
})
print(df)

plt.figure(figsize=(10, 5))
plt.subplot(2,1,1)
plt.plot(df['Temperature'], label='Temperature')
plt.title('Temperature Over Time')

plt.subplot(2,1,2)
plt.plot(df['Movement'], label='Movement',color="orange")
plt.title('Movement Over Time')

plt.show()