score_input = input("Enter Your Marks :: ")
try: 
    score = int(score_input) 
    if score >= 50:
        print('Pass')
    else:
        print('Fail')
except ValueError:
    print('enter numeric input only')