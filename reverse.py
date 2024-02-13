def reverse(my_tuple):
    reversed_items=[]
    for item in my_tuple:
        if isinstance(item,str):
            reversed_items.append(item[::-1])
        elif isinstance(item,(int,float)):
            reversed_items.append(str(item)[::-1])
        else:
            reversed_items.append(item)
    return tuple(reversed_items)
my_tuple=("abc",567,"python","try",87)
reversed_tuple=reverse(my_tuple)
print(reversed_tuple)
            

    