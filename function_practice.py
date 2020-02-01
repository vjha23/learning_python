""""# function using positional arguments
def describe_pet(animal_type,pet_name):
   # display infomation about pet   # docstring
    print("\n I have a "+animal_type+".")
    print("My "+animal_type+" name is "+pet_name.title())
describe_pet('dog','littu')
"""
# function using keywords arguments
"""def describe_pet(animal_type,pet_name):
    print("\n I have a "+animal_type+".")
    print("My "+animal_type+" name is "+pet_name.title())
describe_pet(animal_type='dog',pet_name='littu')
"""
"""def make_tshirt(size,msz):
    print("hey the my size is ",size)
    print(msz)
make_tshirt(23,"i am cool")
make_tshirt(size=34,msz="i am smart")
"""
# using defualt argument
'''def make_tshirt(size='large'or'medium',msz='i love python'):
    print("hey the my size is ",size)
    print(msz)
make_tshirt('medium')
'''
# returning dictionary
'''def build_person(first_name,last_name,age=''):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']= age
    return person
musician=build_person('sonu','nigam')
print(musician)
'''
#using functions with list
'''def show_magicians(names):
    for name in names:
        print("magician list "+name)
show_magicians(['suraj','vijay','harshul'])
'''
# modifying a list in a function
'''
while unprint:
    current=unprint.pop()
    print("processing.."+current)
    complete.append(current)
print("the following model have been printed ")
for completes in complete:
    print(completes)
'''
'''unprinted_design=['iphone case','robot pendant','dodocahedon']
completed_design=[]
def print_model(undesign,complete):
    while undesign:
        current=undesign.pop()
        print("printing models "+ current)
        complete.append(current)
def show(complete):
    for completes in complete:
        print(completes)
print_model(unprinted_design,completed_design)
show(completed_design)
'''


