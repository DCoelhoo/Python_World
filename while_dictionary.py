dream_vacation = {}
active = True

while active:
    name = input("What is your name? ").lower()
    vacation = input("Where your dream vacation would be? ").lower()

    dream_vacation[name.title()] = vacation.title()

    repeat = input("Would you like me to ask another person? Y/N ").lower()

    if repeat == 'n':
        active = False

print("\n--- Poll Results ---\n")
for name, vaction in dream_vacation.items():
    print(f"{name} would like to go to {vacation}")