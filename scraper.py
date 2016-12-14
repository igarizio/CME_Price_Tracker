# -*- coding: utf-8 -*-
from urllib import request
import json
from configparser import ConfigParser


class Scraper:
    def __init__(self, contract):
        parser = ConfigParser()
        parser.read('config.ini')

        self.url = parser.get('urls', 'cme') + contract.upper()
        self.headers = {'User-Agent': parser.get('urls', 'user_agent')}

    def get_price(self):
        req = request.Request(self.url, headers=self.headers)
        with request.urlopen(req) as response:
            html = response.read().decode("utf-8", "ignore")
            dict_res = json.loads(html)
            actual_p = float(dict_res['quotes'][0]['last'])
            print(actual_p)
        return actual_p
