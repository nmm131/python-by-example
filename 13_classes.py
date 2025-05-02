# 13_classes - Python by Example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

def main():
    alice = Person("Alice", 30)
    print(alice.greet())

if __name__ == "__main__":
    main()
