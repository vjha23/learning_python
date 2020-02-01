class User():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.login_attempt=0
    def describe(self):
        print("user name is "+self.fname +self.lname)
    def greet(self):
        print(self.fname + self.lname +" how you doing?")
    def incremental_login_attempts(self):
        self.login_attempt+=1
    def reset_login_attempts(self):
        self.login_attempt=0
    def read_login(self):
        print("total no of attempts are "+str(self.login_attempt))

user=User("vijay","jha")
user.describe()
user.greet()
user.incremental_login_attempts()
user.incremental_login_attempts()
user.incremental_login_attempts()
user.incremental_login_attempts()
user.incremental_login_attempts()
user.read_login()
user.reset_login_attempts()
user.read_login()

