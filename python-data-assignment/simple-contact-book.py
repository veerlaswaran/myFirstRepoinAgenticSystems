def main():
    contacts = {
        "Ravi": "9876543210",
        "Anita": "9123456780",
        "Suresh": "9988776655"
    }

    print("All Contacts:")
    for name, number in contacts.items():
        print(f"{name}: {number}")

    search_name = input("\nEnter a name to search: ")

    if search_name in contacts:
        print(f"Phone number of {search_name}: {contacts[search_name]}")
    else:
        print("Contact not found")

main()
