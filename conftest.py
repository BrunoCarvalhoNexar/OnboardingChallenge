import pytest

@pytest.fixture()
def get_dictionary_temperature():
    dictionary_temperature = {'January': 12, 'February': 13, 'March': 15, 'April': 16, 'May': 18, 'Juny': 21,
                              'July': 24,
                              'August': 25, 'September': 23, 'October': 19, 'November': 16, 'December': 14}
    return dictionary_temperature
