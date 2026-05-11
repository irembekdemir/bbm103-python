# Simple Contact Manager (Python CLI Project)

A simple command-line contact management system built in Python.
Users can add, view, edit, and delete contacts through a menu-driven interface.

##✨ Features
➕ Add new contacts (Name, Phone, Email, Country)
📋 View all contacts in a formatted table
✏️ Edit existing contacts (search by name or partial match)
🗑️ Delete contacts with confirmation
🔍 Smart search (partial name matching supported)
⚠️ Input validation (phone number, empty fields, cancel option)
🧠 Data Structure

- Contacts are stored as a list of dictionaries:
```
contacts = [
    {
        "Name": "John",
        "Phone": "12345678901",
        "Email": "john@mail.com",
        "Country": "USA"
    }
]
```
- Fields are dynamically managed using:
```
CONTACT_INFOS = ("Name", "Phone", "Email", "Country")
```

## 🛠️ How It Works

The program runs a loop-based menu system:

1. Add New Contact
2. View All Contacts
3. Edit Contact
4. Delete Contact
5. Exit

Each operation is handled by a separate function:
```
add_new_contact()
view_contacts()
edit_contact()
delete_contact()
run_manager()
```

## 🔍 Key Design Decisions
✔ Input Validation
- Phone numbers must be exactly 11 digits
- Empty fields are not allowed (except cancel option)
  
✔ Flexible Search
- Partial name matching supported
- Multiple matches handled with selection menu
  
✔ Safe Deletion
- Requires user confirmation before deleting contacts
  
✔ Dynamic Field System
- Uses tuple CONTACT_INFOS to avoid hardcoding fields
  
## 🚀 How to Run
``` bash
python main.py
````

Or with input redirection (optional):
```bash
python main.py input.txt
```

## Learning Goals

This project demonstrates:

- Python functions & modular design
- Dictionaries and lists usage
- Input validation techniques
- CLI menu systems
- Basic CRUD operations (Create, Read, Update, Delete)
 
## Notes
- This is a console-based project (no GUI)
- Data is stored in memory (not persistent storage)

## 👨‍💻 Author
Built as a beginner-friendly Python project to practice structured programming and CRUD logic by [irem bekdemir](https://github.com/irembekdemir)
