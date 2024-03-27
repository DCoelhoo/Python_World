car = 'ferrari'

print("Is car == 'ferrari' ? I predict true")
print(car == 'ferrari')

print("\nIs car == 'tesla' ? I predict false")
print(car == 'tesla')

country = ['japan', 'brazil', 'norway', 'england']

print("\nIs portugal in the list ? I predict false")
print('portugal' in country)

print("\nIs Spain not in the list ? I predict true")
print('spain' not in country)

age = 20

print("\nYou are: ")

if age < 2:
    print("baby")
elif age < 4:
    print("toddler")
elif age < 13:
    print("kid")
elif age < 20:
    print("teen")
elif age < 65:
    print("adult")
else:
    print("elder")