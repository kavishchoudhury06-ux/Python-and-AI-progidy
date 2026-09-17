import csv
# Data to be written
header = ['Name', 'Age', 'City']
data = [
    ['Alice', 28, 'New York'],
    ['Bob', 34, 'Los Angeles'],
    ['Charlie', 22, 'Chicago']
]
# Create and write to the CSV file
with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
# Write the header row
    writer.writerow(header)
# Write multiple data rows

    writer.writerows(data)