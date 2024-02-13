string="pineapple"
freq={}
for i in string:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1
res= max(freq, key=freq.get)
print("most repeating letter in",string,"is",res)            