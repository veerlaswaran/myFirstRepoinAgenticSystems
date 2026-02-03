user_name = input("Enter Your Name :: ")
user_age = int(input("Enter Your Age :: "))
is_active_user = input("Are you a active user (True / False) :: ").strip().lower() == "true"

print(f"User {user_name} is {user_age} years old. Active status: {is_active_user}")