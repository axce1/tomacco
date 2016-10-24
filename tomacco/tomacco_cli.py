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

parser_show = subparser.add_parser('show')
parser_show.set_defaults(func=interface.show)

parser_hide= subparser.add_parser('hide')
parser_hide.set_defaults(func=interface.hide)


def main():
    args = parser.parse_args()
    args.func()

if __name__ == '__main__':
    main()
