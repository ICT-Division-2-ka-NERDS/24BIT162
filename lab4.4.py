n=int(input("Enter a number:"))
#prime number:
count=0
for i in range(2,int(n/2)+1):
    if n%i==0:
        count+=1
if count==0:
    print(" Prime number.")
else:
    print("Not a prime number.")
# perfect number:
if n>=0:
    print("Perfect number.")
else:
    print("Not a perfect number.")        
num=str(n)
lst=list(num)
lst1=[]
length=len(lst)
for ele in lst:
    lst1.append(pow(int(ele),length))
sum=sum(lst1)
if sum==n:
    print("Is armstrong number.")
else:
    print("Not an armstrong number:")
true=0
lst2=lst1
lst3=list(reversed(lst1))
for i in lst2:
  if lst2 in lst1:
        true+=1
if true==len(lst2):
    print("Is not a palindrome.")
else:
    print("Is palindrome.")
#automorphic number
square=str(pow(n,2))
lst4=list(square)
m=len(lst4)
if n==int(lst4[m-1]):
    print("automorphic number")
else:
    print("not automorphic number")