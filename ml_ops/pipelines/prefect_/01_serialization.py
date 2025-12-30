"""
Simple Prefect pipeline demonstrating serialization.
Shows how a Prefect flow can use external functions.
"""

from prefect import flow, task

# External variable (outside the Prefect task)
MULTIPLIER = 10


# External class (outside the Prefect task)
class Calculator:
    def multiply(self, value):
        return value * MULTIPLIER


# External function (outside the Prefect task)
def add(a, b):
    return a + b


@task
def calculate(x, y):
    result = add(x, y)  # Uses external function
    calc = Calculator()  # Uses external class
    return calc.multiply(result)  # Uses external variable via class


@flow
def simple_flow():
    result = calculate(5, 3)
    print(f"Result: {result}")


if __name__ == "__main__":
    simple_flow()
