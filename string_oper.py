# string slicing
#for the positive index
mystr="vijay is a good boy"
print(mystr[4]) # at 4th position and it start from 0th position
print(mystr[0:5]) # here 0 is including and 5 is excluding
print(len(mystr)) # length
print (mystr[0:19]) # full length
print (mystr[0:56]) # if the index exceed it will still print all the elements
print (mystr[0:5:2]) # here means skipping of 1 so v j and y v-0,j-2,y-5 simply 1 ka difference
print(mystr[0:]) # it will select all from the 0th index
print(mystr[:5]) # it will select from the nth to start here n=5
print(mystr[:]) # it also means selecting all string
print(mystr[::]) # basically it means 0:length of string:1
print(mystr[::2]) # skiping of character and(0:19:2)

# negative index
print(mystr[-4:]) # so basically it will counts from the end y-1,o-2,b-3,space -4
print(mystr[-4:-1]) # including -4 and excluding -4
print(mystr[::-1]) # it will reverse the string
print(mystr[::-2])

# functions of strings
print(type(mystr))
print(mystr.isalnum())
print (mystr.endswith("boy")) # for searching string at the end gives boolean result
print(mystr.count("a")) # for counting particular alphabet
print(mystr.capitalize()) # it will capitalize the first aplphabet only
print(mystr.find("is")) # it will search at the index position
print(mystr.upper()) # it will convert into the upper case
print(mystr.replace("is","are"))

