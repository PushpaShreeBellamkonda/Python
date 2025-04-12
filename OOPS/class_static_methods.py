class Amazon:
    overall=5  #class varuable
    def __init__(self,id,name,price,dis):
        self.id=id
        self.name=name
        self.price=price
        self.dis=dis

    def actual_price(self):
        return self.price - self.price*self.dis/100 - Amazon.overall*self.price/100
    
    def print_data(self):
        print('----------------')
        print('id: ',self.id)
        print('name: ',self.name)
        print('final price: ',self.actual_price())

p1=Amazon(1,'a',500,8)
p2=Amazon(2,'b',600,11)

p1.print_data()
p2.print_data()

