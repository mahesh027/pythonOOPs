class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
      #  self.msg=self.name+"is"+str(self.age)+"year"
    @property
    def msg(self):
        return self.name+"is"+str(self.age)+"year"
o=user("mahesh",21) #the value 21 or mahesh cannot be changed by using o.age=45 or o.name=virat...because it is a consructor(but if we are returning these values inside function of the same class,then the value will be changed),if want to change the value then we can create another object and pass that value like obj=user("virat",45) or else can use property decorator
print(o.name)
print(o.age)
#print(o.msg())
print(o.msg)
o.age=45
print(o.msg)
#print(o.msg()) // if @property is not used call like this or else
