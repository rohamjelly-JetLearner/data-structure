class chocolates:
    def __init__(self,colour,taste,size,price,recipe):
        self.colour=colour
        self.taste=taste
        self.size=size
        self.price=price
        self.__recipe=recipe
    def prop(self):
        print(self.colour)
        print(self.taste)
        print(self.size)
        print(self.price)
        print(self.__recipe)
milk_chocolate=chocolates('brown','sweet','medium','1.50','cocoa butter,large amount of sugar')
milk_chocolate.prop()
dark_chocolate=chocolates('black','bitter','medium','2.00','cocoa beans,small amount of sugar')
dark_chocolate.prop()
print(dark_chocolate.__recipe)
