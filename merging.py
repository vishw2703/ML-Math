def Merge(dict1, dict2):
    return(dict2.update(dict1))


dict1 = {101: 'a', 102: 'b', 103: 'c'}
dict2 = {104: 'd', 105: 'e', 106: 'f'}
print(Merge(dict1, dict2))
print(dict2)