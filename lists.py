bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])

cars = ['tesla', 'ferrari', 'audi', 'bmw']

#organize the list 
cars.sort()
#use .sort(reverse = True) if you want the list in reverse-alphabetical roder

#ornganizing temporarily
print(sorted(cars))


message = f"I would like to own a {cars[0].title()} car."
cars.append('porsche')
print(cars)

#inser the item in position 0
cars.insert(0, 'peugeot')
print(cars)

#deletes the item
del cars[3]
print(cars)

#pop removes and stores the data
popped_cars = cars.pop()
print(f"Popped cards: {popped_cars}")

first_owned = cars.pop(0)
print(f"The first car I owned was a {first_owned.title()}.")

#use remove if you don't know the index (position) of the item
cars.remove('audi')
print(cars)

#Reverse Order
cars.reverse()
print(cars)

#Finding the Length
print(len(cars))