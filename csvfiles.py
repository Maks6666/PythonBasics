import csv


# data - table name 
data = [
    ["Name", "Age", "Height"], #add as many columns as you wish
    ["Anna", 25, 171], #add as many strings as you want 
    ["Peter", 30, 180],
    ["Maria", 22, 168]
]

# to open it in code environment:
with open('example.csv', mode='w', newline='') as file: #example.csv - file name 
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        writer.writerow(row)
