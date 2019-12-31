# create a faulty calculator,calution-45*3=555,56+9=77,56/6=4
# choose what operator they want and and take input as two number

print("enter the opetation you want to perform")
print("enter opertor")
choice=input()
print("enter the two number ")
v1=int(input())
v2=int(input())
if(choice=='+'):
    if (v1==56 and v2==3 and choice== '+'):
        print(77)
    else:
        print("addition is",v1+v2)
elif(choice=='-'):
    print("subtration is ",v1-v2)
elif(choice=='*'):
    if (v1==45 and v2==3 and choice=='*'):
        print("multiplication=555")
    else:
        print("multiplication",v1*v2)
elif(choice=='/'):
    if (v1==56 and v2==6 and choice=='/'):
        print("4")
    else:
        print(v1/v2)
else:
    print("choose correct operator")
