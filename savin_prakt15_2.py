# Наследование мы ещё не проходили, поэтому погуглил и выполнил как понял :)

class Transport:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Autobus(Transport):
    def __init__(self,name,max_speed,mileage,capacity):
        super().__init__(name,max_speed,mileage)
        self.capacity=capacity

    def seating_capacity (self):
        print(f"Вместимость одного автобуса {Renault.name}: {Renault.capacity} пассажиров")
      
Renault=Autobus("Renault Logan",180,12,50)
Renault.seating_capacity()
