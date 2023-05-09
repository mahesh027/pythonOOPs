class user():
    course='java'
obj=user()
print(user.__dict__)
print(user.course)
print(obj.__dict__)
print(obj.course)
obj.course="c++"
print(obj.__dict__)
print(obj.course)
print(user.course)
obj2=user()
user.course='python'
print(user.course)
print(obj2.course)
print(user.__dict__)
print(obj.__dict__)
print(obj2.__dict__)
