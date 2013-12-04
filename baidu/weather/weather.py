"""百度天气api
"""
import json
from urllib.parse import urlencode
from urllib.request import urlopen


class Weather():
    API_URL = 'http://api.map.baidu.com/telematics/v3/weather?'

    def __init__(self, ak):
        self.ak = ak

    def get_weather(self, location='济南', output='json'):
        data = {
            'location': location,
            'output': output,
            'ak': self.ak
        }

        url = Weather.API_URL + urlencode(data)
        response = urlopen(url)
        return json.loads(response.read().decode())


if __name__ == '__main__':
    w = Weather('873a531cec3212a4906a683572b248b5')
    print(w.get_weather('北京'))

