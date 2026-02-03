class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.fined = False

    def drive_to(self, destination):
        print(f"Driving {self.model} to", destination)




class Bus(Car):
    def __init__(self, color, model, number):
        super().__init__(color, model)
        self.number = number
    def drive_to(self, destination):
        super().drive_to(destination)
        print(f"Bus{self.model} is driving to", destination)


class Truck(Car):
    pass
car_subaru = Car("silver", "Forester")
print(car_subaru.model, car_subaru.color)
bus_42 = Bus("red", "Man",6)
print(bus_42.model)
bus_42.drive_to("Bishkek")
        