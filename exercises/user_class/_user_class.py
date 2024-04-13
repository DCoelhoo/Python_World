class User:
    
    def __init__(self, first_name, last_name, username, password):
        self.fname = first_name
        self.lname = last_name
        self.username = username
        self.password = password
        self.login_attempts = 0
    
    def describe_user(self):
        ''' Describe user information '''
        print(f"Name: {self.fname} {self.lname}")
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")
        print(f"Login Attemps: {self.login_attempts}")

    def greet_user(self):
        '''Greets the user '''
        print(f"Welcome back {self.username}")

    def increment_login_attempts(self):
        ''' Increase the login attempts by 1. '''
        self.login_attempts += 1

    def reset_login_attempts(self):
        '''Reset the login attempts to 0. '''
        self.login_attempts = 0


user = User("Diogo", "Gonçalves", "dgoncalves", "1234")
user2 = User("Miguel", "Antunes", "mantunes", "5678")

user.describe_user()
user.greet_user()

print("\n --------- \n")

user2.describe_user()
user2.greet_user()

for attempts in range(1, 10):
    user.increment_login_attempts()

user.describe_user()

print("\n --------- \n")

user.reset_login_attempts()

user.describe_user()

print("\n --------- \n")



