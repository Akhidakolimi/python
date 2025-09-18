#n=int(input("enter n"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# n=int(input("enter n"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)



# digit_count=0
# while(n!=0):
    
#     n= n//0
#     digit_count +=1
# print(f"digit count is {digit_count}")



#n=int(input("enter the value of n :"))
# even,odd,rem=0,0,0
# while(n!=0):
#     rem=n%10
#     if rem%2==0:
#         even+=1
#     else:
#         odd+=1
#     n=n//10
# print(f"even digit count is{even}")



# n=int(input("enter n"))
# original=n
# rem,rev=0,0
# print(f"user entered number is{n}")
# while(n!=0):
#     rem=n%10                           # gives remainder nothing but last digit
#     rev=rev*10+rem
#     n=n//10
# print(f"reversed number is {rev}")
# if original == rev:
#     print("polyndrom")
# else:
#     print("not a polyndrom")
    
    
#n=int(input("enter n value"))
# for i in range(1,n+1):
#     print(i*i)
# i=0
# while(i<=n):
#     print(i*i)
#     i+=1


# a=int(input("enter the value of a"))
# b=int(input("enter the value of b"))
# print()
# while(True):
#     print("operation menu")
#     print("1.addition")
#     print ("2.subtraction")
#     print("3.multiplication")
#     print("4.division")
#     print()
#     choice=int(input("enter your choice"))
#     print()
#     if(choice==1):
#         print(f"summation of {a} {b} is {a+b}")
#     elif(choice==2):
#         print(f"subtraction of {a} {b} is {a-b}")
#     elif(choice==3):
#         print(f"multiplication of {a} {b} is {a*b}")
#     elif(choice==4):
#         print(f"division of {a} {b} is {a/b}")
#     elif(choice==5):
#         print("thank you for using operation menu")
#         break
        

                                     #membership operator
# num=[10,20,30,40,50]
# print(10 in num)

# print(60 not in num)

# print(60 in num)




guest_list = []
while(True):
    print("   geust menu   ")
    print("1.to view the guest list")
    print ("2.to add a geust")
    print("3.to check the guest is attending the party")
    print("4.remove a guest list")
    print()
    elif(choice==3):
        guest=input("enter the guest name")
        if guest in guest_list:
            print(f"{guest} attending the party")
        else:
            print(f"{guest} is not attending the party") 
        print()  
    elif(choice==4):
        guest=input("enter the guest name")
        print()
        print("remove the guest if not attending the party")
        if guest in guest_list:
            guest_list.remove(guest)
            print(f"{guest} is removed from party")
        print()
    elif(choice==5):
        print("the finalized guest list")
        print()
        print(guest_list)
        break
        
