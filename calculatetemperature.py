import argparse

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



dictionary_temperature = {'January': 12, 'February': 13, 'March': 15, 'April': 16, 'May': 18, 'Juny': 21, 'July': 24,
                          'August': 25, 'September': 23, 'October': 19, 'November': 16, 'December': 14}

dictionary_temperature_values = [dictionary_temperature[k] for k,v in dictionary_temperature.items()]


