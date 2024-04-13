from class_car import Car
from class_eletric_car import EletricCar as EC

''' Import like this if you want to import multiple classes.
    If you want all classes:
        from class_car import *
'''

my_mustang = Car("Ford", "Mustang", 2024)
print(my_mustang.get_descriptive_name())

print("\n --------- \n")

my_leaf = EC("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())