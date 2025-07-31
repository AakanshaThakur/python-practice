from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def Show(self):
        pass

    @abstractmethod
    def Disp(self):
        pass

class Square(Shape):
    def Disp(self):
        pass
    
class Circle(Square):
    def Show(self):
        print("In CSS to create circle we need to give radius 50%");
    def Disp(self):
        print("Square has 4 sides..")


# obj = Square()
# obj.Show()
c= Circle()
c.Show()
c.Disp()

