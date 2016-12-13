from configparser import ConfigParser
from datetime import datetime


class Logger:

    @staticmethod
    def __write_to_log__(txt):
        parser = ConfigParser()
        parser.read('config.ini')

        log_file = parser.get('files', 'log_file')

        with open(log_file, 'a+') as file:
            file.write(txt)

    @staticmethod
    def log_target(limit, p_target):
        Logger.__write_to_log__("Target {}: {} -- {}\n".format(limit, p_target, datetime.now()))

    @staticmethod
    def log_price(current_p):
        Logger.__write_to_log__("Precio actual: {}  -- {}\n".format(current_p, datetime.now()))

    @staticmethod
    def log_notif_intent():
        Logger.__write_to_log__("Enviando notificación: -- {}\n".format(datetime.now()))

    @staticmethod
    def log_notif_txt(notif_txt):
        Logger.__write_to_log__("{}\n{}\n{}\n".format("-"*50, notif_txt, "-"*50))