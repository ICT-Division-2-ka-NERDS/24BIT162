lst=[]
for i in range(1,31):
    for j in range(1,31):
       r=int((i*i)+(j*j))
       n=pow(r,0.5)
       if n== int(pow(r,0.5)) and i<j:
           lst.append([i,j,int(n)])
        
print(lst)