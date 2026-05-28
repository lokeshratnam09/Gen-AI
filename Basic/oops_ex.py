# collection of variables and functions called as class
# "class" is the keyword , used to declare the class
# __init__, used to declare the constructor
# constructor , used to initialize the instance variables
# instance members are available in seperate copies for each object
#inheritance
#getting the data from parent class to child class is called inheritance

# class Test:
#     def __init__(self):
#         self.num1=200
#         self.num2 = 100
        
# obj1 = Test()
# x= obj1.num1
# y=obj1.num2
# res = x+y
# print(res)  


# class Test:
#     def __init__(self):
#         self.num1=200
# obj1 = Test()
# obj1.num1 = 2000

# obj2 = Test()
# x= obj2.num1
# print(x)


# class Test:
#     def __init__(self,param1,param2):
#         self.num1=param1
#         self.num2 = param2
# obj1 = Test(200,100)
# x= obj1.num1
# y=obj1.num2
# res = x+y
# print(res) 



# class Test:

#    def add1(self):
#     num1 = 200
#     num2 = 100
#     res = num1+num2
#     print(res)

#    def add2(self):
#     num1 = 200
#     num2 = 100
#     res = num1+num2
#     return res

#    def add3(self,param1,param2):
#     res = param1+param2
#     print(res)

#    def add4(self,param1,param2):
#     res = param1+param2
#     return res

# obj1 = Test()
# obj1.add1()

# x= obj1.add2()
# print(x)

# obj1.add3(200,100)

# y = obj1.add4(200,100)
# print(y)

# single level inheritance

# class parent:
#     def __init__(self):
#         self.num1 = 200
        
# class child(parent):
#     def __init__(self):
#         super().__init__()
#         self.num2 = 100 

# obj1 = child()
# x = obj1.num1
# y = obj1.num2
# res = x+y
# print(res)     


# Single level inheritance with parameterized constructor

# class parent:
#     def __init__(self,num1):
#         self.num1 = num1
        
# class child(parent):
#     def __init__(self,num1,num2):
#         super().__init__(num1)
#         self.num2 = num2

# obj1 = child(200,100)
# x = obj1.num1
# y = obj1.num2
# res = x+y   
# print(res)            


# multilevel inheritance

# class parent:
#     def test1(self):
#         print(" parent class")

# class child(parent):
#     def test2(self):
#         print(" child class")

# class subchild(child):
#     def test3(self):
#         print(" class")

# obj1 = subchild()
# obj1.test1()    
# obj1.test2()
# obj1.test3()    

# multilevel inheritance with super() method

# class parent:
#     def test1(self):
#         print(" parent class")
# class child(parent):
#     def test2(self):
#         super().test1()
# class subchild(child):
#     def test3(self):
#         super().test2()

# obj1 = subchild()
# obj1.test3()  

# multiple inheritance

# class parent1:
#     def test1(self):
#         print(" parent1 class")
# class parent2:
#     def test2(self):
#         print(" parent2 class")
# class child(parent1,parent2):
#     pass

# obj1 = child()
# obj1.test1()
# obj1.test2()


# hirarchical inheritance

# class parent:
#     def test1(self):
#         print(" parent class")
# class child1(parent):
#     def test2(self):
#         print(" child1 class")
# class child2(parent):
#     def test3(self):
#         print(" child2 class")

# obj1 = child1()
# obj1.test1()    
# obj1.test2()

# obj2 = child2()
# obj2.test1()
# obj2.test3()  

# hybrid (multiple + hirarchical) inheritance

# class parent:
#     def test1(self):
#         print(" parent class")
# class child1(parent):
#     def test2(self):
#         print(" child1 class")
# class child2(parent):
#     def test3(self):
#         print(" child2 class")
# class subchild(child1,child2):
#     def test4(self):
#         print(" subchild class")
# obj1 = subchild()
# obj1.test1()
# obj1.test2()
# obj1.test3()
# obj1.test4()

# method overriding

# class parent:
#     def db_conn(self):
#         print("oracle conn soon ....")
# class child(parent):
#     def db_conn(self):
#         print("mysql conn soon ....")
# obj = child()
# obj.db_conn()  

# obj1 = parent()
# obj1.db_conn()
                                
