from _user_class import User

class Admin(User):
    '''Class created to admins'''

    def __init__(self, first_name, last_name, username, password):
        super().__init__(first_name, last_name, username, password)
        self.privileges = Privileges()




class Privileges:
    '''Simple class for priviliges'''

    def __init__(self):
        self.privileges = [
            "can add post", 
            "can delete post", 
            "can ban user", 
            "can create user"
        ]

    def show_previleges(self):
        for privilege in self.privileges:
            print(f"Admin can: {privilege}")