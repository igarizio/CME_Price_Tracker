# -*- coding: utf-8 -*-
from scraper import Scraper
from notification import Notification
from logger import Logger
from time import sleep


class Traker:
    def __init__(self, contract, p_target, limit, sender_pass):
        self.logger = Logger()
        self.notif = Notification(sender_pass)

        self.contract = contract
        self.p_target = p_target
        self.limit = limit
        self.scraper = Scraper(self.contract)

    def track_prices(self):
        Logger.log_target(self.limit, self.p_target)

        while True:
            try:
                current_p = self.scraper.get_price()
                Logger.log_price(current_p)
            except Exception:
                Logger.log_price("ERROR")
                continue

            mult_lim = 1 if self.limit.lower() == "superior" else -1

            if self.p_target*mult_lim - current_p*mult_lim < 0:

                Logger.log_notif_intent()
                notif_txt = self.notif.send_notifications(current_p, self.p_target, round(current_p + 0.1 * mult_lim, 2), mult_lim == 1)
                Logger.log_notif_txt(notif_txt)

                self.p_target = round(current_p + 0.1*mult_lim, 2)
                Logger.log_target(self.limit, self.p_target)

            sleep(60*2)
