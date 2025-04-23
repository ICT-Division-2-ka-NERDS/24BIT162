def convert(string):
    set1=set(string)
    lst1=sorted(list(set1))
    print(lst1)
    for ele in lst1:
        if(ele==" "):
            lst1.remove(" ")
    print(lst1)
str=input("Enetr a string:")
convert(str)