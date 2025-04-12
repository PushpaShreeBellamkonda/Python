class A:
    def __init__(self):
        self.a=10

class B:
    def __init__(self):
        self.a=100

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.a=1

ob1=C()
print(ob1.a)


# real life eg

class Driver:
    def __init__(self,f_name,l_name,mbl,age):
        self.f_name=f_name
        self.l_name=l_name
        self.mbl=mbl
        self.age=age

    def full_name(self):
        return f'{self.f_name} {self.l_name}'
    

class Licence(Driver):
    def __init__(self,f_name,l_name,mbl,age,licence_id,validity):
        Driver.__init__(self,f_name,l_name,mbl,age)
        self.licence_id=licence_id
        self.validity=validity

    def is_valid_licence(self):
        if self.validity >= 2021:
            return True
        else:
            return False
        

class  Vehicle(Licence):
    def __init__(self,f_name,l_name,mbl,age,licence_id,validity,veh_no,veh_age):
        Licence.__init__(self,f_name,l_name,mbl,age,licence_id,validity)
        self.veh_no=veh_no
        self.veh_age=veh_age

    def is_valid_driver(self):
        if self.age >=20:
            return True
        else:
            return False
        
class Petrol:
    def __init__(self,price):
        self.price=price

class Diesel:
    def __init__(self,price):
        self.price=price

class Bus(Vehicle,Diesel):
    def __init__(self,f_name,l_name,mbl,age,licence_id,validity,veh_no,veh_age,price,wheels):
        Vehicle.__init__(self,f_name,l_name,mbl,age,licence_id,validity,veh_no,veh_age)
        Diesel.__init__(self,price)
        self.wheels=wheels


bus=Bus('a','b',22,12,102,2021,33,2,20000,2)
print(bus.full_name())
print(bus.is_valid_driver())
print(bus.is_valid_licence())


        

"""
hierarchical== class Bus(Vehicle,Diesel)
               class Lorry(Vehicle,Diesel):
parent=vehicle
child =Bus,Lorry
"""

"""
Multiple== class Bus(Vehicle,Diesel)

parent=vehicle,Diesel
child=Bus
"""

"""
Hybrid==combination of atleast two inheritance type 


"""