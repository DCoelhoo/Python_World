current_usernames = ["kafka", "admin", "d4v1d", "adam", "coelho"]
new_usernames = ["extr3me", "badl1fe", "Kafka", "Adam", "easy"]

if current_usernames:
    for user in current_usernames:
        if user == "admin":
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")


for new_user in new_usernames:
    if new_user.lower() in current_usernames:
        print("You need to enter a new Username")
    else: 
        print("Your username is available")

ordinal_numbers = list(range(1, 10))

print("\nOrdinal Numbers:")

for number in ordinal_numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")