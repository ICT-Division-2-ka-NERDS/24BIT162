str1=input("Enter string:")
str2=input("Enter substring:")
print(str1)
if(str2 in str1):
   str3= str1.replace(str2,"")
print(str3)