#duck typing
# class duck:
#     def walk(self):
#         print("thapak thapak thapk thapak")
# class horse:
#     def walk(self):
#         print("tabdak tabdak tabdak tabdak")
# def myfunction(obj):
#     obj.walk()
# d=duck()
# myfunction(d)
# h=horse()
# myfunction(h)


#method overriding
class engineer:
    def __init__(self):
        pass
    def work(self):
        print("engineer works")
class softwareengineer:
    def __init__(self):
        
      super().__init__()
    def work(self):
        print("s/w enginner works")
class civilengineer:
    def __init__(self): 
        super().__init__()
    def work(self):
         print("civil enginner works")
e=engineer()

se=softwareengineer()

c=civilengineer()
c.work()
e.work()
se.work()
        
    
        
        
        
        
        

