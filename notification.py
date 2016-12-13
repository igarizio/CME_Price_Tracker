# -*- coding: utf-8 -*-
import smtplib
import json
from email.mime.text import MIMEText
from urllib import request
from configparser import ConfigParser


class Notification:
    def __init__(self, sender_pass):
        self.parser = ConfigParser()
        self.parser.read('config.ini')

        self.__sender_mail = self.parser.get('email', 'sender')
        self.__sender_pass = sender_pass

    def send_notifications(self, actual_p, target_p, target_p_new, sobre_precio):
        notif_email = self.send_email(actual_p, target_p, target_p_new, sobre_precio)
        notif_ifttt = self.send_ifttt()

        return notif_email + "\n" + "-"*50 + "\n" + notif_ifttt

    def send_email(self, actual_p, target_p, target_p_new, sobre_precio):
        mail_from = self.__sender_mail
        mail_from_pass = self.__sender_pass
        mail_to = json.loads(self.parser.get('email', 'receivers'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(mail_from, mail_from_pass)

            pos = "sobre" if sobre_precio else "debajo"
            msg = MIMEText("""Hola\nEl precio actual del contrato futuro es de {}, valor por {} de tu precio target (que era de {}).\nPara evitar correos molestos, el nuevo target va a ser: {}"""
                           .format(actual_p, pos, target_p, target_p_new))

            msg['Subject'] = "Precio por {} de tu target".format(pos)
            msg['From'] = mail_from
            msg['To'] = ", ".join(mail_to)

            server.sendmail(mail_from, mail_to, msg.as_string())
            server.quit()
            return msg.as_string()

        except Exception:
            return "---> Error al enviar correo."

    def send_ifttt(self):
        url_get = self.parser.get('urls', 'ifttt') + self.parser.get('urls', 'ifttt_key')
        req = request.Request(url_get)

        try:
            with request.urlopen(req) as response:
                html = response.read().decode("utf-8", "ignore")
                return "Notificación enviada a IFTTT: \n" + html
        except Exception:
            return "---> Error al enviar notificación IFTTT."
