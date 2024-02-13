arr = [45,56,98,3,67,9,90]
max_element = arr[0]
for i in range(len(arr)):
    if arr[i]>max_element:
     max_element = arr[i]
print ("Largest number is",max_element)    
