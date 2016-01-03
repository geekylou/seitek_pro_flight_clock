# seitek_pro_flight_clock

This adds support for setting the clock on the front of the Seitek Pro Flight Yoke to linux.  To use you will first need to install pyusb 'pip install pyusb' and the run python seitek_clock.py as root.

This can also be used on Windows if you are not using the standard usbhid ('not seitek') drivers.  However you will also need to install a filter driver to enable pyusb to work.