def create_list(list1,list2):
    list3=[]
    for ele in list1:
        if ele in list2:
            list3.append(ele)
    print(list3)
lst1=[1,2,3,4,5,6]
lst2=[4,5,6,7,8,9]
create_list(lst1,lst2)