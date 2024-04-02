

while True:

    age = int(input("How old are you? \n(Write 0 to finish the program) "))
    
    if age == 0:
        break;
    elif age <= 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is 10€")
    else:
        print("Your ticket is 15€")
