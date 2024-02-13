list=[45,73,105,7,54,80]
res=[]
for i in list:
    sum=0
    for j in str(i):
        sum+=int(j)
    res.append(sum)
print("sum of digits:"+str(res))        
