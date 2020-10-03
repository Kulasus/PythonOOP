class Employee:

    def __init__(self,name):
        self.name = name

    def displayEmployeeDetails(self):
        print(self.name)

emp1 = Employee("Mark")
emp2 = Employee("Ben")
emp1.displayEmployeeDetails()
emp2.displayEmployeeDetails()