#!/usr/bin/env python
# Purpose: To toggle a GPIO port that shows IP address of your Raspberry Pi in morse code
# Useful for if you do not have a monitor to use with Pi


import RPi.GPIO as GPIO
import subprocess
import time
import sys


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED = 21

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)


def main():
    '''
    Converts RPi's IP address to morse code and ouputs using LED.
    Program quits if no IP address is found within 5 minutes.
    '''
    try:
        ip = ''
        time_start = time.time()
        # Constantly searching for valid IP address. Quits if not IP found within 5 minutes
        while ip == '':
            ip = subprocess.check_output("ifconfig | grep \"inet \" | grep Bcast | \
                cut -f2 -d\':\' | cut -f1 -d\' \'", shell=True)
            time_now = time.time()
            time_since_start = time.strftime('%M', time.localtime(time_now - time_start))
            if int(time_since_start) >= 5:
                sys.exit()
        # Initialize morse code variable and strip the ip of all newline characters and spaces
        morse = ''
        ip = ip.strip()
        for num in ip:
            morse += str2morse(num)
        # IP address is flashed in morse code after 3 preliminary flashes
        # IMPORTANT! Short HIGH = Dot (1), Long HIGH = Dash (0)
        # Example: 127 = 10000 11000 00111
        for i in range(3):
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(LED, GPIO.LOW)
            time.sleep(2)
        for value in morse:
            if value == '1':
                GPIO.output(LED, GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(LED, GPIO.LOW)
                time.sleep(1)
            else:
                GPIO.output(LED, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(LED, GPIO.LOW)
                time.sleep(1)

    # If the user presses CTRL-C, set LED low
    except KeyboardInterrupt:
        GPIO.output(LED, GPIO.LOW)
    # Finally, cleanup the gpio before exiting program
    finally:
        GPIO.cleanup()


def str2morse(number):
    '''
    This function takes a string input called number (which will only be
    numbers and a period and translate it to morse code
    Dot = 1
    Dash = 0

    Args:
        number: string that represents one digit of ip addr.
    Returns:
        Morse code representation of number as a string.
    '''
    if number == '0':
        return '00000'
    elif number == '1':
        return '10000'
    elif number == '2':
        return '11000'
    elif number == '3':
        return '11100'
    elif number == '4':
        return '11110'
    elif number == '5':
        return '11111'
    elif number == '6':
        return '01111'
    elif number == '7':
        return '00111'
    elif number == '8':
        return '00011'
    elif number == '9':
        return '00001'
    elif number == '.':
        return '10101'


if __name__ == '__main__':
    main()
