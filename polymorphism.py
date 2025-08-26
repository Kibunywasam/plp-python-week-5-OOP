class Animal:
    def move(self):
        pass  # Placeholder for polymorphism

class Dog(Animal):
    def move(self):
        print("The dog runs on four legs.")

class Bird(Animal):
    def move(self):
        print("The bird flaps its wings and flies!")

class Fish(Animal):
    def move(self):
        print("The fish swims gracefully through water.")

class Snake(Animal):
    def move(self):
        print("The snake slithers silently on the ground.")

# Polymorphism in action!
def demonstrate_movement(animal: Animal):
    animal.move()

# Test polymorphism
print("Animal Movement")
animals = [Dog(), Bird(), Fish(), Snake()]

for animal in animals:
    demonstrate_movement(animal)