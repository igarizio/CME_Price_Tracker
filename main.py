# -*- coding: utf-8 -*-
from tracker import Traker
from configparser import ConfigParser
import argparse
import getpass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("contract", help="Tipo de contrato")
    parser.add_argument("target", help="Precio target", type=float)
    parser.add_argument("limit", help="Tipo de límite: Superior o inferior")
    args = parser.parse_args()

    if args.limit == "superior" or args.tipo_lim == "inferior":
        config_parser = ConfigParser()
        config_parser.read('config.ini')
        sender_pass = getpass.getpass("Ingrese contraseña de {}: ".format(config_parser.get('email', 'sender'))) #funciona desde consola

        t = Traker(args.contract, args.target, args.limit, sender_pass)
        t.track_prices()
    else:
        print("El tipo de límite debe ser: superior o inferior")

