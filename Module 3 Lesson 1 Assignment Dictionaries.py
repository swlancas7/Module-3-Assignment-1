# Task 1: Restaurant Menu Update

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
# Add a new category called "Beverages" with at least two items.
categories = {
    "Beverage": ["Water", "Skim Milk", 
    "Reduced Sugar Hershey's Chocolate Skim Milk"],
}

print(categories)

# Update the price of "Steak" to 17.99.

restaurant_menu["Steak"] = 17.99

print(restaurant_menu)

# Remove "Bruschetta" from "Starters"

removed_Starters = restaurant_menu["Starters"].pop("Bruschetta")
print(removed_Starters)
print(restaurant_menu)

# Task 2: Customer Service Ticket Tracker 

# Initial sample tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Function to open a new service ticket
def open_ticket(customer, issue):
    ticket_id = f'Ticket{len(service_tickets) + 1:03d}'
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
    print(f"New ticket opened: {ticket_id}")

# Function to update the status of an existing ticket
def update_ticket_status(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]['Status'] = status
        print(f"Ticket {ticket_id} status updated to {status}")
    else:
        print(f"Ticket {ticket_id} not found")

# Function to display all tickets or filter by status
def display_tickets(filter_status=None):
    for ticket_id, details in service_tickets.items():
        if filter_status is None or details['Status'] == filter_status:
            print(f"ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")

# Initialize with some additional sample tickets
open_ticket("Charlie", "Forgot password")
open_ticket("Dave", "Account locked")