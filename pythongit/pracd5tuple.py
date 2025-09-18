                              ###tuple
# tuple=(10,20,30,40,50)
# print(tuple)
# print(type(tuple))


#tuple packing
# num=10,20,30,40,50,60
# print(num)
# print(type(num))

#tuple unpacking
# a,b,c,d,e,f=num
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# # print(f)
    
# num=(10)
# print(type(num))    

#write a python prog to read 2 intger values as input from user and
#swap the values of the 2 int using arthematic operator using third variable ,without using the variable

# a=int(input("enter the values of first integer"))
# b=int(input("enter the value of second integer"))
#logic 1

# print("a =",a)
# print("b =",b)  
# a,b=b,a
# print(f"after swaping a = {a}")
# print(f"after swaping b  {b}")  

#logic 2
# print("a =",a)
#print("b =",b)  
# a=a+b
# b=a-b
# a=a-b             
# print(f"after swaping a = {a}")
# print(f"after swaping b = {b}") 

#logic 3 
# print("a =",a)
# print("b =",b)  
# temp=a
# a=b
# b=temp
# print(f"after swaping a = {a}")
# print(f"after swaping b = {b}") 

#write a python prog to check weather the user entered int is a prime number or not


## prime numbers
# num=int(input("enter the num"))
# fact=0
# for i in range(1,num+1):
#     if (num%i==0):
#         fact+=1
# res="prime number" if (fact==2) else "not prime"

#write a py pro to read a input value and check weather it is a polyndrom
# num=int(input("enter num"))
# fact=0
# ori=num
# rev,rem=0,0
# while(ori!=0):
#         rem=num%10                           # gives remainder nothing but last digit
#         rev=rev*10+rem
#         ori=ori//10
# if(num==rev):
#     if ori == rev:
#           print("polyndrom")
#     else:
#           print("not a polyndrom")

#     for i in range(1,num+1):
#         if (num%i==0):
#           fact+=1
# res="prime number" if fact==2 else "not a prime number"
# print(f"{num} is{rev}")

#perform using addition with out using addition operator and built in operator
# a=int(input("enter a"))
# b=int(input("enter b"))
# sum=a-(-b)
# print(sum)

#write a python program to print all three digit polyndrom  numbers
# for i in range(1,10):
#     for j in range(0,10):
#         print(f"{i}{j}{i}",end=" , ")
#write a to check wheather year or not
#write a python program to print the next 25 leap years from the user enterd year
year=int(input("enter year"))
if(year%400==0)or(year%4==0)and(year%100!=0):
    print("leap year")
else:
    print("not a leap year")

