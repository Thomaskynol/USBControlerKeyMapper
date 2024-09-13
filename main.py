import usb.core
import pyautogui
import time
import os
#045e:028e
dev = usb.core.find(idVendor=0x045e, idProduct=0x0028e)

if dev is None:
    raise ValueError('Device not found')

ep = dev[0].interfaces()[0].endpoints()[0]
i = dev[0].interfaces()[0].bInterfaceNumber
dev.reset()

dev.default_timeout = 0

if dev.is_kernel_driver_active(i):
    dev.detach_kernel_driver(i)
    
dev.set_configuration()
eaddr = ep.bEndpointAddress 

current_key = None

def hold_key(value):
    global current_key
    
    if value == 1:
        current_key = 'up'
        pyautogui.keyDown(current_key)
    elif value == 2:
        current_key = 'down'
        pyautogui.keyDown(current_key)
    elif value == 4:
        current_key = 'left'
        pyautogui.keyDown(current_key)
    elif value == 8:
        current_key = 'right'
        pyautogui.keyDown(current_key)
    elif value == 0:
        if current_key is not None:
            pyautogui.keyUp(current_key)
            current_key = None
        return
    
try:
    while True:
        infos = dev.read(eaddr, 1024)
        print(infos[2])
        hold_key(infos[2])
 
except KeyboardInterrupt:
    print("\nInterrupção de teclado detectada. Encerrando o programa.")