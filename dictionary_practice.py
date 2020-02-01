# examples 1
"""person={"first_name":"vijay","last_name":"jha","age":20,"city":"jaipur"}
print(person)
for key,value in person.items(): # acessing the dict key values
    print(key ,value)
"""
# example 2
"""poll={
    "suraj":5,
    "vijay":7,
    "harshul":6,
    "riya":7,
    "mohit":9,
}
for polling,value in poll.items():
    print("favorite no of "+str(polling)+" is "+str(value))
"""
# example 3
"""fav_lang={
    "suraj":"java",
    "vijay":"python",
    "mohit":"c",
    "rahul":".net",
}
for name,lang in fav_lang.items(): # can use title() with variables
    print(name.title()+"'s fav lang is "+ lang.title()+".") """
#looping through all keys in a dictionary
"""fav_lang={
    "suraj":"java",
    "mohit":"python",
    "rahul":".net",
    "vijay":"python",
    "riya":"c"
}
for name in fav_lang.keys(): # for accessing the key values only
    print(name.title())
"""
# example 2
"""fav_lang={
    "suraj":"java",
    "mohit":"python",
    "rahul":".net",
    "vijay":"python",
    "riya":"c"
}
friends=["suraj","vijay"]
for name in fav_lang.keys():
    print(name.title())
    if name in friends:
        print("Hi "+name.title()+" i see your fav lang is "+fav_lang[name]+ "!") # confusing in this line fav_lang[name] here just it will access the key pair value
"""
# looping through the keys in order
"""fav_lang={
    "suraj":"java",
    "mohit":"python",
    "rahul":".net",
    "vijay":"python",
    "riya":"c"
}
for name in sorted(fav_lang.keys()):
    print(name+" thanks for the poll")
"""
#looping through the values in dic
"""fav_lang={
    "suraj":"java",
    "mohit":"python",
    "rahul":".net",
    "vijay":"python",
    "riya":"c"
}
print("the following lang have been mentioned")
for lang in fav_lang.values():
    print(lang.title())
"""
# excerise
"""river={
    "ganga":"india",
    "yamuna":"india",
    "nile":"egypt",
}
for river,country in river.items(): # for acessing all items at once
     print("The "+river+" runs through the "+country)
for rivers in river.keys(): # for accesing the key only
    print(rivers)
for country in river.values():
    print(country)
"""
"""fav_lang={
    "suraj":"java",
    "sheela":"python",
    "rahul":".net",
    "vijay":"python",
    "riya":"c",
    "mohit":"",
    "reena":"",
    "sheena":"",
}
for key,value in fav_lang.items():
    if value=="":
        print("please take the poll "+key)
    else:
        print("thanks for the taking the poll "+key)
"""
# a list of dictionary
"""alien_0={"color":"green","points":5}
alien_1={"color":"yellow","points":10}
alien_2={"color":"red","points":15}

aliens=[alien_0,alien_1,alien_2]    # for accessing the list in dict
for alien in aliens:
    print(alien)
"""
# make an empty list of storing the elements
"""aliens=[]
for alien_no in range(20):
    new_alien={"color":"green","points":5}
    aliens.append(new_alien)
# showing the 5 alien
for alien_no in aliens[:5]:
    print(alien_no)
"""
"""aliens=[]
for alien_no in range(20):
    new_alien={"color":"green","points":5}
    aliens.append(new_alien)
# showing the 5 alien
for alien_no in aliens[:5]:
    print(alien_no)
for alien_no in aliens[0:3]: # using the variable to modifying the values
    if alien_no["color"]=="green":
        alien_no["color"]="yellow"
        alien_no["point"]=10
for alien_no in aliens[0:5]:
    print(alien_no)
"""
# a list in a dictionary
# store information about pizza ordered
"""pizza={
    "crust":"thick",
    "toppings":["mushroom","extra chesse"]
}
# summarize the order
print("you ordred a "+pizza["crust"]+" -crust pizza" +"with the following the toppings")
for topping in pizza["toppings"]:
    print(topping)
"""
"""fav_lang={
    "suraj":["java","python"],
    "mohit":["python","go"],
    "rahul":".net",
    "vijay":["python","c"],
    "riya":"c"
}
for name,lang in fav_lang.items():
    print("\n"+ name.title()+" fav lang are:")
    for langs in lang:
        print(langs)
"""
# a dictionary in dictionary
# use when we have no of users and we want each user diff info
"""users={
    "vijay":{
        "first":"vijay",
        "last":"jha",
        "location":"nepal",
    },
    "suraj":{
        "first":"suraj",
        "last":"srivatav",
        "location":"jaipur",
    },
}
for user,user_name in users.items():
    print("\n username: " + user)
    full_name=user_name["first"]+ " "+ user_name["last"]
    location=user_name["location"]
    print("\t fullname" + full_name)
    print("\tlocation" + location)
"""
# example-------------------------
"""people_dic={
    "vijay":{
        "first":"vijay",
        "last":"jha",
        "location":"nepal",
    },
    "rahul":{
        "first":"rahul",
        "last":"jain",
        "location":"jaipur",
    },
}
people=[people_dic]
for peoples in people:
    for username,user_info in peoples.items():
        print("\n Usernamw: "+username)
        full_name=user_info["first"]+ " " +user_info["last"]
        locations=user_info["location"]
        print("\n "+ full_name)
        print(locations)
"""
# example about creating a dictionary of pets
"""pets_dict={
    "brownie":{
        "animal":"dog",
        "owner":"vijay",
        "color":"black",
    },
    "susie":{
        "animal":"cat",
        "owner":"suraj",
        "color":"white",
    },
    "chetak":{
        "animal":"horse",
        "owner":"harshul",
        "color":"brown",
    },
}
pets=[pets_dict]
for pet in pets:
    for name,info in pet.items():
        print("\n Petname: "+name)
        print("Infomation about pet: ")
        print("\n Animal: "+info["animal"])
        print("\n Owner: "+info["owner"])
        print("\n color: "+info["color"])
"""
# creating a dictinary about fav places
fav_place={
    "vijay":["nepal","manali","jaipur","japan"],
    "suraj":["jaipur","goa"],
    "suarabh":"goa",
}
for name,places in fav_place.items():
    print(name+" fav place is :")
    for place in places:
        print(place)