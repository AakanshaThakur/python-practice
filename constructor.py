# class A:
#     age=13
#     def __init__(self):
        
#         name="Aakansha"
#         print(name," ",self.age)

# obj=A()

class A:
    def __init__(self):
        print("Aakansha")
    def __init__(self):
        print("Aakanshaaaaaaaaaa")

obj=A()


#default constructor

class A:
    name="AKA"
    age=23
    def __init__(self):
        address="Khamgaon"
        print(self.name," ",address)
    def Show(self):
        print(self.age)

obj=A()
obj.Show()

# Parameterized Constructors

class A:
    name2="Aakansha"
    def __init__(self,age,name,address):
        address="Pune"
        print(age,name,address,self.name2)

    def Show(self):
        print(self.name2)

obj=A(23,"Akaaa",None)
obj.Show();