class Restaurant():
    def __init__(self,name,type):
        self.name=name
        self.type=type
        self.number_served=0
    def describe_res(self):
        print(self.name+" restaurant is popular amongs people .")
        print("its produces different types of cusines")
    def customer(self):
        print("no of customer today arrived " +str(self.number_served))
    def set_number_served(self,served):
        self.number_served=served
    def increment_no_served(self,served):
        self.number_served+=served

rest1=Restaurant('tadka','south')
rest1.describe_res()
rest1.customer()
rest1.set_number_served(23)
rest1.customer()
rest1.increment_no_served(34)
rest1.customer()