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


app = Flask("test")

test = Test("Testing 123")
test.print_test()

@app.route('/')
def index():
    return f'Hello from {test.test}'

app.run()
