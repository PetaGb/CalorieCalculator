from Temperature import Temperature
class Calculator:
    """
    BMR formula to calculate ideal amount of calories:
    10*weight + 6.25*height - 5*age + 5 - 10*temperature.
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature


    def calculate(self):
        result = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5 - (10 * self.temperature)
        return result

temperature = float(Temperature(state="czech republic", city="brno").scrape())
calculator = Calculator(weight=75, height=180, age=36, temperature=temperature)
print(calculator.calculate())