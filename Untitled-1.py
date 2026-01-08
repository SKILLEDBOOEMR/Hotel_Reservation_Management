def add_customer():
    name = input(" customer name: ")
    phone = input(" phone number: ")
    email = input(" email: ")
    address = input(" address: ")

    with open("customers.txt", "a") as file:
        file.write(f"{name}, {phone}, {email}, {address}\n")

    print("Customer added successfully!\n")

def add_order():
    order_id = input(" Order ID: ")
    customer_name = input(" Customer Name: ")
    product = input(" Product: ")
    quantity = input(" Quantity: ")

    with open("orders.csv", "a") as file:
        file.write(f"{order_id},{customer_name},{product},{quantity}\n")

    print("Order added successfully!\n")

def view_customers():
    try:
        with open("customers.txt", "r") as file:
            print("\n-Customers-")
            for line in file:
                print(line.strip())
            print()
    except :
        print("no customers found!\n")

def view_orders():
    try:
        with open("orders.csv", "r") as file:
            print("\n-Orders-")
            for line in file:
                print(line.strip())
            print()
    except :
        print("No orders found!\n")

def search_customer():
    name = input(" customer name to search: ")

    try:
        found = False
        with open("customers.txt", "r") as file:
            for line in file:
                customer_name = line.split(",")[0].strip()

                if customer_name.lower() == name.lower():
                    print("Found the customer!\n")
                    found = True
                    break

        if not found:
            print("Customer not found\n")

    except :
        print("Customer file not found\n")

def menu():
    while True:
        print("Customer and Order Manager ")
        print("1. Add Customer")
        print("2. Add Order")
        print("3. View Customers")
        print("4. View Orders")
        print("5. Search Customer")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            add_order()
        elif choice == "3":
            view_customers()
        elif choice == "4":
            view_orders()
        elif choice == "5":
            search_customer()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


menu()

