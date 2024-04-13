import class_car
import class_eletric_car as ec

''' import like this if you want an entire module.'''

my_mustang = class_car.Car("Ford", "Mustang", 2024)
print(my_mustang.get_descriptive_name())

print("\n --------- \n")

my_leaf = ec.EletricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())