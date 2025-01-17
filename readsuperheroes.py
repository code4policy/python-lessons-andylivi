import json
import csv
import os

# Ensure the output directory exists
os.makedirs('output', exist_ok=True)

# Read the JSON file
with open('superheroes.json', 'r') as jsonfile:
    superheroes = json.load(jsonfile)

# Define the CSV file path
csv_file_path = 'output/members.csv'

# Write the members' data to the CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['name', 'age', 'secretIdentity', 'power', 'squadName', 'homeTown', 'formed', 'secretBase', 'active']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Loop over the members and write each row to the CSV file
    for member in superheroes['members']:
        for power in member['powers']:
            writer.writerow({
                'name': member['name'],
                'age': member['age'],
                'secretIdentity': member['secretIdentity'],
                'power': power,  # Write each power in a separate row
                'squadName': superheroes['squadName'],
                'homeTown': superheroes['homeTown'],
                'formed': superheroes['formed'],
                'secretBase': superheroes['secretBase'],
                'active': superheroes['active']
            })

# Print the superheroes list to verify
print(superheroes)