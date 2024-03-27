#Tuples are lists that can´t be changed (are immutable)

buffet = ('carne', 'batatas', 'peixe', 'arroz', 'massa')

print("The Buffet has: ")

for food in buffet:
    print(food)

buffet = ('carne', 'batatas', 'peixe', 'vegetais', 'salada')

print("\nThe Buffet has now: ")

for food in buffet:
    print(food)