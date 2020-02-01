class Employee:
    raise_amount=1.04
    pass
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"." +last+ "@gmail.com"
    def fullname(self):
        return "{}{}".format(self.first,self.last)
    def pays(self):
        return self.pay
    def mail(self):
        return self.email
    def apply_raise(self):         # it is an class variable means this is common for all employ
        self.pay=int(self.pay+self.raise_amount)
emp1=Employee('vijay','jha',9000)
emp2=Employee('suraj','shri',8000)
print(emp1.fullname(),emp1.pays(),emp1.email)
"""print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
"""
print(Employee.raise_amount) # acessing this class variables by class itself
print(emp1.raise_amount) #acessing this class variables by instases itself
print(emp2.raise_amount)
