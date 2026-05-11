
CONTACT_INFOS = ("Name", "Phone", "Email", "Country") #tuple for dynamic headers

# 1) ADDING NEW CONTACTS

def add_new_contact(contacts):
    print("\n------ADD NEW CONTACT / Type 'Cancel' to return to menu------\n")

    new_contact = {}  #empty dictionary to be filled

    for info in CONTACT_INFOS:
        while True:
            val = input(f"Enter {info} (or 'cancel'):\n").strip()

            if val.lower() == "cancel":
                print("Operation cancelled. Returning to the main menu...")
                return

            #controlling empty inputs (except Phone)
            if info != "Phone" and val == "":
                print(f"Error: {info} cannot be empty.")
                return

            if info == "Phone":
                if len(val) != 11 or not val.isdigit():
                    print("Error: Phone number must be exactly 11 digits (no dashes or spaces).")
                    continue

            new_contact[info] = val
            break

    contacts.append(new_contact)  #adding dictionary to the contacts list: contacts = [{....}]
    print(f"Contact '{new_contact['Name']}' added successfully.\n")

# 2) VIEWING THE CONTACTS

def view_contacts(contacts):
    print("\n----- VIEW ALL CONTACTS -----")
    print("================================")

    if len(contacts) == 0:
        print("There are no contacts to display.\n")
        return

    header = "Index "
    for info in CONTACT_INFOS:
        header = header + "| " + info              #creating the header for the viewing section.
    print(header)
    print("================================")

    row = 1
    for contact in contacts:
        line = str(row) + "   "         #forming the header of the contacts table.
        for info in CONTACT_INFOS:
            line = line + "| " + contact[info] + " "
        print(line)
        row += 1

    print("================================")

# 3) SEARCH & EDIT CONTACT

def edit_contact(contacts):
    print("\n----- EDIT CONTACT -----\n")

    search_contact = input("Enter the name (or part of the name) of the contact to edit or type 'cancel' to return to menu:\n").strip()

    if search_contact.lower() == "cancel":  # case of cancel request
        print("Cancellation is successful, returning to the main menu...\n")
        return

    matches_edit= []                  #finding the result's matches

    for contact in contacts:
        if search_contact.lower() in contact["Name"].lower():
            matches_edit.append(contact)

    if len(matches_edit) == 0:
        print(f"No contacts found matching '{search_contact}'.\n")
        return

    if len(matches_edit) == 1:
        found = matches_edit[0]

    else:
        print("Multiple matches found. Please select one to edit:\n")
        count = 1
        for dict_matches in matches_edit:
            print("[" , count, "]", dict_matches["Name"], dict_matches["Phone"] )  # this will list the matching contacts
            count = count + 1

        choice_try = (input("\nEnter number of contact to edit / 0 for cancel: ")).strip()

        if choice_try.isdigit() == False:  #we need the input to be an integer no letters
            print("Invalid input. Redirecting...\n")
            return

        choice = int(choice_try) #to secure the input to be an integer

        if choice == 0:
            print("Cancellation is successful, returning to the main menu...\n")
            return

        if choice < 0 or choice > len(matches_edit):
            print("Invalid input.\n")
            return

        found = matches_edit[choice-1]

    print("\nEditing contact:" + found["Name"])
    print(" Which field do you want to change? :")
    print("1: Name (Current: " + found["Name"] + ")")
    print("2: Phone (Current: " + found["Phone"] + ")")
    print("3: Email (Current: " + found["Email"] + ")")
    print("4: Country (Current: " + found["Country"] + ")")

    choice2_try = input("\nEnter your choice (or 'cancel'):").strip()

    if choice2_try.isdigit() == False:

        if choice2_try.lower() == "cancel":
            print("Cancellation is successful, returning to the main menu...\n")
            return

        else:
            print("Invalid input. Redirecting...\n")
            return

    choice2 = int(choice2_try)

    if choice2 == 1:
        new_value = input("Enter new value for Name (or 'cancel'): \n").strip()

        if new_value.lower() == "cancel":
            print("Cancellation is successful, returning to the main menu...\n")
            return

        if new_value == "":
            print("ERROR: Name cannot be empty.")
            return

        found["Name"] = new_value
        print("Name updated to " + found["Name"])

    elif choice2 == 2:
        new_value = input("Enter new value for Phone (11 digits, or 'cancel'): \n").strip()
        if new_value.lower() == "cancel":
            print("Cancellation is successful, returning to the main menu...\n")
            return
        if new_value.isdigit() and len(new_value) == 11:
            found["Phone"] = new_value
            print("Phone updated for " + found["Name"] + " to " + found["Phone"])
        else:
            print("Invalid phone number.\n")
            return

    elif choice2 == 3:
        new_value = input("Enter new value for Email (or 'cancel'): \n").strip()
        if new_value.lower() == "cancel":
            print("Cancellation is successful, returning to the main menu...\n")
            return
        found["Email"] = new_value
        print("Email updated for " + found["Name"] + " to " + found["Email"])

    elif choice2 == 4:
        new_value = input("Enter new value for Country (or 'cancel'): \n").strip()
        if new_value.lower() == "cancel":
            print("Cancellation is successful, returning to the main menu...\n")
            return

        found["Country"] = new_value

        print("Country updated for " + found["Name"] + " to " + found["Country"])

# DELETE CONTACTS

def delete_contact(contacts):
    print("\n----- DELETE CONTACT -----\n")

    search_name_delete = input("Enter the name (or part of the name) of the contact to delete:\n").strip()

    if search_name_delete.lower() == "cancel":
        print("Cancellation is successful, returning to the main menu...\n")
        return

    matches_delete = []

    for contact in contacts:
        if search_name_delete.lower() in contact["Name"].lower():  #listing the matches for search
            matches_delete.append(contact)

    if len(matches_delete) == 0:
        print(f"No contacts found matching '{search_name_delete}'.\n")
        return

    if len(matches_delete) == 1:
        chosen_delete = matches_delete[0]

    else:
        print("Multiple matches found. Please select one to delete:\n")

        count = 1
        for delete in matches_delete:
            print("[", count, "]", delete["Name"], delete["Phone"])
            count = count + 1

          #securing the programme in case input will be a string
        choice_try = (input(" Enter number of contact to delete, or type 0 to cancel:\n ")).strip()

        if choice_try.isdigit() == False:
            print("Invalid input. Redirecting...\n")
            return

        choice = int(choice_try)

        if choice == 0:
            print("Cancellation is successful, returning to the main menu...\n")
            return

        if choice < 0 or choice > len(matches_delete): #securing the true range for choice
            print("Invalid input. Redirecting...\n.")
            return

        chosen_delete = matches_delete[choice - 1]

# Confirming the deletion

    confirmation = input(f"Are you sure you want to delete '{chosen_delete['Name']}' ? (Yes/No):\n").strip()

    if confirmation.lower() == "yes":
        contacts.remove(chosen_delete)
        print(f"Contact '{chosen_delete['Name']}' deleted successfully.\n")

    elif confirmation.lower() == "no":
        print("Delete cancelled.\n")

    else:
        print("Invalid input.\n")

def run_manager(contacts):
    while True:
        print("============================")
        print("SIMPLE CONTACT MANAGER MENU")
        print("============================")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        print("--------------------------------")

        choice = input("Enter your choice (1-5):\n")

        if choice == "1":
            add_new_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            edit_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            print("Exiting Contact Manager. Goodbye!\n")
            break

        else:
            print("Invalid choice. Redirecting...\n")

# given code template

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        try:
            sys.stdin = open(input_file_path, 'r')
        except FileNotFoundError:
            sys.exit(1)

    contacts_list = []
    run_manager(contacts_list)

    if len(sys.argv) > 1:
        sys.stdin.close()
