class Employee:
    basic=0
    TA=0
    DA=0
    def salary(self):
        print("salary is:",self.basic+self.TA+self.DA)
emp1=Employee()
emp1.basic=20000
emp1.TA=5000
emp1.DA=1000
emp1.salary()
