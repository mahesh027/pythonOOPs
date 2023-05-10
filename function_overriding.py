class employee:
    def workingHrs(self):
        self.hrs=50
    def printHrs(self):
        print("totak working hours:",self.hrs)

class trainee(employee):
    def workingHrs(self):
        self.hrs=60
    def resetHrs(self):
        super().workingHrs()

emp=employee()
emp.workingHrs()
emp.printHrs()

trainee=trainee()
trainee.workingHrs()
trainee.printHrs()
#reset trainee hrs to 50 by super()//super() implies parent class ie employee
trainee.resetHrs()
trainee.printHrs()
