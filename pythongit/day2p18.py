age=int(input("enter the age"))
if age<5:
    print("free ticket")
elif  5<=age<=12:
    print("half ticket")
elif 13 <=age<=59:
    print("full ticket")
elif age>=60:
    print("senior citizen discount")