balance_input = input("Enter your account balance: ")
withdraw_input = input("Enter withdrawal amount: ")
verified_input = input("Are you verified? (True/False): ")

try:
    balance = int(balance_input)
    withdrawal = int(withdraw_input)

    # Normalize Boolean input
    if verified_input.lower() == "true":
        verified = True
    elif verified_input.lower() == "false":
        verified = False
    else:
        print("Invalid input for verification status. Please enter True or False.")
        verified = None

    if verified is not None:
        if verified and withdrawal <= balance:
            print("Transaction successful")
        else:
            print("Transaction denied")

except ValueError:
    print("Invalid numeric input. Please enter integers for balance and withdrawal amount.")
