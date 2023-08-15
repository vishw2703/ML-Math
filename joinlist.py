spam = ['apples', 'bananas', 'oranges', 'tofu', 'cats']

def joinlist(list):
    joined = ''
    if len(list) == 0:
        return ''
    
    elif len(list) == 1:
        return list[0]
    
    else:
        while len(list) >= 2:
            joined += list.pop(0) + ', '

        joined += 'and '
        joined += list[0]
        return joined
    

print(spam)
print(joinlist(spam))

