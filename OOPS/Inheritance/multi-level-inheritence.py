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
        Licence.__init__(self,f_name,l_name,mbl,age,licence_id,validity,veh_no,veh_age)
        self.veh_no=veh_no
        self.veh_age=veh_age

    def is_valid_driver(self):
        if self.age >=20:
            return True
        else:
            return False
        
veh1=Vehicle('user','one',234,21,101,2020,123,10)
print(veh1.full_name())
print(veh1.is_valid_driver())
print(veh1.is_valid_licence())