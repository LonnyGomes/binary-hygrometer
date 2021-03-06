import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22

class DHTSensor:
  def __init__(self, pin, temperatureOffset = 0, humidityOffset = 0):
    self.dht_pin = pin
    self.temperatureOffset = temperatureOffset
    self.humidityOffset = humidityOffset

  def getValues(self):
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, self.dht_pin)

    if humidity is not None and temperature is not None:
      # convert temperature to F
      temperature = (temperature * 1.8) + 32

      # apply value offets
      temperature += self.temperatureOffset
      humidity += self.humidityOffset
    else:
      print("Failed to retrieve data from humidity sensor") 
      humidity = -1
      temperature = -1

    return (temperature, humidity)

if __name__ == '__main__':
  dht = DHTSensor(4)
  temperature, humidity = dht.getValues()
  print("Temp={0:0.1f}*F  Humidity={1:0.1f}%".format(temperature, humidity))
