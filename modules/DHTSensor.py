import board
import adafruit_dht

class DHTSensor:
  def __init__(self, pin):
    self.dht_pin = pin
    self.dhtDevice = adafruit_dht.DHT22(board.D4)

  def getValues(self):
    try:
      temperature = self.dhtDevice.temperature
      temperature = (temperature * 1.8) + 32
      humidity= self.dhtDevice.humidity

      return (temperature, humidity)
    except RuntimeError as error:
      print("Failed to retrieve data from humidity sensor") 
      print(error.args[0])
      humidity = -1
      temperature = -1
    except Exception as error:
      dhtDevice.exit()
      raise error

if __name__ == '__main__':
  dht = DHTSensor(4)
  temperature, humidity = dht.getValues()
  print("Temp={0:0.1f}*F  Humidity={1:0.1f}%".format(temperature, humidity))
