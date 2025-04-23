length=int(input("Enter length of rectangle:"))
breadth=int(input("Enter breadth of rectangle:"))
area=length*breadth
perimeter=2*(length+breadth)
if(area>perimeter):
    print("Area is greater then perimeter")
else:
    print("Area is smaller then perimeter")