class Employee:
    
    def employeeDetails(self):
        self.name = "Ben"

    @staticmethod
    def welcomeMessage():
        print("Welcome to our organization!")


em1 = Employee()
em1.employeeDetails()
print(em1.name)
em1.welcomeMessage()