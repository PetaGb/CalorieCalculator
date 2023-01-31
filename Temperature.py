import requests
from selectorlib import Extractor


class Temperature:
    """
    Temperature is scraped from timeanddate.com/weather
    """
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    url_base = "https://www.timeanddate.com/weather/"

    def __init__(self, state, city):
        self.state = state.replace(" ", "-")
        self.city = city.replace(" ", "-")


    def scrape(self):
        url = self.url_base + self.state + "/" + self.city
        r = requests.get(url, headers=self.headers).text
        extractor = Extractor.from_yaml_file("temperature.yaml")
        c = extractor.extract(r)
        return c['temp'][0]

#if __name__ == "__main__":
 #   temp = Temperature(state="czech republic", city="brno")
  #  print(temp.scrape())








