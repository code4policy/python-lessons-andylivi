import csv

# List of vegetables with their names and colors
vegetables = [
    {"name": "eggplant", "color": "purple"},
    {"name": "tomato", "color": "red"},
    {"name": "corn", "color": "yellow"},
    {"name": "okra", "color": "green"},
    {"name": "arugula", "color": "green"},
    {"name": "broccoli", "color": "green"},
]

# Open the CSV file for writing
with open('vegetables.csv', 'w', newline='') as csvfile:
    # Define the column headers
    fieldnames = ['name', 'color']
    # Create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()
    # Write each vegetable's data as a row in the CSV file
    for vegetable in vegetables:
        writer.writerow(vegetable)