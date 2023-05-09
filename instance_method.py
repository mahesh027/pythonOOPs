class student():
    name="mahesh"
    age=25

    def printall(self,gender):
        print("name:",student.name)
        print("age:",student.age)
        print("gender:",gender)
o=student()
o.printall("male")
student.printall(o,"male")