class circle:
    def __init__(self,radius):
        self.radius1=radius
    def area(self):
        area = 3.14*self.radius1**2
        return area 
    def circumerence(self):
        cir=3.14*2*self.radius1
        return cir


if __name__=="__main__":
    obj=circle(12)
    print('area of circle is ',obj.area())
    print('circumfarence of circle is ',obj.circumerence())