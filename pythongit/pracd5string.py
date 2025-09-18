                                                ####string
                #   string of immutable
                
                
#number/character                  space/strip
# isalnum()                           istrip()
# isalpha()                           rstrip()
# isdigit()                            strip()
# isnumeric()                           isspace()
# isdecimal()                          center()
           
# string=input("enter the string")
# print(string)
# print(f"the upper case of the given string is {string.upper()}")
# print(f"the upper case of the given string is {string.lower()}")
# print(f"the upper case of the given string is {string.swapcase()}")

# write a py pro to read the name of the user and print 
# the length  of the name and check if it is more than 5 char



# string=input("enter the string: ")
# print(len(string))
# res="more than 5 characters" if(len(string)>5) else "less than 5 char"
# print(res)



#write a python program to check if the user enterd name as a character  A are not

# name=input("enter the name: ").swapcase()
# if "A" in name:
#     print(f"the name {name} consist letter A")
# else:
#     print(f"the {name} does not consisit char A")


    
#write a python program how many alphabets ,how many digits ,how many special
# chara,are present in the user entered input


# name=input("enter the name:")
# alpha,digit,specichar=0,0,0
# for ch in name:
#     if ch.isalpha():
#         alpha+=1
#     elif ch.isdigit():
#         digit+=1
#     else:
#         specichar+=1
# print(f"count of alphabet charcther is{alpha}")
# print(f"count of digit is{digit}")
# print(f"count of special charcther is{specichar}")


#write a python prog to check the count of vowels 
# and consonants present in the user entered input


# name=input("enter the name:")
# vowels,consonants=0,0
# for ch in name:
#     if ch.isalpha():
#         if ch in "a,e,i,o,u":
#             vowels+=1
#         else:
#             consonants+=1
# print(f"vowels count is{vowels}")
# print(f"consonants count is {consonants}")
# write a python prog to read your 12 digit 
# adhar number as input from the user and print the 12 digit num 
# where first 8 digits should be  not visible and last 4 digi sholud visible

#    012345678911234567
# str="pythonprogramming"
# print(str[:6])
# print(str[2:6])
# print(str[0::2])
# print(str[1::2])
# print(str[-11:-4])

number=input("enter the number")
print("**** **** ",number[10::])
    
# if (number[-6:-14]):
#     a= number.replace(number,"x") 
#     print(a)
