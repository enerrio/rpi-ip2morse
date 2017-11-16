# rpi-ip2morse
Python program to convert Raspberry Pi's IP address to morse code and display using LED

## Problem
---
Usually a Raspberry Pi is used with a monitor, mouse, and keyboard. But when those aren't available then the only other option is to ssh into it, but first you need to know the IP address of the RPi. And if you are connecting to the internet in a public area then often times the RPi's IP address changes every time it is turned on. So it would be very difficult to ssh into the RPi if you don't know the IP address and you don't have a monitor.

## Solution
---
This python program is run on the RPi and searches for the an ip address, converts it to morse code, and outputs it using an LED connected to 2 pins on the RPi. Simply connect a LED to pin 40 and ground of the RPi and plug in the RPi. Then the LED will flash the RPi's IP address and you can then ssh into the RPi without a monitor. If no IP address is found within 5 minutes then the program exits.


**IMPORTANT:** I originally documented this project on hackster.io and my write-up can be found [here](https://www.hackster.io/aaron-marquez/find-ip-address-via-morse-code-7ff658). There I give a detailed description of the code as well as how to set up the python script to run during bootup. There is also a video demonstration of the program in action.
