class student():
    name="mahesh"
    age=25

    def printall():
        print("name:",student.name)
        print("age:",student.age)
student.printall()
print(student.__dict__)

print(getattr(student,"printall"))
getattr(student,"printall")()
student.__dict__['printall']()