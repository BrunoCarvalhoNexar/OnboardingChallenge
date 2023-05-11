import pytest

from calculatetemperature import CalculateTemperature

def test_average_temperature(get_dictionary_temperature):
    avg_temperature = CalculateTemperature.avg_temperature(get_dictionary_temperature, [get_dictionary_temperature[k] for k,v in get_dictionary_temperature.items()])
    assert avg_temperature == 18.0

def test_coldest_temperature(get_dictionary_temperature):
    coldest = CalculateTemperature.coldest(get_dictionary_temperature)
    assert coldest == ('January', 12)

def test_hottest_temperature(get_dictionary_temperature):
    hottest = CalculateTemperature.hottest(get_dictionary_temperature)
    assert hottest == ('August', 25)