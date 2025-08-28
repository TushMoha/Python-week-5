

# Assignment 1: Design Your Own Class! 🏗️

# Parent class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        # attributes
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    # method to display phone details
    def phone_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery}% battery"

    # method to simulate charging
    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        return f"{self.model} charged to {self.battery}%"

# Child class: GamingSmartphone (inheritance from Smartphone)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        # call parent constructor
        super().__init__(brand, model, storage, battery)
        # new attribute
        self.gpu = gpu

    # method specific to GamingSmartphone
    def play_game(self, game):
        if self.battery > 20:
            self.battery -= 20
            return f"Playing {game} on {self.model} with {self.gpu} GPU. Battery left: {self.battery}%"
        else:
            return f"Battery too low to play {game}! Please charge your {self.model}."

# Example objects
phone1 = Smartphone("Samsung", "Galaxy S21", 128, 75)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 256, 60, "Adreno 740")

print(phone1.phone_info())              # Basic smartphone info
print(phone1.charge(15))                # Charging
print(gaming_phone.phone_info())        # Inherited method
print(gaming_phone.play_game("PUBG"))   # Child class method
print(gaming_phone.charge(50))          # Charging again


# ------------------------------------------------------------------
# Activity 2: Polymorphism Challenge 

class Animal:
    def move(self):
        pass   # To be defined in subclasses

class Dog(Animal):
    def move(self):
        return "Running"

class Bird(Animal):
    def move(self):
        return "Flying"

class Fish(Animal):
    def move(self):
        return "Swimming"

# Example usage
animals = [Dog(), Bird(), Fish()]

for a in animals:
    print(a.move())   # Polymorphism in action 
