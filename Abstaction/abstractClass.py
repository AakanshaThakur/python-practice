from abc import ABC,abstractmethod
class Car(ABC):
    def Show(self):
        print("Every car has 4 wheels")
    @abstractmethod
    def Speed(self):
        pass

class Fortuner(Car):
    def Speed(self):
        print("Fortuner's Speed is 190kmph")

class Porsche(Car):
    def Speed(self):
        print("Porsche's Speed is 293kmph")

obj=Fortuner()
obj.Show()
obj.Speed()

obj2=Porsche()
obj2.Show()
obj2.Speed()