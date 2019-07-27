'''
MAX 7219
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.
# https://max7219.readthedocs.io/en/0.2.3/
# modified by Peter Chan
# July 2019
'''

# import MAX7219 related modules
import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

class LED_mat:

    def __init__(self):
        
        ### Maxim7219 8x8 LED matrix coding
        # create matrix device
        self.serial = spi(port=0, device=0, gpio=noop())
        self.ledMat = max7219(self.serial, cascaded=1, block_orientation=0,rotate=0, blocks_arranged_in_reverse_order=False)

    def led_matrix(self, msg):
        with canvas(self.ledMat) as draw:
            text(draw, (0, 0), msg, fill="white")
        time.sleep(0.05)
    ### Maxim7219 8x8 LED matrix coding

def main():
    
    mt7219 = LED_mat()
    for i in range(256):
        mt7219.led_matrix(chr(i))
        print('CP437 character:', i)
        time.sleep(1)
    mt7219.led_matrix(chr(0))

if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print('Bye')
