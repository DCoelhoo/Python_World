from class_car import EletricCar

my_leaf = EletricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.get_range()


