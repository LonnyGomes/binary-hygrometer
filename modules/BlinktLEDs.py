from blinkt import set_pixel, set_brightness, show, clear
from signal import pause
import time

class BlinktLEDs:
  def __init__(self):
   pass
 
  def setLEDs(self, leds):
    clear()
    set_brightness(.5)

    # fill leds based leds array
    for i in range(len(leds)):
      if (leds[i] == 1):
        set_pixel(i, 0, 255, 0)
    show()

if __name__ == '__main__':
  blinkt = BlinktLEDs()

  leds = [0, 0, 0, 1, 0, 1, 1, 0 ]
  blinkt.setLEDs(leds)
  time.sleep(5)
