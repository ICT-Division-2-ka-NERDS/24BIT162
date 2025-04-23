lst=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
num=int(input("Enter a number between 0 to 19:"))
if(0<num<=19):
    print(num,"->",lst[num])
else:
    print("Not a valid number.")
