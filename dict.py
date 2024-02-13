def dict(lst):
    result_dict={}
    for item in lst:
        data_type=type(item)
        if data_type in result_dict:
            result_dict[data_type].append(item)
        else:
            result_dict[data_type]=[item]
    return result_dict
input=[34,"word",4.5,"code",89,9.0] 
result_dict=dict(input)
print(result_dict)       

