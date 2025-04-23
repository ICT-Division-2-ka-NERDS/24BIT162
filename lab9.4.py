def sum_avg(marks):
    total=sum(marks)
    average=total/len(marks)
    return total, average
marks=[34,56,46,78]
print(sum_avg(marks))