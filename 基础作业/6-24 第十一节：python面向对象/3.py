class Jx:
    def __init__(self,long,width):
        self.long=long
        self.width=width
    def area(self):
        return self.long*self.width
    def __add__(self,other):
        area=self.area()+other.area()
        return area
    def __sub__(self,other):
        area=self.area()-other.area()
        return area
    def __mul__(self,other):
        area=self.area()*other.area()
        return area
    def __mod__(self,other):
        area=self.area()%other.area()
        return area

a=Jx(3,4)
b=Jx(5,3)
