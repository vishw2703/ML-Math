def Sum(my_dict):
    list=[]
    for i in my_dict:
        list.append(my_dict[i])

    final = sum(list)
    return final

  
my_dict = {'a': 101, 'b':102, 'c': 103}
print(Sum(my_dict))