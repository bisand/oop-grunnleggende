from flask import Flask


class Test:
    """
    A class representing a test.

    Attributes:
        test (any): The test value.
    """

    def __init__(self, test):
        self.test = test

    def print_test(self):
        """
        Test method
        """
        print(f"Hello from {self.test}")


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


app = Flask("test")

test = Test("Testing 123")
test.print_test()


@app.route("/")
def index():
    return f"Hello from {test.test}"


app.run()
