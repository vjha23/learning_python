# dictinary --------------------------------------------------------
# dictonary is key value pair and it is in form of {}
d1 = {}
#print(type(d1))

d2 = {"vijay":"burger","rahul":"fish","harshul":"roti","suraj":"sabji","sourabh":{"b":"roti","l":"maggie","d":"chicken"}}
d2["ankit"] = "chowmin" # adding further dic
d2["rohit"] ="bread"

del d2["rohit"]
print(d2)
print(d2["vijay"])
print(d2["rahul"])
print(d2["sourabh"])
print(d2["sourabh"]["b"]) # dictionary under dictinory
print(d2["sourabh"]["d"])

# here copy function
d3 = d2
del d3["rahul"]
print(d2) # here important point is reflected in oringinal file to avoid this we use copy function

d3 = d2.copy()
del d3["vijay"]
print(d2)
print(d3) #so here it doesnit get changed

# other functions

print(d2.get("vijay")) # to access the dic valies
d2.update({"leena":"toffee"}) # for adding dic
print(d2)
print(d2.keys()) # it will show only the key
print(d2.items())