from modules.Button import Button
import time
import RPi.GPIO as GPIO
import sys
from tm1637 import TM1637
from itertools import cycle
menu_val = cycle(range(3))
#help(cycle)
# etc.
#help(TM1637)

#sys.exit(0)


PIN = 16



DIO=20
CLK=21

#def show_clock(tm):
#    t = localtime()
#    sleep(1 - time() % 1#)
#  hour = t.tm_hour
#    if hour != 12:
#        hour = hour % 12
#    tm.numbers(hour, t.tm_min, True)
#    sleep(.5)
#    tm.numbers(hour, t.tm_min, False)
#
#tm = TM1637(CLK, DIO)
#tm.brightness(1)
#    
#while True:
#    show_clock(tm)

menu = ["alrm", "temp", "cncl"]
state = [menu] 



tm = TM1637(CLK, DIO)
tm.brightness(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
skip_short = False
while True:
    GPIO.wait_for_edge(PIN, GPIO.FALLING)
    print ("Pressed")
    time.sleep(0.02)
    start = time.time()
    while GPIO.input(PIN) == GPIO.LOW:
        length = time.time() - start
        time.sleep(0.01) 
        if length > 1:
            tm.show(menu[0])
            break
    else:
        tm.show(menu[next(menu_val)])
