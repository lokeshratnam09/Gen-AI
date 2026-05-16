#Function - Business Logic called as Function.
# Reuse the Business Logic.
# "def" is the keyword , used to define the Function.
# "pass" is the keyword , representing empty function

# # def function_one():
# #     print("Welcome To Function !!")

# # function_one()

# Example -2 (no para - no return type)
# def addition():
#     num1=100
#     num2=200
#     sum=num1+num2
#     print(sum)

# addition() 

# Example -3 (no para - with return type)
# def addition():
#     num1=100
#     num2=200
#     res=num1+num2
#     return res
# x= addition()
# print(x)

# Example -4 (with para - no return type)
# def addition(num1,num2):
#     res=num1+num2
#     print(res)
# addition(200,300)  

#Example - 5(with para - with return type)
# def addition(num1,num2):
#     sum = num1+num2
#     return sum
# x= addition(200,200)
# print(x)

# def multiply():
#     mul = 2*3
#     print(mul)
# multiply() 

# Keyword Arguments
# def test_func(name,age):
#     print(name,age)
# test_func("lokesh",34)  

# Default Arguments
# def test_func(name="Lokesh"):
#     print(name)
# test_func()

# Variable Length Arguments
# def test_func(*num):
#     print(num,sum(num),type(num),list(num))
# test_func(10,20,30,40,50)   

#keyword variable arguments
# def test_func(**data):
#     print(data,type(data))
# test_func(name="Lokesh",age="35")
 
#param1 & param2 - positional parameters
#param3 - variable length parameter
#param4 - keyword variable arguments

# def test_func(param1,param2,*param3,**param4):
#     print(param1,param2,param3,param4)
# test_func(10,20,30,40,name="samba",age="35")    

  

# def test_func(num1,num2):
#     print(num1+num2,num1-num2,num1*num2,num1/num2)
# x=test_func(200,100)
# print(x)  

#global variable
# x= 100
# def test_func():
#local variable
#     x=200
#     print(x) # accessing local variable
# test_func()  
# print(x)

#Nested Function
# def outter_func():
#     def inner_func():
#         print("Hello")
#     inner_func()
# outter_func()    


# def test():
#     print("Hello")
# x= test()
# print(x)

# Closure Function
# def outer(num1):
#     def inner(num2):
#         return num1+num2
#     return inner

# x= outer(200)
# res = x(100)  
# print(res)


# square = lambda num: num*num
# print(square(10))

# addition =lambda num1,num2: num1+num2
# print(addition(100,200))

# students = [("lokesh",35),("ratnam",32),("arijit",49)]
# students.sort(key=lambda x:x[1])
# print(students)

# LEGB Rule L - Local , E - Enclosing , G - Global , B - Built-in
# x= "global"
# def outer():
#     x= "enclosing"
#     def inner():
#         x="local"
#         print(x)
#     inner()
# outer()        

# Decorator Example
# def decorator(func):
#     def wrapper():
#         print("Security 1")
#         func()
#         print("Security 2")
#     return wrapper

# @decorator
# def hello():
#     print("MLA")
# hello() 

# map()
# manipulate all elements in list
# nums = [1,2,3,4,5]       #[100,200,300,400,500] 
# res = list(map(lambda x:x*100,nums))
# print(res)

# filter()
# apply conditions on list elements
# nums=[1,2,3,4,5,6]
# res = list(filter(lambda x:x%2==0,nums))
# print(res)

# reduce()
# reduce() function , used to find the sum of list elements
# from functools import reduce
# nums=[1,2,3,4,5]
# res = reduce(lambda num1,num2:num1+num2,nums)
# print(res)

# First Class Functions
# store "functions" in "variables"
# pass as "argument"
# return from "functions"
# def test_func():
#     print("Hello")
# x= test_func
# x()

# def func1():
#     print("Hello")
# def func2(func):
#     func()
# func2(func1)        
