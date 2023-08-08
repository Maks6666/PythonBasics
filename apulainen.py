#Programm "Santa's assistance" gives to user information about avaliable or not Christmass presents using TKinter UI and importing CSV files  
import tkinter as tk #Importing TKiner
import csv #Importing CSV to read file 
#columns in csv file(?) 1st - group of items, 2nd - item_type, 3d - price, 4th - amount
class Item: #Creating class, which contains items information
    def __init__(self, group, item_type, price, amount):
        self.group = group
        self.item_type = item_type
        self.price = price
        self.amount = amount

items = [] #Creating a list for all items 

with open('lahjadata.csv', newline='') as csvfile: #Opening CSV file and grouping it 
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        group = row[0]
        item_type = row[1]
        price = float(row[2])
        amount = int(row[3])
        item = Item(group, item_type, price, amount)
        items.append(item)


#Creating a function for available items list
def print_items_with_positive_amount(): 
    global items
    print('------ Available items -------')
    text_area.delete("1.0", "end")
    text_area.insert('end', "------ Available items ------\n") 
    for item in items:
        if item.amount > 0:
            print(f'Group: {item.group}, Type: {item.item_type}, Amount:{item.amount}')
            text_area.insert('end', f"Group: {item.group}, Type: {item.item_type}, Amount:{item.amount}\n")
    print('------End of list-------')
    
    
#Creating a function forprice of available items list
def print_average_prices_by_group():
    global items
    print('------ Average Prices by Group -------')
    
    text_area.delete("1.0", "end")
    text_area.insert('end', "------ Average Prices by Group -------\n") 
    groups = {}
    for item in items:
        if item.amount > 0:
            if item.group not in groups:
                groups[item.group] = [item.price]
            else:
                groups[item.group].append(item.price)
    for group, prices in groups.items():
        avg_price = sum(prices) / len(prices)
        print(f'{group}: {avg_price:.2f} euros')
        text_area.insert('end', f"{group}: {avg_price:.2f} euros\n")

        
    print('------ End of list -------')

#Creating a function for not  available items list
def print_items_with_not_positive_amount():
    global items
    print('------ Not available items -------')
    text_area.delete("1.0", "end")

    text_area.insert('end', "------ Not available items -------\n")
    
    for item in items:
        if item.amount <= 0:
            print(f'Group: {item.group}, Type: {item.item_type}, Amount:{item.amount}')
            text_area.insert('end', f"Group: {item.group}, Type: {item.item_type}, Amount:{item.amount}\n")
    print('------End of list-------')
# Create the root window
root = tk.Tk()

# Set the dimensions of the window
root.geometry("800x600")

# Create a text area
text_area = tk.Text(root)

# Add the text area to the window
text_area.pack(fill=tk.BOTH, expand=True)


# Create three buttons using TKiner 
button_available = tk.Button(root, text="Available items", command=print_items_with_positive_amount)
button_not_available = tk.Button(root, text="Not available items",command=print_items_with_not_positive_amount)
button_average_price = tk.Button(root, text="Average price",command=print_average_prices_by_group)

# Add the buttons to the window using TKiner 
button_available.pack(side=tk.LEFT, padx=10, pady=10)
button_not_available.pack(side=tk.LEFT, padx=10, pady=10)
button_average_price.pack(side=tk.LEFT, padx=10, pady=10)

# Run the main loop
root.mainloop()
