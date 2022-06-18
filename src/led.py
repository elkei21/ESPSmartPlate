import machine
import time


def blink_led(led,num,t_on,t_off):
    counter=0
    while (counter<num):
        led.on()
        time.sleep(t_on)
        led.off()
        time.sleep(t_off)
        counter +=1
