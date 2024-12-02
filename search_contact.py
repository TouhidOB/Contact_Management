def search_contact(all_contacts):
    search_item = input("Searching By Name: ")

    matching_item = []

    for c in all_contacts:
        print(c['Name'].lower())
        print(search_item.lower())
        if search_item.lower() in c['Name'].lower():
            matching_item.append(c)



    if matching_item:
        for i, contact in enumerate(matching_item, start=1):
            print(f"{i}. Name: {contact['Name']}, Email: {contact['Email']}, Mobile: {contact['Mobile']}, Address: {contact['Address']}")
    else:
        print("No Contact Found.")