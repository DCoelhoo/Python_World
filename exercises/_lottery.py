from random import choice

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d"]
winner_ticket = []
win = False
attempts = 0
my_ticket = []

for i in range(1, 5):
    pick = choice(lottery)
    winner_ticket.append(pick)

print(f"The ticket matching the numbers: {winner_ticket} has won the lottery!")

while win == False:
    attempts += 1
    my_ticket = []

    for i in range(1, 5):
        mypick = choice(lottery)
        my_ticket.append(mypick)

    if my_ticket == winner_ticket:
        print(f"You tried {attempts} times to win the lottery")
        print(f"The ticket : {my_ticket} won!")
        win = True
    else:
        print(f"The ticket {my_ticket} did not win after {attempts}")

