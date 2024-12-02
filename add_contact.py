from save_contact import save_contact


def add_new_contact(all_contact):
    name = input("Name: ")
    email = input("Email: ")
    phone_number = input("Phone Number: ")
    address = input("Address: ")


    for c in all_contact:
        if c['Mobile'] == phone_number:
            print("This Number Is Already Exist")
            return


    contact = {
        "Name" : name,
        "Email" : email,
        "Mobile" : phone_number,
        "Address" : address,
    }


    all_contact.append(contact)
    save_contact(all_contact)
    print("1 Contact Added Successfully...!")