import lib.pcf8574
import machine
import var
import time

i2c = machine.I2C(scl=machine.Pin(15), sda=machine.Pin(4))
pcf1 = pcf8574.PCF8574(i2c, 0x20)
pcf2 = pcf8574.PCF8574(i2c, 0x24)

def blink_pin(pcf,pin,num,t_on,t_off):
    counter=0
    pcf_var=eval(pcf)
    while (counter<num):
        pcf_var.pin(pin, 1)
        var.board_led(pcf_var.pin(pin))
        time.sleep(t_on)
        pcf_var.pin(pin, 0)
        var.board_led(pcf_var.pin(pin))
        time.sleep(t_off)
        counter +=1

def test():
    for pin_n in range(8):
        blink_pin('pcf1',pin_n,num=1,t_on=1,t_off=1)
    for pin_n in range(4):
        blink_pin('pcf2',pin_n,1,1,1)
    

def test2():
    # read pin 2
    print(pcf1.pin(2))
    # set pin 3 HIGH
    pcf1.pin(3, 1)
    print(pcf.pin(3))
    # set pin 4 LOW
    pcf1.pin(4, 0)
    print(pcf.pin(4))
    # set all pins at once with 8-bit int
    pcf1.port = 0xff
    # toggle pin 5
    pcf1.toggle(5)
    print(hex(pcf.port))
    # read all pins at once as 8-bit int
    pcf1.port
