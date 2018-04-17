class Vehicle(object):
    def __init__(self, seat, engine_type, turning_mechanism):
        self.seat = seat
        self.engine_type = engine_type
        self.turning_mechanism = turning_mechanism

    def move(self):
        print("You Moved forward")

    def change_direction(self):
        print("You change direction")


class Car(Vehicle):
    def __init__(self, seat, horsepower):
        super(Car, self).__init__(seat, 'engine', 'steering wheel')
        self.hp = horsepower

    def turn_on(self):
        print("You turn the key and the engine starts")

test_car = Car(4, 9001)
test_car.turn_on()
test_car.change_direction()
print(test_car.turning_mechanism)



class KeylessCar(Car):
    def __init__(self, seats, hp):
        super(KeylessCar, self).__init__(seats, hp)

    def turn_on(self):
        print("You push the button and the car turns on")


test_car.turn_on()
cool_car = KeylessCar(4, 9002)
cool_car.turn_on()


class Tesla(Car):
    def __init__(self, seat):
        super(Tesla, self).__init__(seat, 500)

    def launch(self):
        print("You launch the car into low earth orbit")
