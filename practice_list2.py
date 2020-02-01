#note sort is used for permanent change and sorted is used for tempory
places=["kathmandu","manali","jaipur","delhi","banglore"]
#change=sorted(places)
#print(change)
print(places) # original list
change=sorted(places) #sorted-tempory
print(change)
change.reverse() # calling reverse in sorted
print(change)
print(places) # we can see that no change
places.reverse() # reversing original list
print(places)
places.reverse() # using again reverse make into in its original list
print(places)
places.sort() # now it will sort into permanent
print(places)
places.reverse() # now reversing the sort list
print(places)
print("done learning listt")
