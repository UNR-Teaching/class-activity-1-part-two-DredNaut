#!/usr/bin/env python3
from wayne import Pinto
from garth import BMX

def main():

    wayne = Pinto('Blue')
    wayne.print_speed()
    wayne.print_color()

    garth = BMX('White')
    garth.print_speed()
    garth.print_color()

main()
