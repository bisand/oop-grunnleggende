# Objektorientert Programmering

## Grunnleggende

### Klasser og objekter

Klasser er en måte å definere objekter på. Objekter er en instans av en klasse. En klasse kan ha attributter og metoder. Attributter er egenskaper til objektet, mens metoder er funksjoner som kan utføres på objektet.

Eksempel på en klasse:

```python
class Person:
    # Klasss-variabel
    count = 0
    persons = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Øk telleren for hver gang en ny person blir laget
        Person.count += 1
        Person.persons.append(self)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

    def __del__(self):
        # Fjern personen fra listen når objektet blir slettet
        Person.count -= 1
        Person.persons.remove(self)

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # Klasse-metode
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

Oppgaver nedenfor er ment for å gi deg en forståelse av hvordan klasser og objekter fungerer. Disse skal leveres innen neste forelesning. Arbeidskravet vil bestå av å få godkjent minst 2 av oppgavene. Det er ønskelig at dere leverer så mange som mulig, men det er ikke et krav.

Klikk [her](oppgaver/oppgaver.md) for å se oppgaver ([PDF](oppgaver/oppgaver.pdf)).
