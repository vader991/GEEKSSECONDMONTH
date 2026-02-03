class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.fined = False

    def drive_to(self, destination):
        if not self.fined:
            print(f"Driving {self.model} to", destination)
        else:
            print("Машина оштрафована")
car_subaru = Car("silver", "Forester")

car_honda = Car("Black", "Jazz")
car_subaru.color = "white"
print(car_subaru.color, car_subaru.model)
car_subaru.drive_to("Bishkek")
print(car_honda.color, car_honda.model)
car_honda.maxspeed = 140
print(car_honda.maxspeed)



