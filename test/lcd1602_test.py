import i2c_lcd_driver as lcd1602
from time import *

mylcd = lcd1602.lcd()
mylcd.lcd_display_string("Hello World!",1)
mylcd.lcd_display_string("Test LCD1602",2,3)
sleep(3)
mylcd.lcd_clear()
