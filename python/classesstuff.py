class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width 
    def get_perimeter(self):
        return 2 * (self.length + self.width)
x= rectangle(2,3)
print('Area of rectangle', (x.get_perimeter()))
