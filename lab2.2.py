a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
c=int(input("Enter third value:"))
if(a>b & a>c):
    if(b>c):
        print("Largest value is:",a)
        print("Smallest value is:",c)
    elif(c>b):
        print("Largest value is:",a)
        print("Smallest value is:",b)
elif(b>c & b>a):
     if(c>a):
        print("Largest value is:",b)
        print("Smallest value is:",a)
     elif(a>c):
        print("Largest value is:",b)
        print("Smallest value is:",c)
else:
     if(a>b):
        print("Largest value is:",c)
        print("Smallest value is:",b)
     elif(b>a):
        print("Largest value is:",c)
        print("Smallest value is:",a)
     