import time
import json
import sys
from pprint import pprint
import RPi.GPIO as GPIO

class Display:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(20, GPIO.OUT)
        while True:
            GPIO.output(20, 1)
        self.name = "display"
    def get_name(self):
        return self.name



