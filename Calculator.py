class Calculator:
    """
    BMR formula to calculate ideal amount of calories:
    10*weight + 6.25*height - 5*age + 5 - 10*temperature.
    """

    def __init__(self, weight, height, age):
        self.weight = weight
        self.height = height
        self.age = age

    def calculate(self):
        pass
