class AvgTemperature:

    def hottest(temperature):
        return max(temperature.items(), key=lambda x: x[1])

    def coldest(temperature):
      return min(temperature.items(), key=lambda x: x[1])

    def avg_temperature(temperature):
      return sum(temperature) / 12




