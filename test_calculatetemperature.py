import pytest

from calculatetemperature import CalculateTemperature


dictionary_temperature = {'January': 12, 'February': 13, 'March': 15, 'April': 16, 'May': 18, 'Juny': 21, 'July': 24,
                          'August': 25, 'September': 23, 'October': 19, 'November': 16, 'December': 14}
dictionary_temperature_values = [dictionary_temperature[k] for k, v in dictionary_temperature.items()]


def test_average_temperature():
    avg_temperature = CalculateTemperature.avg_temperature(dictionary_temperature, dictionary_temperature_values)
    assert avg_temperature == 18.0

def test_coldest_temperature():
    coldest = CalculateTemperature.coldest(dictionary_temperature)
    assert coldest == ('January', 12)

def test_hottest_temperature(hottest):
    hottest = CalculateTemperature.hottest(dictionary_temperature)
    assert hottest == ('August', 25)