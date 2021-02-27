from blinkt import set_pixel, set_brightness, show, clear
from signal import pause
import time

ANIMATION_DELAY=0.001

class BlinktLEDs:
  def __init__(self, ledCount):
    self.ledCount = ledCount
 
  def animateOff(self):
    for idx in reversed(range(self.ledCount)):
      set_pixel(idx, 0, 0, 0)
      show()
      time.sleep(ANIMATION_DELAY)

  def setLEDs(self, leds, rgb = (0, 0, 255)):
    self.animateOff()

    foundFirstDigit = False
    dim = .2
    dimRGB = [255, 191, 0]

    # fill leds based leds array
    for i in range(len(leds)):
      if (leds[i] == 1):
        foundFirstDigit = True
        set_pixel(i, rgb[0], rgb[1], rgb[2], 0.3)
        show()
        time.sleep(ANIMATION_DELAY)
      else:
        # we only want to fill colors if the first digit
        # has already been encountered
        if foundFirstDigit:
          set_pixel(i, dimRGB[0] * dim, dimRGB[0] * dim, dimRGB[0] * dim, 0.1)
          show()
          time.sleep(ANIMATION_DELAY)
        else:
          # don't sleep for these pixels
          set_pixel(i, 0, 0, 0)
          show()

if __name__ == '__main__':
  blinkt = BlinktLEDs(8)

  leds = [0, 0, 0, 1, 0, 1, 1, 0 ]
  blinkt.setLEDs(leds)
  time.sleep(5)
