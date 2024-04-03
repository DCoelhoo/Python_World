class Restaurant:

    def __init__(self, name, type):
        ''' Initialize name and type attributes.''' 
        self.name = name
        self.type = type
        self.served = 0

    def describe_restaurant(self):
        ''' Method used to describe the restaurant. '''
        print(f"The restaurant {self.name} is a {self.type} type of restaurant.")
    
    def open_restaurant(self):
        ''' Method used to open the restaurant. '''
        print(f"The restaurant {self.name} is open!!")
    
    def customers_served(self):
        ''' Method used to count how many customers have been served. '''
        print(f"A total of {self.served} customers have been served today!")
    
    def set_number_served(self, customers):
        ''' Method to change how many customers have been served. '''
        self.served = customers
    


jp_restaurant = Restaurant("Sakura", "Japanese")

jp_restaurant.describe_restaurant()
jp_restaurant.open_restaurant()

print("\n --- \n")

jp_restaurant.customers_served()

jp_restaurant.set_number_served(20)
jp_restaurant.customers_served()
