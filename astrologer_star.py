# pattern printing

n=int(input("enter the no of rows"))
choose=int(input("choose 1 or 0"))
boolean= True or False

if boolean==choose:
    for i in range(1,n):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
else:

    for i in range(1,n):
        for j in range(n,i,-1):
            print("*",end=" ")
        print()



