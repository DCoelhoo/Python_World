active = True
prompt = "\nHello, what toppings do you want in your pizza?"
prompt += "\n(Enter 'quit' to stop the program) "

while active:

    topping = input(prompt).lower()

    if topping == "quit":
        active = False
    else:
        print(f"Your pizza will have {topping.title()}")

