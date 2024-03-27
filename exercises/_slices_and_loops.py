players = ["charles", "martina", "michael", "florence", "eli"]

print(f"The first three items in the list are: {players[:3]}")
print(f"Three items from the middle of the list are: {players[2:4]}")
print(f"The last three items in the list are: {players[-3:]}")

pizzas = ['carbonara', '4 queijos', 'pepperoni']

friends_pizzas = pizzas[:]


pizzas.append("tropical")
friends_pizzas.append("frango")

print("\nMy favourite pizzas are: ")

for pizza in pizzas:
    print(pizza)

print("\nMy friend's favourite pizzas are: ")

for f_pizza in friends_pizzas:
    print(f_pizza)