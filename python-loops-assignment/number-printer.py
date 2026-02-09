loop_input = input("Enter a number: ")
try:
    max_value = int(loop_input)

    for i in range (max_value+1):
        print(i)

except ValueError:
    print("Invalid input. Please enter a numeric value.")        