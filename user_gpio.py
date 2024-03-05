# Copyright (c) 2019, Digi International, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from machine import Pin

# Pin D9 (ON/SLEEP/DIO9)
LED_RED_PIN_ID = "D9"
LED_GREEN_PIN_ID = "D9"

INPUT_BUTTON_PIN_ID = "D0"


class UserLed:
    def __init__(self):
        # init led gpio
        print(" +--------------------------------------+")
        print(" | XBee MicroPython Blinking LED Sample |")
        print(" +--------------------------------------+\n")
        self.led_red = Pin(LED_RED_PIN_ID, Pin.OUT, value=0)
        self.led_green = Pin(LED_GREEN_PIN_ID, Pin.OUT, value=0)

    def led_red_control(self=0, control=0):
        print("- led red control:" % control)
        self.led_red.value(control)

    def led_green_control(self=0, control=0):
        print("- led green control:" % control)
        self.led_green.value(control)


class UserButton:
    def __init__(self):
        print("- init button gpio init called")
        self.button = Pin(INPUT_BUTTON_PIN_ID, Pin.IN, Pin.PULL_UP)

    def button_check(self):
        return self.button.value()
