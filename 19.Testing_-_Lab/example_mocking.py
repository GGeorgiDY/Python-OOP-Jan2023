import requests


def get_weather(city):
    url = f'https://api.weather.com/current?city={city}'
    response = requests.get(url)
    data = response.json()
    temperature = data['temperature']
    return temperature


# print(get_weather('Shumen'))


import unittest
from unittest.mock import patch
# patch замества функцията requests.get()


def test_det_weather():
    mock_response = {
        'temperature': 25.0
    }
    with patch('request.get') as mock_get:
        mock_get.return_value.json.return_value = mock_response

        temperature = get_weather('mock_city')
        assert_temperature = 25.0


if __name__ == '__main__':
    unittest.main()