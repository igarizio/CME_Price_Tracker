# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from urllib import request


class Notification:
    def __init__(self, p_actual, p_target, p_target_nuevo, sobre_precio):
        self.p_actual = p_actual
        self.p_target = p_target
        self.p_target_nuevo = p_target_nuevo
        self.sobre_precio = sobre_precio

    def send_notifications(self):
        not_txt1 = self.send_ifttt()
        not_txt2 = self.send_email()
        return not_txt1 + "\n" + "-"*50 + "\n" + not_txt2

    def send_email(self):
        mail_from = "notificacioncme@gmail.com"
        mail_from_pass = "password del correo emisor" #Poner password real
        mail_to = ["correo_receptor_2@gmail.com", "correo_receptor_2@gmail.com"] #Poner correo reales
 
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(mail_from, mail_from_pass)

            pos = "sobre" if self.sobre_precio else "debajo"
            msg = MIMEText("""Hola\nEl precio actual del contrato futuro es de {}, valor por {} de tu precio target (que era de {}).\nPara evitar correos molestos, el nuevo target va a ser: {}"""
                           .format(self.p_actual, pos, self.p_target, self.p_target_nuevo))

            msg['Subject'] = "Precio por {} de tu target".format(pos)
            msg['From'] = mail_from
            msg['To'] = ", ".join(mail_to)

            server.sendmail(mail_from, mail_to, msg.as_string())
            server.quit()
            return msg.as_string()

        except Exception:
            return "---> Error al enviar correo."

    def send_ifttt(self):
        url_get = "https://maker.ifttt.com/trigger/price_alert/with/key/{poner key real de IFTTT}" #Pner key de ususario real de IFTTT
        req = request.Request(url_get)
        try:
            with request.urlopen(req) as response:
                html = response.read().decode("utf-8", "ignore")
                return "Notificación enviada a IFTTT: \n" + html
        except Exception:
            print("error ifttt")
            return "---> Error al enviar notificación."
