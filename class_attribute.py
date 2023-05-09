class student():
    name="mahesh"
    age=20

#accessing class
 #1.getattr method
print(getattr(student,"name"))
print(getattr(student,'age'))
print(getattr(student,'gender','no such attribute found'))

#dotNotation
print(student.name)
print(student.age)
#setattr method //to set new data inside class
setattr(student,"name","virat")
print(student.name)

setattr(student,"gender",'male')
print(student.gender)

student.city="delhi"
print(student.city)

print(student.__dict__) #it display all details about the class and its attributes in a dictionary

#delattr()
delattr(student,"city")
#print(student.city) #it show error as we deleted the attribute city...we can also check by __dict__ and compare it
print(student.__dict__)
del student.gender
print(student.__dict__)
