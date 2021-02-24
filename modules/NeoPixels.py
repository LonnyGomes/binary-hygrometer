#!/usr/bin/python3

import board
import neopixel
import time

class NeoPixels:
  # color order configurations
  GRBW = neopixel.GRBW
  RGBW = neopixel.RGBW
  RGB = neopixel.RGB
  GRB = neopixel.GRB

  # available PIN layouts
  D10 = board.D10
  D12 = board.D12
  D18 = board.D18
  D21 = board.D21

  # NeoPixels must be connected to D10, D12, D18 or D21 to work.
  def __init__(self, pixelPin, pixelCount, order):
    self.pixelCount = pixelCount
    self.pixels = neopixel.NeoPixel(\
      pixelPin, pixelCount, brightness=1,\
      auto_write=False, pixel_order=order\
    )

  # funciton definions
  def animateOff(self):
    for pixelIdx in reversed(range(self.pixelCount)):
      self.pixels[pixelIdx] = (0, 0, 0, 0)
      self.pixels.show()
      time.sleep(0.05)

  def animateOn(self, rgbw = (0, 0, 0, 255)):
    for pixelIdx in range(self.pixelCount):
      self.pixels[pixelIdx] = rgbw
      self.pixels.show()
      time.sleep(0.05)

  def setLEDs(self, leds, rgbw = (0, 0, 255)):
    foundFirstDigit = False
    dim = 0.2
    dimRGBW = (0, 0, 0, 255 * dim)

    self.animateOff()

    # fill leds based leds array
    for pixelIdx in range(len(leds)):
      if (leds[pixelIdx] == 1):
        foundFirstDigit = True
        self.pixels[pixelIdx] = rgbw
      else:
        # we only want to fill colors if the first digit
        # has already been encountered
        if foundFirstDigit:
          self.pixels[pixelIdx] = dimRGBW
        else:
          # black out pixel if first hasn't been encountered yet
          self.pixels[pixelIdx] = (0, 0, 0, 0)

      self.pixels.show()
      time.sleep(0.05)

if __name__ == '__main__':
  try:
    # remove after testing
    leds = [0, 0, 0, 1, 0, 1, 1, 0 ]
    np = NeoPixels(NeoPixels.D21, 8, NeoPixels.GRBW)
    np.setLEDs(leds)
    time.sleep(5)
    np.animateOff()
    #blinkt.setLEDs(leds)
  except (KeyboardInterrupt, SystemExit) as exErr:
    print("Closing down application")
  finally:
    pass
