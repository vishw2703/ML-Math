# dict = {'vishw':{'sem':4,'age':19,'cpi':7.5},'shrey':{'sem':4,'age':20,'cpi':8.0},'zinal':{'sem':4,'age':18,'cpi':8.5}}

# print("Names:",list(dict.keys()))
# # value_list = list(dict.values())
# # print(value_list)
# print("Values:",list(dict.values()))

# max = 0 
# for i in dict.values():
#      if(i['cpi']>max):
#         max=i['cpi']

# print(max)


# def fib(limit):
     
#     # Initialize first two Fibonacci Numbers
#     a, b = 0, 1
 
#     # One by one yield next Fibonacci Number
#     while a < limit:
#         yield a
#         a, b = b, a + b
 
# # Create a generator object
# x = fib(5)


# for i in x:
#         print(i)

#Printing Keys
# thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964}
# for x in thisdict:
#         print(x)
# #Printing values
# for x in thisdict:
#         print(thisdict[x])
# student_names = ['Alice', 'Bob', 'Charlie', 'David']

# greeting_map = map(lambda name: "Hello, " + name, student_names)
# greetings = list(greeting_map)

# print(greetings)


# def divide(x, y):
#     try:
# # Floor Division : Gives only Fractional Part as Answer
#         result = x // y
#     except ZeroDivisionError:
#         print("Sorry ! You are dividing by zero ")
#     else:
#         print("Yeah ! Your answer is :", result)
#     finally:
# # this block is always executed
# # regardless of exception generation.
#         print('This is always executed')
# # Look at parameters and note the working of Program
# divide(3, 2)
# divide(3, 0)

#program to remove all white spaces

# import re

# address = re.compile(r"^([\w\d\-\.]+)@([\w\d\-\.]+).(com|in|org)$")
# mail = ['vishw2734@gmail.com', 'shrey.lund@gmail.org', 'hellomf@vishw.shrey']

# for x in mail:
#     match = address.search(x)
#     if match:
#         print("correct mail address")
#     else:
#         print("incorrect mail address")



# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         print("your are in parent class")
#     def printname(self):    
#         print(self.fname, self.lname)
# class Student(Person):
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         print("Hi",self.fname)
# x = Student("John", "Doe")
# x.printname()
# y = Person("Johny", "Drew")
# y.printname()


# def fibonacci(n):
#     # Create an empty list to store the Fibonacci sequence
#     fib = []
    
#     # Initialize the first two values of the sequence
#     a, b = 0, 1
    
#     # Loop through n numbers and generate the Fibonacci sequence
#     for i in range(n):
#         # Add the current value to the list
#         fib.append(a)
        
#         # Compute the next value in the sequence
#         a, b = b, a + b
    
#     # Return the list of Fibonacci numbers
#     return fib

# # Test the function with n = 10
# print(fibonacci(10))

# import re
# address = re.compile(r"^([\w\d\-\.]+)@([\w\d\-\.]+)\.([a-zA-Z]{2,5})$")
# #r"^([\w\d\-\.]+)@([\w\d\-\.]+)\.(com|in|org)"
# mail =  ['123last@example.co.in', 'no.-reply@example.com',]
# for x in mail:
#     match = address.search(x)
#     if match:
#         print ('Match')
#     else:
#         print ('No match')

