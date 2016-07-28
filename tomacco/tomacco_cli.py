#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import dbus
import argparse

bus = dbus.SessionBus()
obj = bus.get_object("org.prog.tomacco", "/org/prog/tomacco")
interface = dbus.Interface(obj, "org.prog.tomacco")

parser= argparse.ArgumentParser()
subparser = parser.add_subparsers()

parser_start = subparser.add_parser('start')
parser_start.set_defaults(func=interface.start)

parser_stop = subparser.add_parser('stop')
parser_stop.set_defaults(func=interface.stop)

parser_spause = subparser.add_parser('spause')
parser_spause.set_defaults(func=interface.spause)

parser_lpause = subparser.add_parser('lpause')
parser_lpause.set_defaults(func=interface.lpause)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func()
