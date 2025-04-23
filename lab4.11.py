n=int(input("Enter value of angle in degrees:"))
x=n*3.14/180
print(x)
sinx=x
fact=1
for i in range(3,26,2):
    fact=fact*i*(i-1)
    i+=1
    for i in range(1,10):
        a=pow(-1,i)
        b=pow(x,(2*i+1))/fact
        sinx=sinx+(a*b)
        i+=1
print(sinx)
