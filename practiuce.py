client={
    "suraj":{
        "food":[],
        "excerise":[],
    },
    "suarabh":{
        "food":[],
        "excerise":[],
    },
}
def food():
    feed=input("enter the food name")
    return feed
for name,routine in client.items():
    for action,list in routine.items():
        if action=="food":
            list.append(food())
            for show in list:
                print(show)
        else:
            print("chall bhagg")
