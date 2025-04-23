centerx1=int(input("input center x1:"))
centery1=int(input("input center y1:"))
r=int(input("Enter radious:"))
x2=int(input("input x2:"))
y2=int(input("input y2:"))
a=pow(x2,2)-pow(centerx1,2)
b=pow(y2,2)-pow(centery1,2)
if(a+b==pow(r,2)):
    print("This points lies on circle")
elif(a+b>pow(r,2)):
    print("This points lies outside the 0circle")
else:
    print("This points lies inside the circle")