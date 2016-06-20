# -*- coding: utf-8 -*-
from scraper import Scraper
from notification import Notification
from time import sleep
from datetime import datetime


class Traker:
    def __init__(self, contract, p_target, tipo_lim):
        self.contract = contract
        self.p_target = p_target
        self.tipo_lim = tipo_lim
        self.scraper = Scraper(self.contract)
        self.log_file = "log.txt"

    def track_prices(self):
        with open(self.log_file, 'a+') as file:
            file.write("Target {}: {} -- {}\n".format(self.tipo_lim, self.p_target, datetime.now()))
            print("Target {}: {}".format(self.tipo_lim, self.p_target))

        while True:
            with open(self.log_file, 'a+') as file:
                try:
                    p_actual = self.scraper.get_price()
                    file.write("Precio actual: {}  -- {}\n".format(p_actual, datetime.now()))
                    print("Precio actual: {}  -- {}".format(p_actual, datetime.now()))

                except Exception:
                    p_actual = -1

                if p_actual != -1:
                    mult_lim = 1 if self.tipo_lim.lower() == "superior" else -1

                    if self.p_target*mult_lim - p_actual*mult_lim < 0:
                        file.write("Enviando notificación: -- {}\n".format(datetime.now()))

                        notification = Notification(p_actual, self.p_target, round(p_actual + 0.1 * mult_lim, 2), mult_lim == 1)
                        notification_text = notification.send_notifications()

                        file.write("{}\n{}\n{}\n".format("-"*50, notification_text, "-"*50))
                        print("Enviando notificación: -- {}\n{}".format(datetime.now(), notification_text))
                        self.p_target = round(p_actual + 0.1*mult_lim, 2)
                        file.write("Target {}: {} -- {}\n".format(self.tipo_lim, self.p_target, datetime.now()))
                        print("Target {}: {}".format(self.tipo_lim, self.p_target))

            sleep(60*2)
