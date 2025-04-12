class Amazon:
    Over_disc=5  #class variable
    def __init__(self,price,name,discount):
        self.price=price
        self.name=name
        self.discount=discount

    def final_price(self):
        final_price=self.price - self.price*self.discount/100 - self.price*Amazon.Over_disc/100
        return final_price
    
    def print_data(self):
        print("---------------")
        print("price: ",self.price)
        print("name: ",self.name)
        print("discount: ",self.discount)
        print("final price: ",self.final_price())
    
    @classmethod
    def change_over_disc(clc,disc):  #class method
        clc.Over_disc=disc

    @staticmethod
    def something(): #we dont use class methods or class vars,its just a normal function
        print("hii")


p1=Amazon(100,'a',10)
p1.print_data()

Amazon.change_over_disc(10)  #we can only call class method using class name
p1.print_data()

Amazon.something() #we can access static methods using class and class methods
p1.something()  