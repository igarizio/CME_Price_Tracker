# -*- coding: utf-8 -*-
from urllib import request
import json


class Scraper:
    def __init__(self, contract):
        self.url = "http://www.cmegroup.com/CmeWS/mvc/Quotes/FutureContracts/XNYM/G?quoteCodes=" + contract.upper()
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"}

    def get_price(self):
        req = request.Request(self.url, headers=self.headers)
        with request.urlopen(req) as response:
            html = response.read().decode("utf-8", "ignore")
            dict_res = json.loads(html)
            p_actual = float(dict_res['quotes'][0]['last'])
        return p_actual
