from add_contact import add_new_contact
from view_contact import view_contacts
from search_contact import search_contact
from remove_contact import remove_contact


class Contact_management:
    all_contacts = []
    def __init__(self):
        print("Welcome To Contact Management System")
        print("0. Exit")
        print("1. View All Contacts")
        print("2. Add New Contact")
        print("3. Search Contact")
        print("4. Delete Contact")

        while True:
            option = input("Choose Your option: ")

            if option == '0':
                break

            elif option == '1':
                view_contacts(Contact_management.all_contacts)


            elif option == '2':
                print("Enter Your Contact Info")
                add_new_contact(Contact_management.all_contacts)

            elif option == '3':
                search_contact(Contact_management.all_contacts)
                

            elif option == '4':
                remove_contact(Contact_management.all_contacts)

            else:
                print("Please Choose A Right Option.")


Contact_management()