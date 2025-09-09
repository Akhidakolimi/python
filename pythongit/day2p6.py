hours=int(input("enter hours"))
if hours>=4:
    print("you are dehydrated!drink water now")
elif hours>=2 or hours<=3:
    print("drink a glass of water")
elif  hours<2:
    print("you're fine")