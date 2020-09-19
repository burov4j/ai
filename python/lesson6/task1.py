import time


class TrafficLight:
    __color = "red"

    def running(self):
        self.__color = "red"
        print(self.__color)
        time.sleep(7)
        self.__color = "yellow"
        print(self.__color)
        time.sleep(2)
        self.__color = "green"
        print(self.__color)
        time.sleep(5)


trafficLight = TrafficLight()
trafficLight.running()
