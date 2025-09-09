  

     
         
                                           #program3
         
  ##two digits
# num=int(input("enter a num"))
# if((num>=10 and num<=99) or (num>=-99 and num<=-10)):
#     print("digit")
# else:
#     print("not a digit")
    
                                        ##program4
       
    ##three num
# num=int(input("enter a num"))
   ###positive                     ##negative
# if((num>=100 and num<=999) or (num>=-999 and num<=-100)):
#     print("digit")
# else:
#     print("not a digit")
    
                                          ##program 5
      
    ##four num
# num=int(input("enter a num"))
     ##positive                   #negative
# if((num>=1000 and num<=9999) or (num>=-9999 and num<=-1000)):
#      print("digit")
# else:
#      print("not a digit")
     
                                            #program6
      
# num1=int(input("enter any first integer :"))
# num2=int(input("enter any second integer"))
# if (num1>num2):
#     print(f"{num1} is a largest number")
# else:
#     print(f"{num2} is largest number")
    
   # or 

#
# res=num1 if(num1>num2) else num2
# print(f"{res} is largest number")    

                                      ##program 7
          
# num1=int(input("enter any first integer :"))
# num2=int(input("enter any second integer"))
# if (num1<num2):
#     print(f"{num1} is a smallest number")
# else:
#     print(f"{num2} is smallest number")
    
#    # or 

# # ternary operator
# res=num1 if(num1<num2) else num2
# print(f"{res} is smallest number")    


                                       ##problrm8
        
# num1=int(input("enter any first integer :"))
# num2=int(input("enter any second integer"))
# num3=int(input("enter any third number"))
# if (num1>num2 and num1>num3):
#     print(f"{num1} is a largest number")
# elif (num2>num1 and num2>num3):
#      print(f"{num2} is largest number")
# else:
#     print(f"{num3} is a largest number")

           #or
# largest=num1 if(num1>num2 and num1>num3) else num2
# res=num3 if(num3>num1 and num3>num2) else largest
# print(f"{res} is largest number")    


                                   ##smallest number
                                      ##program 9
      
# num1=int(input("enter any first integer :"))
# num2=int(input("enter any second integer"))
# num3=int(input("enter any third number"))
# if (num1<num2 and num1<num3):
#    print(f"{num1} is a smallest number")
# elif (num2<num1 and num2<num3):
#      print(f"{num2} is smallest number")
# else:
#    print(f"{num3} is a smallest number")

           #or
# largest=num1 if(num1<num2 and num1<num3) else num2
# res=num3 if(num3<num1 and num3<num2) else largest
# print(f"{res} is smallerest number") 

                                     ##program10 
       
#num1=int(input("enter any first integer :"))
# num2=int(input("enter any second integer"))
# num3=int(input("enter any third number"))
# if (num1>num2 and num1<num3):
#     print(f"{num1} is middle")
# elif(num2>num1 and num2<num3):
#     print(f"{num2} is middele ")
# else:
#     print(num3)
# middle =num1 if (num1>num2 and num1<num3) else num2
# res=num3 if(num3>num1 and num3<num2) else middle
# print(f"{res} is middle number")

                                ##program 11
       
#month=int(input("enter any month number"))
# if (month>=1 and month<=12):
#       print("valid")
# else:
#       print("invalid")
      
      #or
#res="valid" if(month>=1 and month<=12) else "invalid"
#print(res)

                                    ###program12
# m=int(input("enter month number"))
# if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
#       print("31 days")
# elif(m==2):
#       print("28 or 29 days")
# elif(m==4 or m==6 or m==9 or m==11):
#       print("30 days")
# else:
#       print("invalid month")

                                           ##program13
# age=int(input("enter your age"))
# if (age>=18):
#       print("valid voter")
# else:
#       print("not valid voter")
                                          ##program14
# num=int(input("enter any number"))
# if (num %2==0):
#       print("even")
# else:
#       print("odd")

                                          ##program14
# num=int(input("enter any number"))
# if (num%3==0 and num%5==0):
#       print("multiple")
# else:
#       print("not a multiple")
                                                ##program15
# num=int(input("enter any number"))
# if (num%3==0 and num%5==0):
#       print("fizzbuzz")
# elif(num%3==0):
#       print("fizz")
# elif(num%5==0):
#       print("buzz")      


