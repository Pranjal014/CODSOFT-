# Contact book to store, add, view, search, update, and delete contacts

# Dictionary to store contacts
contacts = {}

# Function to add a new contact
def Add_Contact():
    name = input("Enter contact name: ").strip().lower()
    phone = input("Enter contact phone number: ").strip()
    contacts[name] = {
        "phone": phone,
    }
    print(f"\nContact {name} added successfully!\n")

# Function to view all contacts
def View_Contacts():
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name.title()}, Phone: {details['phone']}")
    else:
        print("\nNo contacts found!\n")

# Function to search for a contact by name or phone number
def Search_Contact():
    search_term = input("Enter name or phone number to search: ").strip().lower()
    found = False
    for name, details in contacts.items():
        if search_term == name or search_term == details['phone']:
            print(f"\nFound Contact:\nName: {name.title()}, Phone: {details['phone']}")
            found = True
            break
    if not found:
        print("\nContact not found.\n")

# Function to update a contact
def Update_Contact():
    name = input("Enter the name of the contact to update: ").strip().lower()
    if name in contacts:
        phone = input(f"Enter new phone number for {name.title()} (current: {contacts[name]['phone']}): ").strip()
        contacts[name] = {
            "phone": phone,
        }
        print(f"\nContact {name.title()} updated successfully!\n")
    else:
        print("\nContact not found.\n")

# Function to delete a contact
def Delete_Contact():
    name = input("Enter the name of the contact to delete: ").strip().lower()
    if name in contacts:
        del contacts[name]
        print(f"\nContact {name.title()} deleted successfully!\n")
    else:
        print("\nContact not found.\n")

# Function to display the menu
def Display_Menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

# Main program loop
def Contact_Book():
    while True:
        Display_Menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            Add_Contact()
        elif choice == '2':
            View_Contacts()
        elif choice == '3':
            Search_Contact()
        elif choice == '4':
            Update_Contact()
        elif choice == '5':
            Delete_Contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select again.\n")

# Run the Contact Book
Contact_Book()
