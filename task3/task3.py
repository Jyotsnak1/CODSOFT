class Contact_book:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

contacts = []

while True:
    print("\n  Contact book using python  ")
    print("1. View Contact List")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Contact List:")
        for contact in contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone_number}")
    elif choice == "2":
        keyword = input("Enter name or phone number to search: ")
        found_contacts = []
        for contact in contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        if found_contacts:
            print("Found contacts:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No contacts found.")
    elif choice == "3":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        new_contact = Contact_book(name, phone_number, email, address)
        contacts.append(new_contact)
        print("Contact added successfully.")
    elif choice == "4":
        name = input("Enter name of the contact to update: ")
        contact_found = False
        for contact in contacts:
            if contact.name == name:
                new_phone_number = input("Enter new phone number (leave blank to keep current): ")
                new_email = input("Enter new email (leave blank to keep current): ")
                new_address = input("Enter new address (leave blank to keep current): ")
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print("Contact updated successfully.")
                contact_found = True
                break
        if not contact_found:
            print("Contact not found.")
    elif choice == "5":
        name = input("Enter name of the contact to delete: ")
        contact_found = False
        for contact in contacts:
            if contact.name == name:
                contacts.remove(contact)
                print("Contact deleted successfully.")
                contact_found = True
                break
        if not contact_found:
            print("Contact not found.")
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")