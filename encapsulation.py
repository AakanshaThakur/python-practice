#Encapsulation is that data member should be protected
class A:
    _a = 10 #protected
    __b=20 #private
    def Show(self):
        print("a = ",self._a)
        print("__b = ",self.__b)

obj = A()
obj.Show()
print("Outside of class",obj._a)
# print("Outside of class",obj.__b)