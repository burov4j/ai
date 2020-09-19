class Car:
    speed = 0

    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed += 20
        print(f"Speed increased to {self.speed}")

    def stop(self):
        self.speed = 0
        print("Car is stopped")

    def turn(self, direction):
        print(f"Car is turned to {direction}")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, color, name):
        super(TownCar, self).__init__(color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Slow down!")


class SportCar(Car):
    def __init__(self, color, name):
        super(SportCar, self).__init__(color, name, False)


class WorkCar(Car):
    def __init__(self, color, name):
        super(WorkCar, self).__init__(color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Slow down!")


class PoliceCar(Car):
    def __init__(self, color, name):
        super(PoliceCar, self).__init__(color, name, True)


car = PoliceCar('blue', 'super_car')
print(car.is_police)
car.go()
car.go()
car.go()
car.show_speed()

car = WorkCar('black', 'slow_car')
print(car.is_police)
car.go()
car.go()
car.go()
car.show_speed()
car.stop()
car.show_speed()
