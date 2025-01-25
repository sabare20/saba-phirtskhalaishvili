class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("The car is driving")

class Bike(Vehicle):
    def move(self):
        print("The bike is cycling")

class Truck(Vehicle):
    def move(self):
        print("The truck is hauling")

def test_vehicles(vehicles: list):
    for vehicle in vehicles:
        vehicle.move()

def main():
    car = Car()
    bike = Bike()
    truck = Truck()

    vehicles = [car, bike, truck]
    test_vehicles(vehicles)
if __name__ == '__main__':
    main()