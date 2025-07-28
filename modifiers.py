#Access Modifiers

class A:
    a = 10  #Public
    _b = 20 #protected
    __c = None #private
    print(a," ",_b," ",__c)
    # def Add(self):
    #     self.__c = self.a + self._b
    #     print("Addition: ",self.__c)

class B:
    def Show(self):
        print(A.a)
        print(A._b)
        # print(A.__c)
    

obj = B()
obj.Show()
# print(obj.a)
# print(obj._b)
# print(obj.__c)

# obj = A()
# obj.Add()
# print(obj.a)
# print(obj._b)
# print(obj.__c)