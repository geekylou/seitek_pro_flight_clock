import time

import usb.core
import usb.util

class SeitekFlightYoke(object): 
    def __init__(self):
        self.dev = usb.core.find(idVendor=0x06a3,idProduct=0x0bac)

        endpoint = self.dev[0][(0,0)][0]
        self.tm_sec = -1
        
    def tick(self):
            extracted_time = time.localtime()
            if extracted_time.tm_sec != self.tm_sec:
                self.tm_sec = extracted_time.tm_sec
                self.dev.ctrl_transfer(usb.util.CTRL_OUT | usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_RECIPIENT_DEVICE, 0x91, extracted_time.tm_sec << 8 | extracted_time.tm_sec, 0x00CA, "") 
                self.dev.ctrl_transfer(usb.util.CTRL_OUT | usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_RECIPIENT_DEVICE, 0x91, extracted_time.tm_hour  << 8 | extracted_time.tm_min, 0x00C0, "")
                      
if __name__ == "__main__":
    seitek_yoke = SeitekFlightYoke()
    while True:
        seitek_yoke.tick()
        time.sleep(1)
        

