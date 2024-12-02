def view_contacts(all_contacts):
    if all_contacts:
        print("All Contacts Are: ")
        for i, contact in enumerate(all_contacts):
            print(f"{i}. Name: {contact['Name']}, Email: {contact['Email']}, Name: {contact['Mobile']}, Name: {contact['Address']}")

    else:
        print("Contact List is Empty")