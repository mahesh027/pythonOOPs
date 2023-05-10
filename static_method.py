#static method/function is used when function is creted without (self) ie it is common function that can be called by any object
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printDetail(self):
        print("name:",self.name, "age:",self.age)

    @staticmethod
    def welcome():
        print("welcome to our institution")
o1=student("mahesh",21)
o1.printDetail()
o1.welcome()

o2=student("rahul",22)
o2.printDetail()
o2.welcome()