def Convert(lst):
    res_dct = map(lambda i: (lst[i], lst[i+1]), range(len(lst)-1)[::2])
    return dict(res_dct)
 
 
lst1 = ['a', 1, 'b', 2, 'c', 3]
lst2 = ['d', 2, 'e', 3, 'f', 4]
print(Convert(lst1))
print(Convert(lst2))
