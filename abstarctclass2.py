from abc import ABC ,abstractmethod
class Shape(ABC):
    def __init__(self,color,borderwidth):
        self.__color=color
        self.__borderwidth=borderwidth
    def getcolor(self):
        return self.__color
    def getborderwidth(self):
        return self.__borderwidth
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
class Circle(Shape):
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return Circle.pi*self.radius*self.radius
class Triangle(Shape):
    def __init__(self,base ,hight):
        self.base=base
        self.hight=hight
    def area(self):
        return 0.5 *self.base*self.hight
r=Rectangle(5,6)
print(r.area())
c=Circle(5)
print(c.area())
t=Triangle(5,6)
print(t.area())



