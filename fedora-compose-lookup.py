#!/usr/bin/env python

import argparse
import re as regex
import fileinput
import json
import sys

def main():
    argparser = argparse.ArgumentParser(
        prog='fedora-compose-lookup',
        description='Simple script to look up Fedora Rawhide composes \
            and compare them'
        )

    argparser.add_argument(
        '-l',
        '--list',
        metavar='N',
        help='Lists Fedora Rawhide composes released within the last N days.'
        )
    argparser.add_argument(
        'COMPOSE',
        nargs=2,
        help='Two specific Fedora Rawhide composes to compare, specified \
            by their name in the format of YYYYMMDD.n.N where N is \
            the compose\'s ordinal number within the given day \
            starting with 0.'
        )

    args = argparser.parse_args()


if __name__ == '__main__':
    main()
