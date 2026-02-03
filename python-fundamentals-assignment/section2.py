accuracy_input = input("Enter model accuracy : ")
if type(accuracy_input) is int:
    accuracy = float(accuracy_input)
    print(f"Model accuracy is {accuracy}")
else:
    print('enter numeric input only')