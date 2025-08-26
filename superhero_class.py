class Superhero:
    def __init__(self, name, power, city):
        self.name = name                
        self.power = power               
        self._identity_known = False    
        self.__health = 100 
        self.city = city             

    # Getter for health (encapsulation)
    def get_health(self):
        return self.__health

    # Method to simulate using power
    def use_power(self):
        print(f"{self.name} uses their power: {self.power}!")

    # Simulate taking damage
    def take_damage(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            print(f"{self.name} is down!")
        else:
            print(f"{self.name} took {damage} damage. Health left: {self.get_health()}")

    # Simulate healing
    def heal(self, amount):
        self.__health += amount
        print(f"{self.name} healed by {amount}. Health: {self.get_health()}")

    # String representation
    def __str__(self):
        return f"{self.name} from {self.city}, has the power of {self.power}!"


# Inheritance
class FlyingSuperhero(Superhero):
    def __init__(self, name, city, flight_speed):
        super().__init__(name, "Flight & Super Strength", city)
        self.flight_speed = flight_speed

    # Polymorphism
    def use_power(self):
        print(f"{self.name} soars through the sky at {self.flight_speed} mph!")

    # New method specific to FlyingSuperhero
    def dive_attack(self):
        print(f"{self.name} performs a supersonic dive attack!")



# Creating a regular superhero
spider = Superhero("Spider-Man", "Web-Slinging", "Kitui")
print(spider)
spider.use_power()
spider.take_damage(30)
spider.heal(10)

print()

# Creating a flying superhero (inheritance + polymorphism)
nova = FlyingSuperhero("Nova Flyer", "Skyhaven", 600)
print(nova)
nova.use_power()  
nova.dive_attack()