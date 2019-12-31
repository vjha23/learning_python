# operation of list data type
# note list is written in []
grocery = ["harpic","vim bar", "deodrant","bhindi","lolypop",56]
print(grocery)
print(grocery[0]) # for accessing the patrticular list element
print(grocery[3])

number = [2,45,6,34]
#print(number[3])
#number.sort() # it will sort the number
#print(number)
#number.reverse() # it will reverse the number the number
#print(number)

# slicing in list
print(number[0:4])
print(number[:])           #         0-default and last vslue default [:]
print(number[1:4])
print(number[::2])

number.append(7) # for adding number at end
print(number)

number.insert(1,65)
 # in this we can add anywhwere by provinding index no
number.remove(6) # it remove the item
number.pop() # it remove the last element only
print(number)


# now tuples examples
# mutable -- can changed -- [list]
#immutable -- cannot changed  [tuple]

tp = (1, 2, 3)
print(tp)
