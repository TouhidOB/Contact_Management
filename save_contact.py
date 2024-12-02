import csv

def save_contact(all_contact):
    with open('contact_list.csv', 'w') as fp:
        writer = csv.DictWriter(fp, fieldnames=["Name", "Email", "Mobile", "Address"])
        writer.writeheader()
        writer.writerows(all_contact)