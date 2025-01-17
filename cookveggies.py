import csv
import json  # Import the json module

vegetables = []

# Read the CSV file
with open('vegetables.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        vegetables.append(row)

# Write the vegetables list to a JSON file
with open('output/vegetables.json', 'w') as jsonfile:
    json.dump(vegetables, jsonfile, indent=2)

# Print the vegetables list to verify
print(vegetables)