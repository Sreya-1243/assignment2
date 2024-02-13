list=['banana','cherry','apricot','coconut','kiwi','avocado','apple']
check='a'
print("the original list:",str(list))
res=[]
for i in list:
    if(i.find(check)==0 or i.find(check.lower())==0):
        res.append(i)
    print("the list of matching first letter:",str(res))    