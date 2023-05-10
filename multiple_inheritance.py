class father():
    def fishing(self):
        print("fishing in river")
    def cricket(self):
        print("playing cricket")
    def income(self,salary):
        print("salary:",salary)
class mother:
    def cooking(self):
        print("cooking food")
    def chess(self):
        print("playing chess")

class son(father,mother): #inherited from father mother // multiple inheritance
    def ride(self):
        print("riding bike")
o=son()
o.cricket()
o.ride()
o.chess()
o.income(50000)