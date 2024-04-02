sandwich_order = [
    "frango grelhado",
    "pastrami",
    "queijo e presunto",
    "atum com maionese",
    "pastrami",
    "vegetais assados",
    "peru com abacate",
    "pastrami",
]

finished_sandwiches = []

print("We ran out of Pastrami!!!")

while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

while sandwich_order:
    sandwich = sandwich_order.pop()
    print(f"I made you {sandwich} sandwich!")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} is finished!")