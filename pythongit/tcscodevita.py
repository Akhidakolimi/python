          ##tcs code vita pro 1 
          #solution type 1
# n=int(input())
# n=list(str(n))
# x=n.count('3')
# y=n.count('7')
# print(x+y)
 
            ##sol type 2
# n=input().strip()
# print(sum(1 for d in n if d in ['3','7']))

           #prob 2
##solu 1
# str=list(input().split())
# print(len(max(str)))

# prob 3
# n=int(input())
# print(n)
# for i in range (n):
#    even=list(filter(lambda x:x%2==0,n))
#    odd=list(filter(lambda x:x%2!=0,n))
# print(even,odd)
            
# n=int(input())
# digit=list(map(int,input().split()))
# add=[i for i in digit if i%2==0]+[i for i in digit if i%2!=0]
# print(add)


#prob4
# n=input().split()     
# n=n[::-1]
# print(*n)

#prob 5
# n=input().upper()
# original=n
# a=n[::-1]
# if original==a:
#     print("Yes")
# else:
#     print("No")

#sol 2
# n=input().upper()
# print("yes") if n==n[::-1] else print("no")

#pro 6
# n=list(map(int,input().split()))
# print(sum(i for i in n))

n=list(map(int,input().split()))
n=n(reverse=True)
print(n[1])














