class A:   # Method Overloading
    # def Show(self):
    #     print("Heyy")

    # def Show(self,firstname=''):
    #     print("Heyy",firstname)

    def Show(self,firstname='', lastname=''):
        print("Heyy",firstname,lastname)

obj = A()
obj.Show()
obj.Show("Aakansha")
obj.Show("Aakansha","Thakur")