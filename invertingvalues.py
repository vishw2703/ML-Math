ini_dict = {101 : "akshat", 201 : "ball"}
print("initial dictionary : ", str(ini_dict))

inv_dict= {v:k for k, v in ini_dict.items()}

print("inverse mapped dictionary : ", str(inv_dict))