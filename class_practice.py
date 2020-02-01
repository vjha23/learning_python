"""class Dog():
    def __init__(self,name,age):
        self.name=name # initialize name and age attributes
        self.age=age
    def sit(self):
        print(self.name.title() + "is now sitting")
    def roll_over(self):
        print(self.name.title() + "is rolling over")
"""
""""# making the instances of class
my_dog=Dog('willie',7)
print("my dog name is "+my_dog.name.title() + ".")
print("my dog is "+str(my_dog.age) + "years old.")
# calling methods
my_dog.sit()
my_dog.roll_over()"""
"""# creating multiple instances
my_dog=Dog("willie",7)
your_dog=Dog("lucy",6)

print("my dog name is "+my_dog.name)
print("my dog is "+str(my_dog.age)+"years old")
my_dog.sit()
my_dog.roll_over()
print("your dog name is "+your_dog.name)
print("your dog is "+str(your_dog.age))
your_dog.sit()
your_dog.roll_over()
"""
"""class Restaurant():
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def describe_res(self):
        print(self.name+" restaurant is popular amongs people .")
        print("its produces different types of cusines")
    def open_restaurant(self):
        print(self.name +" is now open")"""
"""restaurant=Restaurant('tadka',"indian")
restaurant.describe_res()
print(restaurant.type+" is famous among indians")
restaurant.open_restaurant()
"""
"""rest1=Restaurant("tadka","indian")
rest1.describe_res()
print(rest1.type+" cusine is famous among indian")
rest1.open_restaurant()
rest2=Restaurant("t2 dhaba","chinese")
rest2.describe_res()
rest3=Restaurant("mahadev","italy")
rest3.describe_res()
"""
"""class User():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def describe(self):
        print("user name is "+self.fname +self.lname)
    def greet(self):
        print(self.fname + self.lname +" how you doing?")
user1=User("vijay","jha")
user1.describe()
user1.greet()

user2=User("suraj","srivastav")
user2.describe()
user2.greet()

user3=User("harshul","agrawal")
user3.describe()
user3.greet()
"""
# working with class and instances
"""class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def get_description(self):
        long_name=str(self.year) + " " +self.make+ " "+self.year
        return long_name.title()
my_new_car=Car("audi","a4","2016")
print(my_new_car.get_description())"""
# setting a default for an attribute
"""class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0

    def get_description(self):
        long_name=str(self.year) + " " +self.make+ " "+self.year
        return long_name.title()
    def read_odometer(self):
        print("this car has "+str(self.odometer)+ " miles on it")

my_new_car=Car("audi","a4","2016")
print(my_new_car.get_description())
#my_new_car.read_odometer()
"""
# modifying attributes values
# modifying an attributes value directly
"""my_new_car.odometer=23
my_new_car.read_odometer()
"""
# modifying attribute value through a method
"""class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0

    def get_description(self):
        long_name=str(self.year) + " " +self.make+ " "+self.year
        return long_name.title()
    def update_odometer(self,mileage):
        self.odometer=mileage
    def read_odometer(self):
        print("this car has " + str(self.odometer) + " miles on it")

my_new_car=Car("audi","a4","2016")
print(my_new_car.get_description())
my_new_car.update_odometer(45)
my_new_car.read_odometer()"""
# incrementing an attribute value through a method
"""class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0

    def get_description(self):
        long_name=str(self.year) + " " +self.make+ " "+self.year
        return long_name.title()

    def update_odometer(self, mileage):
        self.odometer = mileage

    def read_odometer(self):
        print("this car has " + str(self.odometer) + " miles on it")
    def incremental_odometer(self,miles):
        self.odometer+=miles
my_new_car=Car("subaru","outback","2013")
print(my_new_car.get_description())

my_new_car.update_odometer(29007)
my_new_car.read_odometer()

my_new_car.incremental_odometer(1000)
my_new_car.read_odometer()
"""
"""class Restaurant():
    def __init__(self,name,type):
        self.name=name
        self.type=type
        self.number_served=0
    def describe_res(self):
        print(self.name+" restaurant is popular amongs people .")
        print("its produces different types of cusines")
    def served_customer(self):
        print(self.number_served , " customer served till now")
    def update_served(self,value):
        self.number_served=value
    def increment_served(self,value):
        self.number_served+=value
restuarant=Restaurant("tadka","indian")
restuarant.describe_res()
restuarant.served_customer()
#restuarant.number_served=34
#restuarant.served_customer()
restuarant.update_served(45)
restuarant.served_customer()
restuarant.increment_served(456)
restuarant.served_customer()
"""
class User():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.login_attempt=0
    def describe(self):
        print("user name is "+self.fname +self.lname)
    def greet(self):
        print(self.fname + self.lname +" how you doing?")
    def incremental_login_attempt(self):
        self.login_attempt+=1
    def reset_login_attempt(self):
        self.login_attempt=0
    def read_login_attempt(self):
        print(self.login_attempt, " login attempt has been done")

user1=User("vijay","jha")
user1.describe()
user1.incremental_login_attempt()
user1.incremental_login_attempt()
user1.incremental_login_attempt()
user1.read_login_attempt()
user1.reset_login_attempt()
user1.read_login_attempt()