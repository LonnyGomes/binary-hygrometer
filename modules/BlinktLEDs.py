from blinkt import set_pixel, set_brightness, show, clear
from signal import pause
import time

class BlinktLEDs:
  def __init__(self):
   pass
 
  def setLEDs(self, leds, rgb = (0, 0, 255)):
    clear()

    foundFirstDigit = False
    dim = 0.2
    dimRGB = [255, 255, 255]

    # fill leds based leds array
    for i in range(len(leds)):
      if (leds[i] == 1):
        foundFirstDigit = True
        set_pixel(i, rgb[0], rgb[1], rgb[2], 0.8)
      else:
        # we only want to fill colors if the first digit
        # has already been encountered
        if foundFirstDigit:
          set_pixel(i, dimRGB[0] * dim, dimRGB[0] * dim, dimRGB[0] * dim, 0.1)

    show()

if __name__ == '__main__':
  blinkt = BlinktLEDs()

  leds = [0, 0, 0, 1, 0, 1, 1, 0 ]
  blinkt.setLEDs(leds)
  time.sleep(5)
