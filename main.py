# -*- coding: utf-8 -*-
from tracker import Traker
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("contract", help="Tipo de contrato")
    parser.add_argument("target", help="Precio target", type=float)
    parser.add_argument("tipo_lim", help="Tipo de límite: Superior o inferior")
    args = parser.parse_args()

    if args.tipo_lim == "superior" or args.tipo_lim == "inferior":
        t = Traker(args.contract, args.target, args.tipo_lim)
        t.track_prices()
    else:
        print("El tipo de límite debe ser: superior o inferior")
