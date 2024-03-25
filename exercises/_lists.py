friends = ['Addyson Lawson', 'Lane Price', 'Piper Boyer', 'Zeke Raymond']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

cars = ['tesla', 'ferrari', 'audi', 'bmw']
message = f"I would like to own a {cars[0].title()} car."
print(message)

invite_names = ['Karen Carpenter', 'Jeremy Eaton', 'Miley Walters']
print("------- INVITES -------")
print(f"Hello {invite_names[0]}, I would like tou invite you to dinner.")
print(f"Hello {invite_names[1]}, I would like tou invite you to dinner.")
print(f"Hello {invite_names[2]}, I would like tou invite you to dinner.")
print("--------------")

print(f"{invite_names[2]} can't make it.")

del invite_names[1]
invite_names.insert(1, 'Colson Magana')
print("------- INVITES -------")
print(f"Hello {invite_names[0]}, I would like tou invite you to dinner.")
print(f"Hello {invite_names[1]}, I would like tou invite you to dinner.")
print(f"Hello {invite_names[2]}, I would like tou invite you to dinner.")
print("--------------")

print("I found a bigger table.")
invite_names.insert(0, 'Mina Hurley')
invite_names.insert(2, 'Van Hogan')
invite_names.append('Clay Cain')

print("------- INVITES -------")
print(f"Hello {invite_names[0]}, I would like tou invite you to dinner.")
print(f"Hello {invite_names[1]}, I would like tou invite you to dinner.")
print(f"Hello {invite_names[2]}, I would like tou invite you to dinner.")
print(f"Hello {invite_names[3]}, I would like tou invite you to dinner.")
print(f"Hello {invite_names[4]}, I would like tou invite you to dinner.")
print(f"Hello {invite_names[5]}, I would like tou invite you to dinner.")
print("--------------")

print("Our new dinner table won't arrive in time. We only have space for two guests.")
pop1 = invite_names.pop()
print(f"I'm sorry {pop1}, I can't invite you to dinner")
pop2 = invite_names.pop()
print(f"I'm sorry {pop2}, I can't invite you to dinner")
pop3 = invite_names.pop()
print(f"I'm sorry {pop3}, I can't invite you to dinner")
pop4 = invite_names.pop()
print(f"I'm sorry {pop4}, I can't invite you to dinner")

print(f"Hello {invite_names[0]}, you are still invited to dinner.")
print(f"Hello {invite_names[1]}, you are still invited to dinner.")
print("------")
print(f"Invited Persons: {len(invite_names)}")
del invite_names[1]
del invite_names[0]


print(invite_names)

