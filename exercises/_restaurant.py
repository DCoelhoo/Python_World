from _restaurant_class import *

jp_restaurant = Restaurant("Sakura", "Japanese")

jp_restaurant.describe_restaurant()
jp_restaurant.open_restaurant()

print("\n --- \n")

jp_restaurant.customers_served()

jp_restaurant.set_number_served(20)
jp_restaurant.customers_served()

ice_restaurant = IceCreamStand("Ice", "Ice Cream")
ice_restaurant.decribe_flavor()