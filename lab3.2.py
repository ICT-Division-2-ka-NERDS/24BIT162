str=input("Enter a string:")
lst1=[]
lst2=[]
lst3=[]
#lower case
for char in str:
    a=ord(char)
    if 65<=a<=90:
        a=a+32
        lst1.append(chr(a))

    else:
        lst1.append(chr(a))
string2=''.join(lst1)
print( "lower case is :",string2)
#upper case
for char in str:
    a=ord(char)
    if 97<=a<=122:
        a=a-32
        lst2.append(chr(a))

    else:
        lst2.append(chr(a))
string3=''.join(lst2)
print( "upper case is :",string3)
#toggle case
for char in str:
    a=ord(char)
    if 65<=a<=90:
        a=a+32
        lst3.append(chr(a))

    else:
        a=a-32
        lst3.append(chr(a))
string4=''.join(lst3)
print( "lower case is :",string4)

