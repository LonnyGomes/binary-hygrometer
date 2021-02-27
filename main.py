#!/usr/bin/python3

import time
from modules.DHTSensor import DHTSensor
from modules.BlinktLEDs import BlinktLEDs
from modules.NeoPixels import NeoPixels

LED_COUNT = 8
DHT_PIN = 14

DHT_TEMPERATURE_OFFSET = 0
DHT_HUMIDITY_OFFSET = -14

def calcLEDs(rawInputVal):
  ledVals = [0] * LED_COUNT

  # verify for valid value
  if rawInputVal < 0 or rawInputVal > 100:
      print("Value must be between 0 and 100")
      return ledVals

  # round input value to an int
  inputVal = int(round(rawInputVal))

  # convert number to binary string
  binaryStr = format(inputVal, 'b')

  # loop through 
  offsetIdx = LED_COUNT - len(binaryStr)

  # populate LED array where 1 = LED ON and 0 = LED OFF
  for idx in range(0, len(binaryStr)):
    ledVals[idx + offsetIdx] = int(binaryStr[idx]) 

  return ledVals

dht = DHTSensor(DHT_PIN, DHT_TEMPERATURE_OFFSET, DHT_HUMIDITY_OFFSET)
blinkt = BlinktLEDs(LED_COUNT)
np = NeoPixels(NeoPixels.D21, LED_COUNT, NeoPixels.GRBW)

humidityClr = [0, 0, 255]
humidityRgbw = (0, 0, 255, 0)
temperatureClr = [255, 0, 0]
temperatureRgbw = (255, 0, 0, 0)
isHumidity = True

while True:
  try:
    temperature, humidity = dht.getValues()
    print("Temp={0:0.1f}*F  Humidity={1:0.1f}%".format(temperature, humidity))

    # determine which value to display
    curClr = humidityClr if isHumidity else temperatureClr
    curRgbw = humidityRgbw if isHumidity else temperatureRgbw
    curVal = humidity if isHumidity else temperature
    leds = calcLEDs(curVal)

    # display the value on LED strip
    blinkt.setLEDs(leds, curClr)
    np.setLEDs(leds, curRgbw)
    time.sleep(10)

    #toggle value
    isHumidity = not isHumidity
  except ValueError as error:
    # failing to read this type of sensor is common, try again
    continue

