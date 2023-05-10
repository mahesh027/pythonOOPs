
class nokia():
    company="nokia india"
    website="www.nokia.com"
    def contact_detail(self):
        print("address: kaloor,kerala,india")
class nokia1100(nokia): #inherited ,now can access any variables or method of class nokia() inside class nokia1100
    def __init__(self):
        self.name="nokia 1100"
        self.year=2000
    def product_details(self):
        print("name :",self.name)
        print("year :",self.year)
        print("company:",self.company)
        print("website :",self.website)

o=nokia1100()
o.product_details()
o.contact_detail()