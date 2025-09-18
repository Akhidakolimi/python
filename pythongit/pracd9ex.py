# class employee():
#     def __init__(self,name,hourly_rate,hours_worked):
#         self.name=name
#         self.hourly_rate=float(hourly_rate)
#         self.hours_worked=float(hours_worked)
#     def show_details(self,salary):
#         print(f"employee name:{self.name}")
#         print(f"total salary:{salary:.2f}")
# #lambda for overtime calculation
# overtime_pay=lambda extra_hours,rate: extra_hours*rate*1.5
# def calculate_salary(rate,hours):
#     if hours<=40:
#         return hours*rate
#     else:
#         regular =40*rate
#         overtime=overtime_pay(hours-40,rate)
#         return regular+overtime
# name=input("enter the employee name:").strip()
# rate=(input("enter the rate of pay:").strip())
# hours=input("enter no of working hours:").strip()
# emp=employee(name,rate,hours)
# salary=calculate_salary(emp.hourly_rate,emp.hours_worked)      
# emp.show_details(salary)  
    

class student:
    def __init__(self,std_name,s1,s2,s3,s4,s5):

        self.std_name=std_name
        self.marks=[s1,s2,s3,s4,s5]
    
        self.avg=lambda : sum(self.marks)/5
    def grades(self):
      avg=self.avg()
      if avg>=90:
        return "A"
      elif avg (75>=avg<=89):
        return "B"
      elif avg(50>=avg<=74):
        return "C"
      else:
        return "fail"
    def display(self):
        print(f"std_name:{self.std_name}")
        print(f"average:{self.avg}")
name=input("enter the name").strip()
marks=list(map(int,input("enter the marks of 5 subjects ").split()))
std=student(name,marks[0],marks[1],marks[2],marks[3],marks[4])

std.display()