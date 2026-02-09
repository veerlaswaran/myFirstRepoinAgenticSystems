age_input = input("Enter your age: ")
id_input = input("Do you have an ID card (True/False): ")

try:
    age = int(age_input)  # Convert age to integer

    # Normalize Boolean input
    if id_input.lower() == "true":
        has_id = True
    elif id_input.lower() == "false":
        has_id = False
    else:
        print("Invalid input for ID card. Please enter True or False.")
        has_id = None

    if has_id is not None:
        if age >= 18 and has_id:
            print("Entry allowed")
        else:
            print("Entry denied")

except ValueError:
    print("Invalid age. Please enter a numeric value.")
