class demo():
    pass #cant create a empty class and empty function, to avoid that error pass keyword is used inside a class amd functions
a=10
print(type(a))
print(type(demo))
obj=demo() #object created for the class demo()

print(isinstance(obj,demo))
print(isinstance(a,int))
print(type(obj))