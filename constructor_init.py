class user():
    def __init__(self,name):
        print("this function is called when new obj is created")
        self.name=name
      #  print("name:",self.name)
    def printall(self):
        print("name:",self.name)
o=user("mahsh")
o.printall()
print(o.__dict__)
o2=user("maheshhhh")
o2.printall()
print(o2.__dict__)