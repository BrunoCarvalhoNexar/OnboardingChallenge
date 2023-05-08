class AvgTemperature:

    def __init__(self,temp):
       self.temperature = temp
    def hottest(self):
        return max(self.items(), key=lambda x: x[1])

    def coldest(temperature):
      return min(temperature.items(), key=lambda x: x[1])

    def avg_temperature(temperature):
      return sum(temperature) / 12




