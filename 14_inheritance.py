# 14_inheritance - Python by Example

class Animal:
    def speak(self):
        return "I make a sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def main():
    for pet in [Dog(), Cat(), Animal()]:
        print(f"{pet.__class__.__name__}: {pet.speak()}")

if __name__ == "__main__":
    main()
