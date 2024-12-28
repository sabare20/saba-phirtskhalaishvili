from abc import ABC, abstractmethod

# აბსტრაქტული კლასი Appliance
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# კონკრეტული კლასი WashingMachine
class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing machine is now ON")

    def turn_off(self):
        print("Washing machine is now OFF")

# კონკრეტული კლასი Refrigerator
class Refrigerator(Appliance):
    def turn_on(self):
        print("Refrigerator is now ON")

    def turn_off(self):
        print("Refrigerator is now OFF")

# ფუნქცია operate_appliance
def operate_appliance(appliance):
    appliance.turn_on()
    appliance.turn_off()

def main():
    washing_machine = WashingMachine()
    refrigerator = Refrigerator()
    operate_appliance(washing_machine)
    operate_appliance(refrigerator)
if __name__ == '__main__':
    print(main())