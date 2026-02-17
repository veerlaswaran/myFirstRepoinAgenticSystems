def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def has_admin_access(roles):
    return "admin" in roles

def main():
    users = [
        {
            "name": "Alice",
            "scores": [80, 85, 90, 75],
            "roles": {"editor", "admin"}
        },
        {
            "name": "Bob",
            "scores": [60, 55, 70],
            "roles": {"viewer"}
        },
        {
            "name": "Charlie",
            "scores": [95, 88, 92, 85],
            "roles": {"editor", "viewer"}
        }
    ]

    for user in users:
        name = user["name"]
        avg_score = calculate_average(user["scores"])
        admin_access = has_admin_access(user["roles"])

        print(f"Name: {name}")
        print(f"Average Score: {avg_score:.2f}")
        print(f"Admin Access: {admin_access}")
        print("-" * 30)

main()
