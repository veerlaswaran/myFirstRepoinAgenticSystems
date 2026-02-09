total = 0

while True:
    num_input = input("Enter a number: ")
    try:
        num = int(num_input)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if num == 0:
        break
    total += num
print("Total:", total)
