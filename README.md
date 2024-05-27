# Objektorientert Programmering

## Grunnleggende

### Klasser og objekter

Klasser er en måte å definere objekter på. Objekter er en instans av en klasse. En klasse kan ha attributter og metoder. Attributter er egenskaper til objektet, mens metoder er funksjoner som kan utføres på objektet.

```python
class Person:
    # Class variable
    count = 0

    def __init__(self, name, age):

        self.name = name
        self.age = age
        # Increment the count when a new instance is created
        Person.count += 1

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


    # Class method
    @classmethod
    def print_count(cls):
        print(f"Total number of persons: {cls.count}")

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

person1.print_info()
person2.print_info()

Person.print_count()

```

### Oppgaver

Klikk [her](oppgaver/oppgaver.md) for å se oppgaver.
