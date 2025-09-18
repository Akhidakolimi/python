                               ####set
# set={10,20,30,30,40,100,30}
# print(set)
### string is immutable(can't be changed)
##int is immutable

#list is *ordered                                dict is *unordered
#        *changable                                      *indexed
#        *duplicate                                      *duplicate
                                                    #     *changable
 
# tuple is muttable                                  set is 
#         *ordered                                 *unorderd
#         *changeable                              *changable
#        * duplicate                               *duplicate are not allowed
                                                  #  *indexed 
                                                  
# size=int(input("enter the size")) 
# num=[]
# for i in range(size):
#     val=int(input(f"enter the element at{i} index"))
#     num.append(val)
# print("user entered list :")
# print(num)     

#write a py pro to read size of list as input from user and read the list element as alphabetic character
#and print the user entered list and the sorted version of user entered list




#number/character                  space/strip
# isalnum()                           istrip()
# isalpha()                           rstrip()
# isdigit()                            strip()
# isnumeric()                           isspace()
# isdecimal()                          center()
           

size=int(input("enter the size")) 
alpha=[]
for i in range(size):
    val=(input(f"enter the element at{i} index"))
    alpha.append(val)
print("user entered list :")
print(alpha)     


                                         
                                                  
                                                  
                                                  
