class Musician:
    def __init__(self,a):
        self.members=a
    
class Band(Musician):
    instances=[]
    def __init__(self,n="",list1=[]):
        self.name=str(n)
        Musician.__init__(self,list1)
        Band.instances.append(self)
    def __str__(self):
        return f'Our band name is {self.name}'
    def __repr__(self):
        return f'Our member {self.members}'
    @classmethod
    def to_list(cls):
        return cls.instances
    def play_solos(self):
        solo=[]
        for i in self.members:
            print(f"Hello {i} did you need to play solo")
            solo.append(i.play_solo())
        return solo
        

class Guitarist(Musician):
    def __init__(self,n=""):
        self.name=str(n)
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    def play_solo(self):
        return "face melting guitar solo"
    def get_instrument(self,name="guitar"):
        return name

    
class Bassist(Musician):
    def __init__(self,n=""):
        self.name=str(n)
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    def play_solo(self):
        return "bom bom buh bom"
    def get_instrument(self,name="bass"):
        return name
    
class Drummer(Musician):
    def __init__(self,n=""):
        self.name=str(n)
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    def play_solo(self):
        return "rattle boom crash"
    def get_instrument(self,name="drums"):
        return name

