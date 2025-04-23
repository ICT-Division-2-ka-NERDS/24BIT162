print("Enter all three subject marks:")
lst=[]
lst.append(int(input()))
lst.append(int(input()))
lst.append(int(input()))
print(lst)
total=sum(lst)
average=total/3
i=1
print("Total marks are:",total)
print("Average marks are:",average)
for ele in lst:
    if(0<=ele<=39):
        print(" F grade in subject",i)
    elif(40<=ele<=44):
        print(" P grade in subject",i)
    elif(45<=ele<=49):
        print(" C grade in subject",i)
    elif(50<=ele<=54):
        print(" B grade in subject",i)
    elif(55<=ele<=59):
        print(" B+ grade in subject",i)
    elif(60<=ele<=69):
        print(" A grade in subject",i)
    elif(70<=ele<=79):
        print(" A+ grade in subject",i)
    elif(80<=ele<=100):
        print("O grade in subject",i)

    else:
        print("Invalid marks:")
    i+=1