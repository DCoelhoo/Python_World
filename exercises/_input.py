people = int(input("Hello, how many are you? "))

if people > 8:
    print("I'm sorry, but you'll have to wait for a table.")
else:
    print("Your table is ready.")

print("\n----------------\n")

number_asked = int(input("Choose a number: "))

if number_asked % 10 == 0:
    print("Is a multiple of 10.")
else:
    print("Isn't a multiple of 10.")