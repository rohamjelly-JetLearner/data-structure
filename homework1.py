class car:
    def __init__(self,speed,size,acceleration):
        self.speed=speed
        self.size=size
        self.acceleration=acceleration
    def brake(self):
        self.speed-=10
    def accelerate(self):
        self.speed+=10
class audi(car):
    def __init__(self,speed,size,acceleration,model):
        car. __init__(self,speed,size,acceleration)
        self.model=model
    def brake(self):
        self.speed-=20
    def accelerate(self):
        self.speed+=30
    def description(self):
        print('it has ',[self.speed],' and has a ',[self.size],' size with a ',[self.acceleration],'amount of acceleration and is version ',[self.model])
    def speedshow(self):
        print(self.speed)
class mercedes(car):
    def __init__(self,speed,size,acceleration,benz):
        car. __init__(self,speed,size,acceleration)
        self.benz=benz#say is/isnt
    def brake(self):
        self.speed-=40
    def accelerate(self):
        self.speed+=50
    def description(self):
        print('it has ',[self.speed],' and has a ',[self.size],' size with a ',[self.acceleration],'amount of acceleration and it ',[self.benz],' a mercedes benz' )
    def speedshow(self):
        print(self.speed)
car1=audi(10,'10','10','v1')
car1.description()
car2=mercedes(20,'20','20','is')
car2.description()
car2.speedshow()
car2.brake()
car2.speedshow()
car2.accelerate()
car2.accelerate()
car2.speedshow()