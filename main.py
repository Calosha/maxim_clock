#!/usr/bin/env python3

from tm1637 import TM1637
from time import time, sleep, localtime

DIO=20
CLK=21

def show_clock(tm):
    t = localtime()
    sleep(1 - time() % 1)
    hour = t.tm_hour
    if hour != 12:
        hour = hour % 12
    tm.numbers(hour, t.tm_min, True)
    sleep(.5)
    tm.numbers(hour, t.tm_min, False)

tm = TM1637(CLK, DIO)
tm.brightness(1)
    
while True:
    show_clock(tm)
