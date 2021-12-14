class Vehicle:
        def __init__(self, started = False, speed = 0): 
            self.started = started
            self.speed = speed

        def start(self):
            self.started = True
            print("Started, Lets`s Gooooooo!")

        def increase_speed(self, delta):
            if self.started:
                self.speed = self.speed + delta
                print("Vroooom!")

            else:
                print('Start the car first')

        def stop(self):
            self.speed = 0
            print('HALTEDDDDD')

class Car(Vehicle):
    trunk_open = False

    def open_trunk(self):
            self.trunk_open = True
    def close_trunk(self):
        self.trunk_open = False

car = Car()
car.start()
car.increase_speed(40)
car.stop()