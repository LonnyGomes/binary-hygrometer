import time
from modules.DHTSensor import DHTSensor

LED_COUNT = 8
DHT_PIN = 4

def setLED(rawInputVal):
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

dht = DHTSensor(DHT_PIN)

while True:
  temperature, humidity = dht.getValues()
  print("Temp={0:0.1f}*F  Humidity={1:0.1f}%".format(temperature, humidity))
  leds = setLED(humidity)
  print(leds)
  time.sleep(10)
