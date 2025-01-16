import csv


"""This is the program for creating a phonebook and working with it."""

HEADER = """Personal phonebook management program.
Functionality allows you to:
"""


def print_functionality():
    print(HEADER)
    print('0. Print help message.')
    print("1. Create a new contact.")
    print("2. Search contacts.")
    print("3. Delete contact.")
    print("4. Update contact.")
    print("5. Show all contacts.")
    print("-" * 30)
    print("9. Exit")


def main():
    print_functionality()
    while True:
        choice = int(input("Please, make a choice: "))
        if choice == 0:
            print_functionality()
        elif choice == 1:
            first_name = input("Please, enter first name: ")
            last_name = input("Please, enter last name: ")
            phone_number = input("Please, enter phone number: ")
            country = input("Please, enter country: ")
            create_contact(first_name, last_name, phone_number, country)
            print("Contact has been added")
        elif choice == 2:
            # print("Choose filter")
            # print("1. By first name.")
            # print("2. By last name.")
            # print("3. By phone number.")
            # print("4. By city or state.")
            # if choice == 1:
            search_contact(key_word=input("Enter key word for searching: "))
        elif choice == 3:
            delete_contact()
        elif choice == 5:
            show_phonebook()
        elif choice == 9:
            exit()
        else:
            print_functionality()
            print("Wrong choice. Please, try again.")

def create_contact(first_name, last_name, phone_number, country):
    """This function is for creating a new contact."""
    with open('db.сsv', 'a+') as file:
        file.write(f"{first_name}, {last_name}, {phone_number}, {country}\n")


def search_contact(key_word):
    """This function is for searching contacts in phonebook.
    You can search by:
    - first name
    - last name
    - phone number
    - city or state"""

    result = []

    with open('db.сsv', 'r') as file:
        for line in file:
            if key_word.lower() in line.lower():
                result.append(line.strip())

    if result:
        if len(result) == 1:
            print(f"Found 1 contact: {result[0].replace(',', ' ')}")
        else:
            print(f"Found {len(result)} contacts:")
            for idx, contact in enumerate(result, start=1):
                print(f"{idx}. {contact.replace(',', ' ')}")
    else:
        print("Haven't found any contact.")


def delete_contact():
    with open('db.сsv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    choice = int(input("If you want to see full list, enter '1'\n"
                       "If you want search contact by key word, enter '2'\n"
                       "Enter your choice: "))
    if choice == 1:
        show_phonebook()
        del_choice = int(input("Which contact do you want to delete?\n"
                               "Enter a number of contact: "))
        contact_to_del = rows[del_choice - 1]
        conf = input(f"Do you want to delete {''.join(contact_to_del)}?\n"
                      "Please, enter y/n: ")
        if conf.lower() == 'y':
            del rows[del_choice - 1]
            with open('db.сsv', 'w', newline='') as file:
               writer = csv.writer(file)
               writer.writerows(rows)
            print("Contact has been deleted.")
        elif conf.lower() == 'n':
            print("Deletion canceled.")
            exit()
        else:
            print("Your answer must be y or n")
    if choice == 2:
        with open('db.сsv', 'r') as file:
            rows = file.readlines()
        key_word = input("Enter key word for searching: ")
        result = [line.strip() for line in rows if key_word.lower() in line.lower()]

        if len(result) == 1:
            print(f"Found 1 contact: {result[0]}")
            choice = input(f"Do you want to delete it? (y/n): ")
            if choice.lower() == 'y':
                with open('db.сsv', 'w') as file:
                    for line in rows:
                        if result[0] not in line.strip():
                            file.write(line)
                print("Contact has been deleted.")
            elif choice.lower() == 'n':
                print("Deletion canceled.")
            else:
                print("Invalid choice. Exiting.")

        elif len(result) > 1:
            print("Found the following contacts:")
            for idx, contact in enumerate(result, start=1):
                print(f"{idx}. {contact}")

            choice = int(input("Which contact do you want to delete?\n"
                               "Enter a number: "))
            contact_to_del = result[choice - 1]

            with open('db.сsv', 'w') as file:
                for line in rows:
                    if contact_to_del not in line.strip():
                        file.write(line)
            print("Contact has been deleted.")
        else:
            print("No contacts found.")
            exit()

# def update_contact():
#     show_phonebook()
#     choice = int(input("Which contact do you want to delete?\n"
#                        "Enter a number of contact or if you want to search by key word, enter '0': "))
#



def show_phonebook():
    result = []
    with open('db.сsv') as file:
        for line in file:
            result.append(line.strip())
    for idx, contact in enumerate(result, start=1):
        print(f"{idx}. {contact}")



if __name__ == "__main__":
    main()