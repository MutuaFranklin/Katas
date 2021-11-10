from models import NetSalary

    
salary = float(input("Enter Your salary: "))
benefits = float(input("Enter your total benefits: "))  

class_salary = NetSalary(salary, benefits)

net_salary =(class_salary.netSalary(salary, benefits))

print(net_salary)

