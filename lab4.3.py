str=input("Enter a string:")
count_alpha=0
count_digit=0
for ele in str:
    if ele.isalpha():
        count_alpha+=1
    elif ele.isdigit():
        count_digit+=1

print("number of digits in the string are:",count_digit)
print("number of alphabets in the string are:",count_alpha)