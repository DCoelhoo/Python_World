name = input("What is your name?")
print(f"Hello, {name.title()}!")

age = input("How old are you?")
age = int(age)

if age <= 18:
    print("You can't drink alcohol.")
else:
    print("What do you want do drink?")