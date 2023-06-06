import sqlite3

# Connect to the database
conn = sqlite3.connect('food_ordering.db')
cursor = conn.cursor()
"""
#If table already exist, drop it. 
cursor.execute(
    
)
cursor.execute('''
    #DROP TABLE menu
    '''
)
"""
# Create the menu table
cursor.execute('''
    CREATE TABLE menu (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER1
    )
''')

# Insert some menu items
cursor.execute('''
    INSERT INTO menu (name, price) VALUES
        ("Cheeseburger", 5),
        ("Pizza", 10),
        ("Fried Chicken", 8),
        ("Salad", 6)
''')

# Create the orders table
cursor.execute('''
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY,
        item_id INTEGER,
        quantity INTEGER,
        FOREIGN KEY (item_id) REFERENCES menu(id)
    )
''')

# Function to display the menu
def show_menu():
    cursor.execute('''
        SELECT id, name, price FROM menu
    ''')
    menu_items = cursor.fetchall()
    for item in menu_items:
        print(f"{item[0]}. {item[1]} - ${item[2]}")

# Function to place an order
def place_order():
    show_menu()
    item_id = int(input("Enter the ID of the item you'd like to order: "))
    quantity = int(input("Enter the quantity: "))
    cursor.execute('''
        INSERT INTO orders (item_id, quantity) VALUES (?, ?)
    ''', (item_id, quantity))
    conn.commit()
    print("Order placed successfully!")

# Main loop
while True:
    action = input("What would you like to do? (1.view menu / 2.place order / 3.exit) Enter the number please ")
    if action == "1":
        show_menu()
    elif action == "2":
        place_order()
    elif action == "3":
        break

# Close the database connection
conn.close()
