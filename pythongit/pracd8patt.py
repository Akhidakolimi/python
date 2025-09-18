                                     ###day 8 patterns
# #1.enter the value of n : 5
# #    * * * * * 
# #    * * * * *
# #    * * * * *
# #    * * * * *
# #    * * * * *


# n=int(input("enter the value of n"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()
#output
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# n=int(input("enter the value of n"))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
#output
# * 
# * *
# * * *
# * * * *
# * * * * *
    
# n=int(input("enter the value of n"))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
   
#output
# * * * * * 
# * * * *
# * * *
# * *
# *
# n=int(input("enter the value of n"))
# for i in range(1,n+1):    
#     print(" "*(n-i)+ "*" * i)
    
#output
#     *
#    **
#   ***
#  ****
# *****
        
# n=int(input("enter the value of n"))
# for i in range(n,0,-1):    
#     #print(" "*(n-i)+ "*" * i)
#     print(i * "*"+(n-i)*" ")
    
# #output
# *****
# **** 
# ***  
# **   
# *   
    
# n=int(input("enter the value of n"))
# for i in range(n,0,-1):                #n=5 #i=5 
#     print(" "*(n-i)+ "*" * i)

# n=int(input("enter the value of n"))
# for i in range(n,0,-1):                #n=5 #i=5 
#     print(" "*(n-i)+ i)
# output:
# *****
#  ****
#   ***
#    **
#     *     
#output:
        # *****
        # ****       i=1 0    n=5-5=0   i=2-1=1
        # ***        i=       n=5-4=1   
        # **                   n=5-3=2
        # *                    n=5-2=3
        
#another way
# n=int(input("enter the value of n :"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (j>=i):
#             print("*",end="")
#         else:
#             print("",end="")
    #print()      


# n=int(input("enter the value of n"))
# for i in range(n,0,-1):
#     for j in range(i):
#        print("*",end=" ")
#     print()

#output
# * * * * * 
# * * * *
# * * *
# * *
# *


# n=int(input("enter the value of n"))
# for i in range(n,0,-1):                #n=5 #i=5 
#     print("  "*(n-i)+ "*" * i)
      
# n=int(input("enter the value of n"))
# for i in range(1,n+1):    
#     print(" "*(n-i)+ "*" * i)
    
#output:
#     *
#    *   n n*
#   ***
#  ****
# *****

# n=int(input("enter the value of n"))
# for i in range(1,n+1):    
#     print(" "*(n-i)+ " *" * i)
# for i in range(n,0,-1):
#     print(" "*(i-n)+" *" * i)

#output:
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *

# n=int(input("enter the value of n"))
# for i in range(1,n+1,2):
#     #for j in range(1,n+1):         
#    print(" "*(n-i)+"* "*i)
# print()

#output
#     * 
#   * * *
# * * * * *   

# n=int(input("enter the value of n"))
# for i in range(n,0,-2):
#     #for j in range(1,n+1):
             
#    print(" "*(n-i)+"* "*i)
# print()  
#output
# * * * * * 
#   * * *
#     *

# n=int(input("enter the value of n"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print() 
  
#   output  
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5


# n=int(input("enter the value of n"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print() 

# output
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# n=int(input("enter the value of n"))
# # for i in range(1,n+1):
# #     for j in range(1,i+1):
# #         print(j,end=" ")
# #     print() 

# #output
# # 1 
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5
# # 1 2 3 4 5 6

# # n=int(input("enter the value of n"))
# # for i in range(1,n+1):
# #     for j in range(1,n+1):
# #         print(j,end=" ")
# #     print() 

# # n=int(input("enter the value of n"))
# # for i in range(1,n+1):
# #     for j in range(1,i):
# #         print(j,end=" ")
# #     print() 
    
# # n=int(input("enter the value of n"))
# # for i in range(1,n+1):    
# #     print(" "*(n-i)*i)  

# # n=int(input("enter the value of n"))
# # for i in range(n,0,-1):
# #     for j in range(1,n+1):
# #         print(i,end=" ")
# #     print() 
    
# # 6 6 6 6 6 6 
# # 5 5 5 5 5 5
# # 4 4 4 4 4 4
# # 3 3 3 3 3 3
# # 2 2 2 2 2 2
# # 1 1 1 1 1 1
  
# # n=int(input("enter the value of n"))
# # for i in range(n,0,-1):
# #     for j in range(1,n+1):
# #         print(j,end=" ")
# #     print() 

# #output
# # 1 2 3 4 5 6 
# # 1 2 3 4 5 6
# # 1 2 3 4 5 6
# # 1 2 3 4 5 6
# # 1 2 3 4 5 6
# 1 2 3 4 5 6
    
# n=int(input("enter the value of n"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print() 

#output
# 1 2 3 4 5 6 
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# n=int(input("enter the value of n"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print() 


# n=int(input("enter the value of n"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print() 
    
#output
# 6 6 6 6 6 6 
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# n=int(input("enter the value of n"))
# k=1
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(k,end=" ")
#     k+=1
#     print() 
    
#output
# 1 1 1 1 1 
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# n=int(input("enter the value of n"))
# for i in range(n,0,-1):
#     space=(n-i)*"  "
#     print(space,end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print() 
    
#output
# 1 2 3 4 5 
#   1 2 3 4
#     1 2 3
#       1 2
#         1

# n=int(input("enter the value of n"))
# for i in range(n,0,-1):
#     space=(n-i)*"  "
#     print(space,end="")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print() 
#output
# 5 5 5 5 5 
#   4 4 4 4
#     3 3 3
#       2 2
#         1


# n=int(input("enter the value of n"))
# for i in range(n,0,-1):                #n=5 #i=5 
#     print(" "*(n-i)+i)



# n=int(input("enter the value of n"))
# for i in range(1,n+1):    
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#       print(j,end="")
#     print()
    
#output:
#     1
#    12
#   123
#  1234
# 12345
# n=int(input("enter the value of n"))
# for i in range(n,0,-1):    
#     print(" "* (n-i),end="")
#     for j in range(1,i+1):
#       print(j,end="")
#     print()

#output
# 12345
#  1234
#   123
#    12
#     1

# n=int(input("enter the value of n"))
# for i in range(1,n+1):    
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#       print(j,end=" ")
#     print()
# for i in range(n,0,-1):    
#     print(" "* (n-i),end=" ")
#     for j in range(1,i+1):
#       print(j,end=" ")
#     print()
    
# #output
# #      1 
#     1 2
#    1 2 3
#   1 2 3 4
#  1 2 3 4 5
#  1 2 3 4 5
#   1 2 3 4
#    1 2 3
#     1 2
#      1

#write a py pro to print the upper case alphabets from a to z

# for ch in range(1,26):
#     print(chr(ch+97))                   ##askey value=upper case=A=65
                                        # lower case=a=97
# n=int(input("enter the value of n:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(i+64),end="  ")
#     print()

#output:
# A  A  A  A  A  
# B  B  B  B  B
# C  C  C  C  C
# D  D  D  D  D
# E  E  E  E  E

# n=int(input("enter the value of n:"))
# for i in range(n,0,-1):
#     for j in range(1,n+1):
#         print(chr(i+64),end="  ")
#     print()

#output
# E  E  E  E  E  
# D  D  D  D  D
# C  C  C  C  C
# B  B  B  B  B
# A  A  A  A  A

# n=int(input("enter the value of n:"))
# for i in range(n,0,-1):
#     for j in range(1,n+1):
#         print(chr(i+96),end="  ")
#     print()

#output
# e  e  e  e  e  
# d  d  d  d  d
# c  c  c  c  c
# b  b  b  b  b
# a  a  a  a  a

# n=int(input("enter the value of n:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(i+96),end="  ")
#     print()
#output
# a  a  a  a  a  
# b  b  b  b  b
# c  c  c  c  c
# d  d  d  d  d
# e  e  e  e  e

# n=int(input("enter the value of n:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(j+96),end="  ")
#     print()
#output:
# a  b  c  d  e  
# a  b  c  d  e
# a  b  c  d  e
# a  b  c  d  e
# a  b  c  d  e

# n=int(input("enter the value of n:"))
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(chr(j+96),end="  ")
#     print()
#output
# e  d  c  b  a  
# e  d  c  b  a
# e  d  c  b  a
# e  d  c  b  a
# e  d  c  b  a

# n=int(input("enter the value of n:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(j+64),end="  ")
#     print()
#output
# A  B  C  D  E  
# A  B  C  D  E
# A  B  C  D  E
# A  B  C  D  E
# A  B  C  D  E

# n=int(input("enter the value of n:"))
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(chr(j+64),end="  ")
#     print()
    
#output
# E  D  C  B  A  
# E  D  C  B  A
# E  D  C  B  A
# E  D  C  B  A
# E  D  C  B  A

# n=int(input("enter the value of n"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i%2==0):
#             print("* ",end="")
#         else:
#             print(chr(i+64),end=" ")
#     print()

#output
# A A A A A 
# * * * * *
# C C C C C
# * * * * *
# E E E E E

# n=int(input("enter the valueof n"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(i+64),end=" ")
#     print()
#output
# A 
# B B
# C C C
# D D D D
# E E E E E
# n=int(input("enter the valueof n"))
# for i in range(n,0,-1):
#     for j in range(i):
#         print(chr(i+64),end=" ")
#     print()
#output
# E E E E E 
# D D D D
# C C C
# B B
# A
# n=int(input("enter the value :"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(j+65),end=" ")
#     print()
#output
# A 
# A B
# A B C
# A B C D
# A B C D E

# n=int(input("enter the value :"))
# for i in range(n,0,-1):
#     for j in range(i):
#         print(chr(j+65),end=" ")
#     print()
#output:
# A B C D E 
# A B C D
# A B C
# A B
# A


# n=int(input("enter the valueof n"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(i+96),end=" ")
#     print()
    
#output
# a 
# b b
# c c c
# d d d d
# e e e e e

# n=int(input("enter the valueof n"))
# for i in range(n,0,-1):
#     for j in range(i):
#         print(chr(i+96),end=" ")
#     print()
#output:
# e e e e e 
# d d d d
# c c c
# b b
# a

# n=int(input("enter the value :"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(j+97),end=" ")
#     print()
    
#output:
# a 
# a b
# a b c
# a b c d
# a b c d e


# n=int(input("enter the value :"))
# for i in range(n,0,-1):
#     for j in range(i):
#         print(chr(j+97),end=" ")
#     print()
# output:
# a b c d e 
# a b c d
# a b c
# a b
# a

n=int(input("enter the value:"))
for i in range(1,n+1):
    print(""*(n-i),i)
    for j in range(i):
        print(chr(j+65),end="")
    print()
    
