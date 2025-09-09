                                   ##programm 2
       
num=int(input("enter the integer :"))
#if else
if(num>=-9 and num<=9):
    print("digit")
else:
    print("number")
     
    # or (in simple)
     
       #ternary operator 
res="digit" if(num>=-9 and num<=9) else "number"
print(res)