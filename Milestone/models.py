class NetSalary:
    def __init__ (self, salary, benefits):
        self.salary = salary
        self.benefits =benefits

    @classmethod
    def payee(cls, salary):
        if(0<salary<=24000):
            tax = 0.1*salary
        elif(24001<=salary<=40667):
            tax = 0.15*salary
        elif(40668<=salary<=57334):
            tax = 0.2*salary
        else:
            tax = 0.25 *salary

        return tax

    @classmethod
    def NHIFdeductions(cls, salary, benefits):
        gross_salary = (salary +benefits)

        if(0<gross_salary<=5999):
            nhif = 150
        elif(6000<=gross_salary<=7999):
            nhif = 300
        elif(8000<=gross_salary<=11999):
            nhif = 400
        elif(12000<=gross_salary<=14999):
            nhif = 500
        elif(15000<=gross_salary<=19999):
            nhif = 600

        elif(20000<=gross_salary<=24999):
            nhif = 750
        elif(25000<=gross_salary<=29999):
            nhif = 850
        elif(30000<=gross_salary<=34999):
            nhif = 900
        elif(35000<=gross_salary<=39999):
            nhif = 950


        elif(40000<=gross_salary<=44999):
                nhif = 1000
        elif(45000<=gross_salary<=49999):
            nhif = 1100
        elif(50000<=gross_salary<=59999):
            nhif = 1200
        elif(60000<=gross_salary<=69999):
            nhif = 1300

        elif(70000<=gross_salary<=79999):
            nhif = 1400
        elif(80000<=gross_salary<=89999):
            nhif = 1500 
        elif(90000<=gross_salary<=99999):
            nhif = 1600
        else:
            nhif=1700

        return nhif


    @classmethod
    def NSSFdeductions(cls, salary):
        nssf = 0.06 * salary

        return nssf

    @classmethod
    def grossSalary(cls, salary, benefits):
        gross = salary + benefits
        return gross
    
    def netSalary(self, salary,benefits):
        tax =self.payee(salary)
        nhif= self.NHIFdeductions(salary, benefits)   
        nssf = self.NSSFdeductions(salary) 
        gross_salary=self.grossSalary(salary, benefits)
        total_deductions = nhif+nssf+tax
        net = gross_salary-total_deductions  
        
        return net
