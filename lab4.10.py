n=int(input("Enter number:"))
a=0
b=1
temp=b
i=1
while i<=n:
    print(a,end=" ")
    a=b
    b=temp
    temp=a+b
    i+=1

