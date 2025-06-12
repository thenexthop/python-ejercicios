class App:
    
    def __init__(self, users=0, storage=0, username="default"):
        self.users = users
        self.storage = storage
        self.username = username


    def login(self):
        if self.username == "admin":
            print("Welcome, admin user!")    
            print(f"Currently you have {self.users} users in your list.")    
        else:
            print("You are not allowed to logged in as a regular user.")    


    def increase_capacity(self, amount):
        self.storage += amount
        print(f"Now your storage capacity is {self.storage}.")    


obj1 = App(25, 105, "admin")
obj1.login()
obj1.increase_capacity(115)

obj2 = App()
obj2.login()

