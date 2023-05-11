import pytest


class CalculateTemperature:

    def __init__(self, temp):
        self.temperature = temp

    def hottest(self):
        return max(self.items(), key=lambda x: x[1])

    def coldest(self):
        return min(self.items(), key=lambda x: x[1])

    def avg_temperature(self, dictionary_temperature_values):
        return sum(dictionary_temperature_values) / len(dictionary_temperature_values)


