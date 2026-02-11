
# just learn about indented

# for i in range(3):
#  print(i)   # must be indented
#  if True:
#   print("I have no Indentation ")
# print("I have tab Indentation ")

# Taking input in Python

# name = input("What is your name  ")
# print("Hello,", name, "! Welcome")

#Printing variables

# s = "Amit"
# print(s)

# s = "Anjali"
# age = 21
# city = "New York"
# print(s, age, city)

#Take Multiple Input in Python by using split() function

# x, y = input("Enter two values: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)
 
# x, y, z = input("Enter three values: ").split()
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)

#Change the Type of Input in Python as sting and Print Names in Python

"""

color = input("What color is rose?: ")
print(color)
#Print Numbers in Python
color = int(input("No. of roses?: "))
print(color)
#Print Float or Decimal Number in Python
price = float(input("Price of each rose?: "))
print(price)

#Find DataType of Input in Python

a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks") #A tuple is like a list, but cannot be changed.
e = ["Geeks", "for", "Geeks"] #A list is used to store many items in one variable.
f = {"Geeks": 1, "for":2, "Geeks":3}  #A dictionary (dict) stores data in key : value form.


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))  
"""
"""
#Multiple Assignments

x, y, z = 1, 2.5, "Python"
print(x, y, z)

a = b = c = 100
print(a, b, c)

#Type Casting a Variable

s = "10"  
n = int(s)

cnt = 5
f = float(cnt) 

age = 25
s2 = str(age)  

print(n)  #integer
print(f)  #float
print(s2) #string

#Type of Variable

n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))

"""
#Concept of Object Reference

"""
x = 5
When x = 5 is executed, Python creates an object to represent the value 5 and makes x reference this object.
y = x
This statement creates y and references the same object as x, not x itself. This is called a Shared Reference, where multiple variables reference the same object.
x = 'Geeks'
Python creates a new object for the value "Geeks" and makes x reference this new object.
shared reference example.
The variable y remains unchanged, still referencing the original object 5. Now, If we assign a new value to y:
y = "Computer"
Python creates yet another object for "Computer" and updates y to reference it.
The original object 5 no longer has any references and becomes eligible for garbage collection.
Python variables hold references to objects, not the actual objects themselves.
Reassigning a variable does not affect other variables referencing the same object unless explicitly updated.

"""
#Deleting a Variable

# x = 10
# print(x)
# del x
# print(x)  #value at x is not available thats why ts gives error
"""

# 1. Swapping Two Variables: 

a, b = 5, 10
a, b = b, a
print(a, b)

# 2. Counting Characters in a String

name="AmitTiwari"
lenght= len(name)
print("Total word are present in given string", lenght)
"""

#Python Keywords

"""
(a). Getting List of all Python keywords:
We can also get all the keyword names using the below code.

import keyword
print("The list of keywords are : ")
print(keyword.kwlist)

Keywords as Variable Names
If we attempt to use a keyword as a variable, Python will raise a SyntaxError. Let's look at an example:

for = 10 
print(for)



Category:	Keywords
Value Keywords: True, False, None
Operator Keywords :	and, or, not, is, in
Control Flow Keywords  : if, else, elif, for, while, break, continue, pass, try, except, finally, raise, assert
Function and Class:	def, return, lambda, yield, class
Context Management:	with, as
Import and Module:	import, from
Scope and Namespace:	global, nonlocal
Async Programming:	async, await

"""
#The ** operator is used for exponentiation in Python. 5 ** 2 means 5 raised to the power of 2.
# num= 5**2
# print(num)

#Which function will you use to find the absolute value of a number in Python?
#Ans: abs()

#How to find the base-2 logarithm of 16 in Python?
#Ans: both math.log2(16) and math.log(16, 2) calculate the base-2 logarithm of 16.

#In Python, any non-zero integer is considered "truthy," so 1 evaluates to True when converted to a boolean.

#How does Python evaluate the expression "bool(0) and bool(1)"?
#Ans: bool(0) is False and bool(1) is True, but the and operator requires both operands to be True to return True.

# all()
#ans: The all() function returns True only if all elements in the iterable are True. Since there is a False in the list, the result is False.


# d = [
#     {"userId": 1, "name": "rahul", "completed": False},
#     {"userId": 1, "name": "rohit", "completed": False},
#     {"userId": 1, "name": "ram", "completed": False},
#     {"userId": 1, "name": "ravan", "completed": True}
# ]

# print("With Python 3.8 Walrus Operator:")
# for E in d:
#     if name := E.get("name"):
#         print(name)

# print("Without Walrus operator:")
# for entry in d:
#     name = entry.get("name")
#     if name:
#         print(name)

# number = input("enter number of switch case")

# match number:
#     case 1:
#         print("One")
#     case 2 | 3:
#         print("Two or Three")
#     case _:
#         print("Other number")

    # loop
"""

    
n = 4
for i in range(0, n):
    print(i)

li = ["geeks", "for", "geeks"]
for x in li:
    print(x)
    
tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)
    
s = "abc"
for x in s:
    print(x)
    
d = dict({'x':123, 'y':354})
for x in d:
    print("%s  %d" % (x, d[x]))
    
set1 = {10, 30, 20}
for x in set1:
    print(x)

li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])    

cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")    

    
"""
# Infinite While Loop
# while (True):
#     print("Hello Geek")

#Nested loop

# from __future__ import print_function
# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=' ')
#     print()

# Loop Control Statements
# for letter in 'geeksforgeeks':
#     if letter == 'e' or letter == 's':
#         continue
#     print('Current Letter :', letter)

# Break Statement
# for letter in 'geeksforgeeks':
#     if letter == 'e' or letter == 's':
#         break

# print('Current Letter :', letter)

#Pass Statement: We use pass statement in Python to write empty loops. Pass is also used for empty control statements, functions and classes.
# for letter in 'geeksforgeeks':
#     pass
# print('Last Letter :', letter)
"""
# Using Else with Loops in Python

for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("kyu bhai loop ke baad aa hi n ya mai jab break nhi hia to")

#not execute else block beacause break aa gaya

for i in range(1, 4):
    print(i)
    break
else: # Not executed as there is a break
    print("No Break")

# Python 3.x program to check if an array consists 
# of even number
def contains_even_number(l):
    for ele in l:
        if ele % 2 == 0:
            print ("list contains an even number")
            break

    # This else executes only if break is NEVER
    # reached and loop terminated after all iterations.
    else:     
        print ("list does not contain an even number")

# Driver code
print ("For List 1:")
contains_even_number([1, 9, 8])
print (" \nFor List 2:")
contains_even_number([1, 3, 5])
"""
# count = 0
# while (count < 1):    
#     count = count+1
#     print(count)
#     break
# else:
#     print("No Break")

# items = input("Enter shopping items separated by commas: ").split(',')

# for item in items:
#     print("Buy:", item.strip()) #strip() removes extra spaces (whitespace) from BOTH ends of a string

# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     print("Square of", i,"is", i**2)

# seconds = int(input("Enter countdown time in seconds: "))

# while seconds > 0:
#     print("Time left:", seconds)
#     seconds -= 1

# Sum util user enter 0 to stop

# total = 0
# num = int(input("Enter number (0 to stop): "))
# while num != 0:
#     total += num
#     num = int(input("Enter number (0 to stop): "))
# print("Total sum:", total)

#Print a multiplication table

# n = 3

# for i in range(1, n + 1):
#     for j in range(1, 11):
#         print(i * j, end=' ')
#     print()

#: Print Identity Matrix Pattern
# n = 4

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()  # move to the next row

#Control Flow Statements in Loops

#break
# items = ["apple", "banana", "cherry", "stop", "mango"]

# for item in items:
#     if item == "stop":
#         break
#     print("Item:", item)

#infinite
# while True:
#     num = int(input("Enter a number: "))
#     if num % 2 == 0:
#         print("First even number found:", num)
#         break

#2. continue
# items = ["milk", "bread", "out of stock", "eggs"]

# for item in items:
#     if item == "out of stock":
#         continue
#     print("Buy:", item)

# n = 10

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         continue
#     print("Odd number:", i)

#3.pass: statement does nothing. It’s a placeholder when the syntax requires a statement but no action is needed.
tasks = ["email", "meeting", "call"]

for task in tasks:
    if task == "call":
        pass  # Logic to be added later
    print("Do:", task)

#empty loop pass

for i in range(5):
    pass  # Placeholder for future logic



