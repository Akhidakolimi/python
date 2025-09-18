# class student:
#        def __init__(self):
#         print("student is a obje")
# s1=student()
# s2=student()
# s3=student()
# s4=student()

                                #without function
# class student:
#     def __init__(self,name,age,branch):
#         self.stdname=name
#         self.age=age
#         self.branch=branch
# s1=student("scott",20,"cse")
# print(f"student name: = {s1.stdname}")
# print(f"student age: = {s1.age}")
# print(f"student branch: = {s1.branch}")
# print()
# s2=student("akhi",21,"csc")
# print(f"student name: = {s2.stdname}")
# print(f"student age: = {s2.age}")
# print(f"student branch: = {s2.branch}")
# print()
# s3=student("pooja",23,"eee")
# print(f"student name: = {s3.stdname}")
# print(f"student age: = {s3.age}")
# print(f"student branch: = {s3.branch}")
# print()
# s4=student("priya",45,"hr")
# print(f"student name: = {s4.stdname}")
# print(f"student age: = {s4.age}")
# print(f"student branch: = {s4.branch}")

# class student:
#     def __init__(self,name,age,branch):
#         self.stdname=name
#         self.age=age
#         self.branch=branch
#     def display(self):
#         print(f"student name is :{self.stdname}")
#         print(f"student age: = {self.age}")
#         print(f"student branch: = {self.branch}")
# s1=student("scott",20,"cse")
# s1.display()
# s2=student("adams",21,"eee")
# s2.display()
# s3=student("zub",20,"csc")
# s3.display()


#write a py program class an employee class and declare 
# states as em name,em no,designation,salary,dep no
# create 5 obje and access the details of 5 empolo obj using func

# class employee:
#     def __int__(self,empname,empno,design,salary,depno):
#         self.empname=empname
#         self.empno=empno
#         self.design=design
#         self.salary=salary
#         self.depno=depno
#     def display(self):
#         print(f"emp name is:{self.empname}")
#         print(f"emp no is:{self.empno}")
#         print(f"designation is:{self.design}")
#         print(f"salary is:{self.salary}")
#         print(f"dep nois:{self.depno}")
# e1=employee("scott",1,"hr",50000,3701)
# e1.display()
# e2=employee("adams",2,"manager",10000,3702)
# e2.display()
# e3=employee("akhi",3,"developer",30000,3703)
# e3.display()
# e4=employee("priya",4,"tester",50000,3704)
# e4.display()
# e5=employee("ram",5,"snalyst",40000,3705)
# e5.display()

###                                                   methods
#  types of methods
# *instance methods
#   -accessor methods
#   -mutator methods
# *class methods
# *static methods


#      #   instance method
# the instance related to object is called instance method

#     #   accessor method
# this method is used to access or read data of the variables.
# this method do not modify the data in the variable.
# this is also called as getter method.

# ex: def get_value(self):
#     def get_result(self):
#     def get_id(self):
#     def get_name(self):

#     ##  mutator method
# this method is used to access or read and modify data of variables.
# this method modify the data in the variables.
# this also called as setter method

# ex: def set_value(self):
#     def set_result(self):
#     def set_id(self):
#     def set_name(self):

# class student:
       
#     def __init__(self):
#         print()
#         print("student obj is created")
#         print()
#         #mutator method or setter method
#     def set_name(self,name):
#         self.name=name
#     def set_age(self,age):
#         self.age=age
#     def set_branch(self,branch):
#         self.branch=branch
    #accessor method or getter method
#     def get_name(self):
#         print(f"student name is{self.name}")
#     def get_age(self):
#         print(f"student age is:{self.age}")
#     def get_branch(self):
#         print(f"student branch is:{self.branch}")
# s1=student()
# s1.set_name("scott")
# s1.set_age(23)
# s1.set_branch("csc")
# s1.get_name()
# s1.get_age()
# s1.get_branch()




#class methodwith parameter
# class mobile:
#     @classmethod 
#     def show_model(cls):
#         print("realm")
# realme=mobile()
# mobile.show_model()

#static method
class mobile:
    @staticmethod 
    def show_model():
        print("realm")
realme=mobile()
mobile.show_model()





        









