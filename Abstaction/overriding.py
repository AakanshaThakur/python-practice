class A:
    def Disp(self):
        print("This is parent class method")

class B(A):
    def Disp(self):
        super().Disp()
        print("This is child class method")

obj = B()
obj.Disp()
