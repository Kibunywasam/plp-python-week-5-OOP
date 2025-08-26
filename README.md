# Object-Oriented Programming Assignment
 This assignment demonstrates core OOP principles: **encapsulation**, **inheritance**, and **polymorphism** through creative class design and real-world simulations.

---

## Project Structure

This project is divided into two main parts:

1. **Assignment 1: Design Your Own Class!**  
   - Created a `Superhero` class with attributes, methods, and encapsulation.
   - Extended it using inheritance with `FlyingSuperhero`.

2. **Assignment 2: Polymorphism Challenge!**  
   - Implemented polymorphism using an `Animal` base class.
   - Each animal subclass defines its own version of the `move()` method.

---

## Assignment 1: Superhero Class

### Features
- **Attributes**: `name`, `power`, `city`, protected `_identity_known`, and private `__health`.
- **Encapsulation**: The `__health` attribute is private and accessed via `get_health()`.
- **Methods**: `use_power()`, `take_damage()`, `heal()`, and custom string representation.
- **Inheritance**: `FlyingSuperhero` inherits from `Superhero` and adds flight speed and a dive attack.
- **Polymorphism**: `FlyingSuperhero` overrides `use_power()` for unique behavior.

### Example Usage
```python
spider = Superhero("Spider-Man", "Web-Slinging", "New York")
spider.use_power()
spider.take_damage(30)

nova = FlyingSuperhero("Nova Flyer", "Skyhaven", 600)
nova.use_power()  # Output: "Nova Flyer soars through the sky at 600 mph!"
