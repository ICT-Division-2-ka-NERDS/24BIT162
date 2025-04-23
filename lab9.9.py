def count_alpha_digits(string):
    countalpha=0
    countnum=0
    for ele in string:
        if(ele.isalpha()==True):
            countalpha+=1
        elif(ele.isdigit()==True):
            countnum+=1
    dict={ "Alphabets" : countalpha,
          "Digits" : countnum}
    print(dict)
str=input("Enter a string:")
count_alpha_digits(str)