
from add_to_GINI import add_one
import requests
import matplotlib.pyplot as plt

endpoint = 'https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22'

response = requests.get(endpoint)
response.raise_for_status()
response = response.json()

country_requested = input("Escriba el nombre del pais del cual desea obtener el indice GINI: ")


country_selected = []

for gini in response[1]:
    if gini["country"]["value"].lower() == country_requested.lower() and gini["value"] != None:
        country_selected.insert(0, {"country": gini["country"]["value"],
                                 "value": float(gini["value"]),
                                 "date": gini["date"]})
        
 
# Sample data
x = [item["date"] for item in country_selected]  
y = [item["value"] for item in country_selected]

x1 = [item["date"] for item in country_selected]  
y1 = [add_one(item["value"]) for item in country_selected]
 
# Create a line chart
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-')
plt.plot(x1, y1, marker='o', linestyle=':')
 
# Add annotations
for i, (xi, yi) in enumerate(zip(x, y)):
    plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')
 
# Add title and labels
plt.title('GINI INDEX')
plt.xlabel('Year')
plt.ylabel('GINI value')
 
# Display grid
plt.grid(True)
 
# Show the plot
plt.show()