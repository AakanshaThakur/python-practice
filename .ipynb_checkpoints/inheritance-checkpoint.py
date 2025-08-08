class Parent:
    #properties
    def Lands(self):
        print("I have 150 Ekar Lands")
        pass


class Child(Parent):
    #Properties
    def Money(self):
        print("I have 11 Cr. Rupees")
        pass

p=Parent()
p.Lands()
p.Money()

#Single Inheritance
class A:
    num1=int(input("Enter 1st no. : "))
    num2=int(input("Enter 2nd no. : "))
    def Add(self):
        print("Addition: ",self.num1 + self.num2)
    def Sub(self):
        print("Subraction: ",self.num1 - self.num2)

class B(A):
    def Mul(self):
        print("Multiplication: ",self.num1 * self.num2)

    def Div(self):
        print("Division: ",self.num1 / self.num2)

    def Reminder(self):
        print("Reminder: ",self.num1 % self.num2)

obj=B()
obj.Add()
obj.Sub()
obj.Mul()
obj.Div()
obj.Reminder()

#Multi-Level Inheritance

class Parent():
    surname="Singh"
class Child1(Parent):
    def Show(self):
        print("Aakansha",self.surname)
class Child2(Child1):
    def Dis(self):
        print("Akka",self.surname)

s=Child1()
s.Show()

d=Child2()
d.Dis()
d.Show()

#Multiple Inheritance
class SeniorDeveloper:
    Backend_Techstack="Oracle DB and Java"
    def Backend(self):
        print("Backend task implemented using: ",self.Backend_Techstack)
class JuniorDeveloper:
     Frontend_Techstack="HTML, CSS, Javascript"
     def Frontend(self):
        print("Frontend task implemented using: ",self.Frontend_Techstack)
class TeamLead(SeniorDeveloper, JuniorDeveloper):
    def Show(self):
        print("Dynamic Website Created")

T = TeamLead()
T.Backend()
T.Frontend()
T.Show()

# Hierarchical Inheritance

class Parent:
    surname="Shivaya";
    def Show(self):
        print("My Surname is ",self.surname)

class Child1(Parent):
    def Dis(self):
        print("My name is Om ",self.surname)

class Child2(Parent):
    def Display(self):
        print("My name is Namah ",self.surname)

c1=Child1()
c1.Dis()
c1.Show()

c2=Child2()
c2.Display()
c2.Show()