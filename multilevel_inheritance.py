class grandfather:
    def ownhouse(self):
        print("grandpa house")
class father(grandfather):
    def ownbike(self):
        print("fathers bike")
class son(father):
    def ownbook(self):
        print("son have a book")
o=son()
o.ownbook()
o.ownbike()
o.ownhouse()

o1=father()
o1.ownbike()
o1.ownhouse()
#o1.ownbook() not possible