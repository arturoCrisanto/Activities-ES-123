# Activity: Contact List

Create a simple program to store and display contacts using a list of dictionaries.

## Instructions:

1. Each contact should have:

- "`name`" (string)
- "`phone`" (string)

2. The user should be able to:

- `View` all contacts
- `Add` a new contact
- `Exit` the program

## Example Output:

```bash
1. View Contacts
2. Add Contact
3. Exit
Enter your choice: 1

Contacts List:
--------------
Name: Alice, Phone: 123-4567
Name: Bob, Phone: 987-6543

1. View Contacts
2. Add Contact
3. Exit
Enter your choice: 2
Enter contact name: Charlie
Enter phone number: 555-1234
Contact added successfully!

1. View Contacts
2. Add Contact
3. Exit
Enter your choice: 3
Goodbye!
```

Sample list with Dictionaries:

```bash
contacts = [
    {"name": "Alice", "phone": "123-4567"},
    {"name": "Bob", "phone": "987-6543"}
]
```

## hint:

use `while loop` for the looping and put the conditions inside
