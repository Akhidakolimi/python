# List=[1,2,3,45]
# Tuple=(1,2,3,4,5,6)
# Set={1,2,3,4,5,5}
# print(List,type(List))
# print(Tuple,type(Tuple))
# print(Set,type(Set))


# rg1=range(10)
# print(rg1)
# print(type(rg1)) 

# for i in range(10):
#     print(range)

# for i in range(1,11,3):
#     print(i)

# n=int(input("enter the natural number"))
# print(f"natural number is {n}")
# for i in range(1,n+1):
#     print(i)


# n=int(input("enter the natural number"))
# print(f"natural number is {n}")
# for i in range(n,0,-1):
#     print(i)

# n=int(input("enter the even number from n to "))
# print(f"even number is {n}")
# for i in range(2,n+1,2):
#     print(i)
# for i in range(2,n+1):
#     if i%2==0:
#         print(i)
    
    
# n=int(input("enter the even number from n to 1"))
# print(f"even number from n to 1 is {n}")
# for i in range(n,0,-2):
#     if i%2==0:
#         print(i)
    
# n=int(input("enter the odd number"))
# print(f"odd number is {n}")
# for i in range(1,n+1,2):
#     if i%2!=0:
#         print(i)

# n=int(input("enter the odd number from n to 1"))
# print(f"odd number from n to 1 is {n}")
# for i in range(n+1,0,-1):
#     if i%2!=0:
#         print(i)


# n=int(input("enter any number"))
# for i in range (1,11):
#     print(n,"x" , i,"=", n*i)


# n=int(input("enter any number"))
# for i in range (1,n+1):
#     print(i)
#     for j in range(10,0,-1):
#         print(i,"x" , j,"=", i*i)


# unit=int(input("enter the units"))
# if unit==100 :
#     total=unit*5 
# print("your total bill per unit" ,total)
# elif unit>=100:
#     total=unit*7
# print(total)
# elif unit>=200:
#     total=unit*10
# print(total)

# bmi=int(input("enter your weight"))
# if bmi< 18.5:
#     print("under weight")
# elif 18.5<=bmi<25:
#     print("normal weight")
# elif 25<=bmi<30:
#     print("over weight")
# elif bmi>=30:
#     print("obese")


# salary=int(input("enter your salary"))
# cresco=int(input("enter the credit"))
# if salary >=30000 and cresco >=700:
#     print("eligible")
# else:
#     print("not eligible")



# temp=int(input("enter your temp"))
# if temp<0:
#     print("freezing wether")
# elif temp>0 and temp<=20:
#     print("cold weather")
# elif temp>=21 or temp <=35:
#     print("normal weather")
# elif temp>35:
#     print("hot weather")

# balance=int(input("enter the balance"))
# if balance==0:
#     print(f"{balance}MB recharge required")
# elif balance <=100:
#     print(f"{balance}MB low data warning")
# else:
#     print("sufficient data available")

age=int(input("enter the age"))
if age<5:
    print("free ticket")
elif  5<=age<=12:
    print("half ticket")
elif 13 <=age<=59:
    print("full ticket")
elif age>=60:
    print("senior citizen discount")