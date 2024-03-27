pizzas = ['carbonara', '4 queijos', 'pepperoni']

for pizza in pizzas:
    print(f"I like {pizza.title()} pizza")

print("I really love pizza!")

animals = ["dog", "cat", "fish"]

for animal in animals:
    print(f"{animal.title()} would make a great pet.")

print(f"Any of these animals would make a great pet!")

print("\n--------------------------------\n")

#numbers lists w/ loops
numbers = list(range(0, 1_000_001))

print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

odd_numbers = list(range(0, 21, 2))

for odd_number in odd_numbers:
    print(odd_number)

print("\n--------------------------------\n")

multiples_three = list(range(0, 31, 3))

for i in multiples_three:
    print(i)

cubes_list = []

for cubes in range(0, 11):
    cubes_list.append(cubes ** 3)

print(f"Cubes: {cubes_list}")

cubes_list2 = [value ** 3 for value in range(0, 11)]

print(cubes_list2)