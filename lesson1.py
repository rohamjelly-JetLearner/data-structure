class chocolates:
    def __init__(self,colour,taste,size,price):
        self.colour=colour
        self.taste=taste
        self.size=size
        self.price=price
    def prop(self):
        print(self.colour)
        print(self.taste)
        print(self.size)
        print(self.price)
milk_chocolate=chocolates('brown','sweet','medium','1.50')
milk_chocolate.prop()
dark_chocolate=chocolates('black','bitter','medium','2.00')
dark_chocolate.prop()        