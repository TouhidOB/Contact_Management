def remove_contact(all_contacts):
    item = input("Enter The Number You Want To Delete: ").strip()
    

    for i, contact in enumerate(all_contacts):
        if contact['Mobile'] == item:
            all_contacts.pop(i)
            
            print(f"Contact with Mobile Number {item} has been deleted.")
            break