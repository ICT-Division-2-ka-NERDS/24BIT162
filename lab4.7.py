#npr n!/(n-r)!=n*n-1*..n-r
product=1
n=int(input("Enter n:"))
r=int(input("Enter r:"))
i=1
while i<=r:
    product=product*(n-i+1)
    i+=1
print(product)
#ncr=n!/r!(n-r)!  
sum=1
for i in range(1,r+1):
    sum=sum*(n-r+i)/i
print("nCr =",sum)
    