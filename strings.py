class Car:
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.colour} {self.model}")

    def stop(self):
        print(f"You stop driving the {self.colour} {self.model}")

    def describe(self):
        print(f"{self.year} {self.colour} {self.model}")









car1 = Car("VW", 2008, "Red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "Yellow", True)


car1.describe()
car2.describe()

car3.describe()