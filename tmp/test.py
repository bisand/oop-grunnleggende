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

app = Flask("test")

test = Test("Testing 123")
test.print_test()


@app.route("/")
def index():
    return f"Hello from {test.test}"


app.run()
