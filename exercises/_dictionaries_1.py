person_0 = {
    "first_name" : "jill",
    "last_name" : "reed",
    "age" : "33",
    "city" : "liverpool"
}

person_1 = {
    "first_name" : "john",
    "last_name" : "doe",
    "age" : "26",
    "city" : "manchester"
}

person_2 = {
    "first_name" : "hannah",
    "last_name" : "brown",
    "age" : "21",
    "city" : "london"
}

people = [person_0, person_1, person_2]

for person in people:
    print(f"\nFull Name: {person["first_name"].title()} {person["last_name"].title()}")
    print(f"Age: {person["age"].title()}")
    print(f"City: {person["city"].title()}")

print("\n----------------\n")

favourite_nr = {
    "Diogo" : 22,
    "João" : 8,
    "Gabriel" : 18,
    "Tiago" : 44,
}

for name, number in favourite_nr.items():
    print(f"\nName: {name}")
    print(f"Favourite Number: {number}")
    if number == 22:
        print("Nice number!")

print("\n----------------\n")

pet_0 = {
    "name" : "ben",
    "type" : "dog",
    "owner" : "fernando",
    "color" : "white",
}

pet_1 = {
    "name" : "speed",
    "type" : "horse",
    "owner" : "diogo",
    "color" : "black",
}

pet_2 = {
    "name" : "iris",
    "type" : "cat",
    "owner" : "carlos",
    "color" : "gray",
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()} -> {value.title()}")
    print("\n --- \n")