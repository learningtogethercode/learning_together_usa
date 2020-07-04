import aiy.toneplayer
from time import sleep
from gpiozero import Servo
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)
from multiprocessing import Process
from aiy.pins import PIN_A

simple_servo = Servo(PIN_A, min_pulse_width=.0004, max_pulse_width=.0019)

#do re mi fa sol la si
#c  d  e  f  g   a  b
def himn():
    himn_usa = [
    
        'C5', 'A4', 'F4', 'A4', 'C5', 'F5', 'A5', 'G5', 'F5', 'A4', 'B4', 'C5',
        'C5', 'C5', 'A5', 'G5', 'F5', 'E5', 'D5', 'E5', 'F5', 'A4', 'B4', 'C5',
        
    ]
    
    player = aiy.toneplayer.TonePlayer(22)
    player.play(*himn_usa)
    
def flag():
    for i in range(4):
        with Leds() as leds:
            leds.update(Leds.rgb_on(Color.BLUE))
            sleep(1)

            leds.update(Leds.rgb_on(Color.RED))
            sleep(1)

            leds.update(Leds.rgb_on(Color.WHITE))
            sleep(1)

def kids():
    for i in range(1):
        for i in range(10, -1, -1):
            value = (float(i)-10)/10
            simple_servo.value = value
            print(value)
            sleep(0.13)
        print('Termina primer loop')
        for i in range(1, 20):
            value = (float(i)-10)/10
            simple_servo.value = value
            print(value)
            sleep(0.13)
        print('Termina segundo loop')
        for i in range(20, -1, -1):
            value = (float(i)-10)/10
            simple_servo.value = value
            print(value)
            sleep(0.13)
        print('Termina tercer loop')
        for i in range(1, 21):
            value = (float(i)-10)/10
            simple_servo.value = value
            print(value)
            sleep(0.13)
        print('Termina cuarto loop')
        for i in range(19, 9, -1):
            value = (float(i)-10)/10
            simple_servo.value = value
            print(value)
            sleep(0.13)
 
if __name__ == '__main__':
    for i in range(5):
        p1 = Process(target=flag)
        p1.start()
        p2 = Process(target=himn)
        p2.start()
        p3 = Process(target=kids)
        p3.start()
        p1.join()
        p2.join()
        p3.join()
