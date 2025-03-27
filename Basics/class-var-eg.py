class Amazon:
    Over_disc=5  #class variable
    def __init__(self,price,name,discount):
        self.price=price
        self.name=name
        self.discount=discount

    def disc(self):
        final_disc=self.price - self.price*self.discount/100 - self.price*Amazon.Over_disc/100
        return final_disc
    
p1=Amazon(100,'a',10)
print(p1.disc())