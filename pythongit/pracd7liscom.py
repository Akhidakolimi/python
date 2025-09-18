# num=[]
# for i in range(1,11):
#     num.append(i)
# print(num)

##list comprehension
# num=[val for val in range(1,11)]
# print(num)


#write a py program a list of even number from 1 to n using list comprehension
# n=int(input("enter:"))
# even_num=[val for val in range(1,n+1) if val%2==0]
# print(even_num)

#filter syntax()
#filter(function_name,iterable)

#reduce function syntax
# from func import reduce
#reduce(function_name,sequence)

# map function()
# syntax:map(function_name,iterable)


# anonymous function or lambda
 
#  a funstion wuthout a name is called as anonymous function.
#  it is also known as lambda function
 
#  anonymus function are not defined using def keuword rather they are defined using lambda keyword.
#  syntax:
#      lamda argument_list: expression

# ex: lambda x:print(x)
# lambda x,y:x+y

  #where:lambda is a keyword

# write a pythion fun to print square values of n using normal method and lambda funtion

# def square(n):
#     for i in range(1,n+1):
#         print(i*i)
# square(10)
#answers:

# def square(n):
#     print(n*n)
# square(10)

# #lambda function

# x=lambda n:print(n*n)
# x(10)


#write a lambda function to add 10 to a number

# add=lambda n:n+10
# add(5) # here we are just writing the retuning statement for printing it we need to print it
# print(add(5))#it will print now
# #write a py pro to check westher the user entered int is even using lambda function

# even=lambda n:n%2==0 
# print(even(24))
# print(even(25))

# #without lambda

# def even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# print(even(25))

#write a py pro to sqr the number in the list using the lambda functions

# num=[1,2,3,4,5,6,7,8,9,10]
# sqr=lambda :[val*val for val in num]
# print(sqr())

# num=[1,2,3,4,5,6,7,8,9,10]          num={1,2,3,4,5,6,7,8,9,10}     
# res=[]                               res=[i+i for i in num]
# for i in num:                        print(res)
#     val=i*i
#     res.append(val)
# print(res)

# num=[1,2,3,4,5,6,7,8,9,10]
# def double(n):
#     return n+n
# res=list(map(double,num))
# print(res)


#write a python pro to read list as
#input from user and return length of each word for the list
# size=int(input("enter the size of list"))
# wordlist=[]
# for i in range(size):
#   val=input("enter the  word:")
#   wordlist.append(val)
# print("user entered wordlist is :",wordlist)
# len=list(map(lambda w:len(w),wordlist))
# print("length of the word in the list:",len)




#to declare small fun in one way without using def ==== lambda()
#to avoid looping and applies a fun to every element in a sequence==== map()




#write a python prog to read three int values as input in same line and print the sum of it
# num=[]
# for i in range(4+1):
#    print(int(input("enter the num ")))
  
#    num.append(i)
   
# print(num)
  
# num=list(map(int,input("enter the number: ").split(",")))
# print(num)
# print(sum(num))

#write a py pro to read a list of elements as 
# input from user and print the square values of the list elements without loop
#looping way

# size=int(input("enter the size of list"))
# list=[]
# new=[]
# for i in range(size):
#   val=int(input("enter the values :"))
#   list.append(val)
# print(list)
# for i in list:
#   i=i*i
#   new.append(i)
# print(new)

# #using list compre

# num=list(map(int, input("enter the number :").split(",")))
# sqr=[x*x for x in num ]
# print(sqr)

# #using map()
# #another way
# sqr=(list(map(lambda x:x*x, num)))
# print(sqr)


# #write a python prog to read a list of numbers and 
# # print the list of even number and odd number with out using loops and conditional statements


# num=list(map(int, input("enter the number :").split()))
# even=list(map(lambda x:x%2==0,num))  ## it only gives true or false for the operator in map
# odd=list(map(lambda x:x%2!=0,num))
# print("user enter:",num)
# print(even)
# print(odd)

# num=list(map(int, input("enter the number :").split()))
# even=list(filter(lambda x:x%2==0,num))
# odd=list(filter(lambda x:x%2!=0,num))
# print("user enter:",num)
# print(even)
# print(odd)

# num=list(map(int, input("enter the sales for a week :").split(",")))
# print(max(num))
# print(sum(num))
#size=int(input("enter the size of list"))
marks=tuple(map(int, input("enter the 3 subj marks:").split(",")))
avg=(sum(marks)/3)
res=tuple(map(lambda i:i >=35,marks))
res="failed" if (False in res ) else "passed"
print(f"avg :{avg}")
print(res)

